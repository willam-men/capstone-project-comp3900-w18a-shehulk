
import json
from uuid import UUID
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from json import dumps
from project.meal_plan import get_meal_plan, delete_meal_plan, add_meal_plan, get_ingredients_meal_plan
from project.ingredients import find_differences_ingredients, add_ingredients_to_recipe, get_old_ingredients
from project.pantry import add_list_to_pantry, find_the_missing_ingredients, get_pantry, is_makeable, find_recipes_based_on_pantry
from project.auth import is_valid_token, token_to_id, destroy_token, get_current_user, check_if_username_email_exists, register_user, find_user_from_email, check_password_correct
from project.models.orm import UserOrm, IngredientsOrm
from project.recipe import fill_recipe_fields, insert_recipe, update_published_recipes_for_user, get_recipe, get_recipes_by_page, edit_recipe, like_recipe, unlike_recipe, get_recipes_by_user, get_recipes_by_subscription, search_recipes, delete_recipe, recommended_recipes, author_matches
from project.error import AccessError, InputError, default_handler, NotFoundError
from project.user import add_subscription, remove_subscription, get_user_info, get_user_info_by_id, get_all_user_info, remove_recipe_from_user
from project.comments import create_comment,get_comments,edit_comment,delete_comment, rate_comment, get_average_rating, delete_comments_from_recipe
from project.profile import update_profile, update_user_credentials


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, default_handler)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


#######################################################################
#                   USER AUTHENTICATION                               #
#######################################################################

@app.route("/api/register", methods=['POST'])
@cross_origin()
def register_user_json() -> json:
    """Used to Register a new user of Ratatouille 

    Raises:
        InputError: Username/email/password/name was not given

    Returns:
        Json: {"token": string of current valid token for the given user}
    """
    try:
        username = request.get_json()['username']
        email = request.get_json()['email']
        name = request.get_json()['name']
        password = request.get_json()['password']
    except:
        raise InputError('Bad Request: Please provide an email and password')

    if not username or not email or not password:  # or not name or not password:
        raise InputError('Bad Request: Please provide all required fields')

    check_if_username_email_exists(username, email)
    return dumps(register_user(username, email, name, password), default=str)


@app.route("/api/login", methods=['POST'])
@cross_origin()
def login_user() -> json:
    """This wrapper endpoint is used for user login using a username and password

    Raises:
        InputError: If an email/password was not given

    Returns:
        JSON: {"token": string of current valid token for the given user}
    """
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
    except:
        raise InputError('Bad Request: Please provide an email and password')

    if not data or not email or not password:
        raise InputError('Bad Request: Please provide an email and password')

    sql_query_credentials = find_user_from_email(email)
    return dumps(check_password_correct(password, sql_query_credentials), default=str)


@app.route("/api/logout", methods=['POST'])
@cross_origin()
def logout_user_json() -> json:
    """Used to log a user out of the system

    Raises:F
        InputError: If there is no current user logged in/ errors when logging out

    Returns:
        json: empty json
    """
    try:
        token = request.get_json()["token"]
    except:
        raise InputError("There is no user currently logged in")

    if destroy_token(token):
        return dumps({})

    raise InputError("There was an error in logging out. Please try again.")


@app.route("/api/recipes", methods=['GET'])
@cross_origin()
def recipes() -> list[dict]:
    """Returns all recipe details in database

    Returns:
        list[json]: List of all recipe details
    """
    recipes = get_recipes_by_page()
    return dumps(recipes, default=str)


@app.route("/api/recipe", methods=['GET'])
@cross_origin()
def recipe() -> json:
    """Returns a recipe with given recipeId

    Raises:
        AccessError: Current logged in token is invalid

    Returns:
        json: Details of a recipe with given recipeId
    """
    recipe_id = request.args.get('recipeId')
    token = request.headers.get('token')
    recipe = get_recipe(recipe_id)
    if recipe is None:
        raise NotFoundError("recipe can't be found")
    recipe['isLiked'] = False
    recipe['inMealPlan'] = False
    recipe['isMakeable'] = False
    recipe['ratings'] = get_average_rating(recipe_id)
    if not token:
        pass
    elif not is_valid_token(token):
        raise AccessError("token is invalid")
    else:
        curr_user = token_to_id(token)
        if curr_user in recipe['likedList']:
            recipe['isLiked'] = True
        recipe['isMakeable'] = is_makeable(curr_user, recipe_id)
        meal_plans = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == curr_user).dicts().first()['mealPlans']
        if (UUID(recipe_id) in meal_plans):
            recipe['inMealPlan'] = True
        else:
            recipe['inMealPlan'] = False
        recipe['mealPlans'] = meal_plans
    recipe.pop('likedList')
   
    return dumps(recipe, default=str)


@app.route("/api/recipe", methods=['DELETE'])
@cross_origin()
def delete_recipe_from_db() -> json:
    """Deletes a recipe with id=recipe_id from the database 

    Raises:
        AccessError: If the token is invalid
        NotFoundError: If the user is not the publisher of the recipe

    Returns:
        json: Empty json, if successful
    """
    recipe_id = request.get_json()['recipeId']
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user = token_to_id(token)
    recipe = get_recipe(recipe_id)
    # check curr_user is the author
    if (curr_user != recipe['authorId']):
        raise NotFoundError("User does not have permission to delete this recipe")
    ## delete recipe from ingredientsorm
    remove_ingredients = [ingred['ingredient'] for ingred in recipe['ingredients']]
    add_ingredients_to_recipe([], remove_ingredients, UUID(recipe_id))
    delete_comments_from_recipe(recipe_id)
    remove_recipe_from_user(curr_user, recipe_id)
    return delete_recipe(recipe_id)
    

@app.route("/api/recipe/user", methods=['GET'])
@cross_origin()
def recipe_if_user_is_publisher() -> json:
    """Returns a recipe with given recipeId if the user is the publisher

    Raises:
        AccessError: Current logged in token is invalid

    Returns:
        json: Details of a recipe with given recipeId
    """
    recipe_id = request.args.get('recipeId')
    token = request.headers.get('token')
    recipe = get_recipe(recipe_id)
    recipe['isLiked'] = False
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user = token_to_id(token)
    if (curr_user != recipe['authorId']):
        raise NotFoundError(
            "User does not have permission to edit this recipe")
    if curr_user in recipe['likedList']:
        recipe['isLiked'] = True
    recipe.pop('likedList')
    return dumps(recipe, default=str)


@app.route("/api/subscribe", methods=['POST'])
@cross_origin()
def subscribe() -> json:
    """Function to subscribe to a user

    Raises:
        AccessError: Token is invalid

    Returns:
        json: Empty json
    """
    data = request.get_json()
    token = request.headers['token']
    publisher = int(data.get('userId'))
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    subscriber = token_to_id(token)
    add_subscription(subscriber, publisher)
    return dumps({})


@app.route("/api/unsubscribe", methods=['POST'])
@cross_origin()
def unsubscribe() -> json:
    """Function to unsubscribe to a user

    Raises:
        AccessError: Token is invalid

    Returns:
        json: Empty json
    """
    data = request.get_json()
    token = request.headers['token']
    publisher = int(data.get('userId'))
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    subscriber = token_to_id(token)
    remove_subscription(subscriber, publisher)
    return dumps({})


@app.route("/api/profile/<string:userId>/update", methods=['POST'])
@cross_origin()
def update_user_prof(userId):
    '''The Post function takes in a JSON object and updates a given users profile.
       It requires that atleast one of name, title, bio, pfp be passed alongside a users token
    '''
    data = request.get_json()
    if 'token' not in data or len(data) <= 1 or len(data) > 5:
        raise InputError("Error invalid parameters")
    token = data['token']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    userId2 = str(token_to_id(token))
    name = data['name'] if 'name' in data else None
    title = data['title'] if 'title' in data else None
    bio = data['bio'] if 'bio' in data else None
    pfp = data['profile_picture'] if 'profile_picture' in data else None 
    update_profile(userId2,name,title,bio,pfp)
    return dumps({},default=str)


@app.route("/api/credentials/manage", methods=['POST'])
@cross_origin()
def update_credentials():
    data = request.get_json()
    if 'token' not in data or len(data) <= 1 or len(data) > 5 : raise InputError("Error invalid parameters")
    token = data['token']
    userId = str(token_to_id(token))
    if not is_valid_token(token) : raise AccessError("token is invalid")
    username = data['username'] if 'username' in data else None 
    email = data['email'] if 'email' in data else None 
    current_password = data['current_password'] if 'current_password' in data else None 
    new_password = data['new_password'] if 'new_password' in data else None
    update_user_credentials(userId, username, email,current_password, new_password)
    return dumps({},default=str)


@app.route("/api/<string:recipeId>/comments", methods=['GET'])
@cross_origin()
def list_comments(recipeId) -> json:
    """Returns a JSON List of comments for a given recipe

    Args:
        recipeId (uuid): URI for a given string

    Raises:
        InputException if recipe does NOT exist

    Returns:
        json: list of comments for a given recipe
    """
    comments_list = get_comments(recipeId)
    return dumps(comments_list,default=str)
    
    
@app.route("/api/<string:recipeId>/comment", methods=['POST','PUT','DELETE'])
@cross_origin()
def crud_comment(recipeId):
    """ This method is used for creating comments with ratings. Updating both comments 
    and ratings, as well was deleting comments with their respective rating. 

    Args:
        recipeId (uuid): The recipe identifier

    Raises:
        InputError: when a comment parameter is not provided. Note for comment deleting an empty double quote must be provided {"comment": ""} 
        AccessError: Invalid token

    Returns:
        json: {"Message:"Success}
    """
    data = request.get_json()
    if 'token' not in data or 'comment' not in data:
        raise InputError("Error invalid parameters")
    token = data['token']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    userId = str(token_to_id(token))
    comment = data['comment']
    rating = data['rating'] if 'rating' in data else None  
    photo = data['photo'] if 'photo' in data else None 
    commentId = data['commentId'] if 'commentId' in data else None 
    if request.method == 'POST': create_comment(userId,recipeId,comment,photo,rating)
    elif request.method == 'PUT': edit_comment(userId,commentId,comment,photo,rating)
    elif request.method == 'DELETE': delete_comment(userId,commentId)        
    return dumps({"Message":"Success"},default=str)
    

@app.route("/api/ratings", methods=['POST'])
@cross_origin()
def rate_comment_wrapper():
    """ This api method is used for rating comments left by users

    Raises:
        InputError: Incorrect request parameters
        AccessError: Token is expired or invalid

    Returns:
       json:empty dictionary
    """
    data = request.get_json()
    if 'token' not in data or 'commentId' not in data or 'rating' not in data:
        raise InputError("Error Invalid paramaters")
    token = data['token']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    userId = str(token_to_id(token))
    commentId = data['commentId']
    rating = data['rating']
    rate_comment(userId,commentId,rating)
    return dumps({},default=str)


@app.route("/api/recipe/create", methods=['POST'])
def create_recipe() -> json:
    """Used to create a new recipe

    Returns:
        json: {"id": id of newly created recipe}
    """
    data = request.get_json()
    token = data['token']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    current_user = get_current_user(data['token'])
    recipe = fill_recipe_fields(data, current_user)
    try:
        id = insert_recipe(recipe)
        # also need to update the published recipes of the user
        update_published_recipes_for_user(id, current_user)
        # then add to ingredients orm
        diff = find_differences_ingredients([], data['ingredients'])
        add_ingredients_to_recipe(diff.get('add'), diff.get('remove'), id)
    except Exception as e:
        InputError(e)
    return {"id": str(id)}


@app.route("/api/recipe/save", methods=['POST'])
def save_recipe() -> json:
    """Edit an existing recipe

    Raises:
        InputError: editing of recipe didn't work

    Returns:
        json: empty json
    """
    data = request.get_json()
    token = data['token']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user = token_to_id(token)
    recipe_id = data['id']
    try:
        old_ingredients = get_old_ingredients(recipe_id)
        diff = find_differences_ingredients(
            old_ingredients, data['ingredients'])
        add_ingredients_to_recipe(
            diff.get('add'), diff.get('remove'), UUID(recipe_id))
        recipe_id = edit_recipe(data)
        ## check curr_user is the author
        if not author_matches(recipe_id, curr_user):
            raise NotFoundError("User does not have permission to delete this recipe")
        return dumps({})
    except Exception as e:
        return InputError(e)


@app.route("/api/like", methods=['POST'])
@cross_origin()
def like() -> json:
    """POST request used to like someone's recipe

    Raises:
        AccessError: Current token is invalid

    Returns:
        json: Empty json
    """
    data = request.get_json()
    token = request.headers.get('token')
    recipe = data['recipeId']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    user = token_to_id(token)
    like_recipe(user, recipe)
    return dumps({})


@app.route("/api/unlike", methods=['POST'])
@cross_origin()
def unlike() -> json:
    """POST request used to unlike someone's recipe

    Raises:
        AccessError: Current token is invalid

    Returns:
        json: Empty json
    """
    data = request.get_json()
    token = request.headers.get('token')
    recipe = data['recipeId']
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    user = token_to_id(token)
    unlike_recipe(user, recipe)
    return dumps({})


@app.route("/api/userInfo", methods=['GET'])
@cross_origin()
def public_user_info() -> json:
    """GET request to retrieve a user's public information

    Raises:
        AccessError: Token is invalid

    Returns:
        json: user's public information
    """
    user = request.args.get('userId', type=int)
    token = request.headers.get('token')
    user_info = get_user_info(user)
    user_info['isSelf'] = False
    user_info['isSubscribed'] = False
    if not token:
        pass
    elif not is_valid_token(token):
        raise AccessError("token is invalid")
    else:
        curr_user = token_to_id(token)
        if curr_user == user:
            user_info['isSelf'] = True
        if curr_user in user_info['followerIds']:
            user_info['isSubscribed'] = True
    user_info.pop('followerIds')
    try:
        user_info['recipes'] = get_recipes_by_user(user)
    except:
        user_info['recipes'] = []
    user_info['likes'] = 0
    for recipe in user_info['recipes']:
        user_info['likes'] += recipe['likes']
    return dumps(user_info, default=str)


@app.route("/api/personalised_recipes", methods=['GET'])
@cross_origin()
def personalised_recipes() -> list[dict]:
    """Get a list of recipes which have been published by an author they have subscribed to

    Raises:
        AccessError: Token is invalid

    Returns:
        list[str]: list of recipes which have been published by an author they have subscribed to
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    user = token_to_id(token)
    return dumps(get_recipes_by_subscription(user), default=str)


@app.route("/api/user_details", methods=['GET'])
@cross_origin()
def user_info() -> json:
    """Get a specific user details

    Raises:
        AccessError: Token is invalid

    Returns:
        json: a user's private details
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    user = token_to_id(token)
    return dumps(get_user_info_by_id(user), default=str)


@app.route("/api/ingredients", methods=['GET'])
@cross_origin()
def get_ingredients() -> list[dict]:
    """Gets a list of ingredients from our database

    Returns:
        list[dict]: list of {ingredient: ingredient_name}
    """
    ingredients = list(IngredientsOrm.select(
        IngredientsOrm.ingredient).dicts())
    return ingredients


@app.route("/api/user_infos", methods=['GET'])
@cross_origin()
def get_all_users() -> list[dict]:
    """Get a list of all users' information

    Raises:
        AccessError: Token is invalid

    Returns:
        list[json]: Returns a list of jsons of all user's (public) information
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    return dumps(get_all_user_info(), default=str)


@app.route("/api/search", methods=['GET'])
@cross_origin()
def search():
    title = request.args.get('title')
    include = request.args.get('include')
    exclude = request.args.get('exclude')
    method = request.args.get('method')
    mealtypes = request.args.get('mealtypes')

    filters = []
    if title:
        filters.append('title')
    if method:
        filters.append('method')
    if include:
        filters.append('include')
        include = include.split(',')
    if exclude:
        filters.append('exclude')
        exclude = exclude.split(',')
    if mealtypes:
        filters.append('mealtypes')
        mealtypes = mealtypes.split(',')

    return dumps(search_recipes(filters, title, method, include, exclude, mealtypes), default=str)


@app.route("/api/pantry", methods=['POST', 'GET'])
@cross_origin()
def add_to_pantry() -> json:
    """Add/delete a list of ingredients to the pantry

    Raises:
        AccessError: If the token is invalid

    Returns:
        json: {"pantry": list of ingredients in the pantry}
    """

    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user_id = token_to_id(token)
    if request.method == 'POST':
        add = request.get_json()['add']
        delete = request.get_json()['delete']
        return add_list_to_pantry(add, delete, curr_user_id)
    else:
        return json.dumps(get_pantry(curr_user_id))


@app.route("/api/missing_ingredients", methods=['GET'])
@cross_origin()
def find_missing_ingredients() -> json:
    """Find ingredients that a user is missing from their pantry to make a list of recipes

    Raises:
        AccessError: Token is invalid

    Returns:
        json: {"ingredients": list of missing ingredients that a user will need to buy}
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user_id = token_to_id(token)
    meal_plan_list = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == curr_user_id).dicts().first()['mealPlans']
    pantry = get_pantry(curr_user_id).get('pantry')
    return json.dumps(find_the_missing_ingredients(meal_plan_list, pantry))


@app.route("/api/makeable_recipes", methods=['GET'])
@cross_origin()
def find_recipes_from_pantry_ingredients() -> json:
    """Find recipes that can be made based on the pantry ingredients

    Raises:
        AccessError: Token is invalid

    Returns:
        json: {"recipes": list of recipes that can be made}
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user_id = token_to_id(token)
    pantry = get_pantry(curr_user_id).get('pantry')
    recipes = find_recipes_based_on_pantry(pantry)
    return {"recipes": recipes}


@app.route("/api/meal_plan", methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def meal_plan():
    """Get meal plans / Add or delete recipe to meal plan

    Raises:
        AccessError: Token is invalid

    Returns:
        For GET:
            dict: {"mealPlans": list of recipe ids in meal plan}
        For POST:
            dict: {"added": boolean of whether the recipe was added}
        For DELETE:
            dict: {"removed": boolean of whether the recipe was deleted}
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user_id = token_to_id(token)
    if request.method == 'GET':
        return {"mealPlans": get_meal_plan(curr_user_id)}
    elif request.method == 'POST':
        recipe_id = UUID(request.get_json()['id'])
        return json.dumps({"added": add_meal_plan(recipe_id, curr_user_id)})
    else:
        recipe_id = UUID(request.get_json()['id'])
        return json.dumps({"removed": delete_meal_plan(recipe_id, curr_user_id)})

@app.route("/api/meal_plan/ingredients", methods=['GET'])
@cross_origin()
def get_ingredients_for_meal_plan() -> list[str]:
    """Get all ingredients needed to make the recipes inside the meal plan

    Raises:
        AccessError: Token is invalid
        InputError: Error retrieving meal plan/ getting ingredients

    Returns:
        list[str]: List of ingredients needed to make the recipes inside the meal plan
    """
    token = request.headers.get('token')
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    curr_user_id = token_to_id(token)
    try:
        meal_plans = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == curr_user_id).dicts().first()['mealPlans']
        return get_ingredients_meal_plan(meal_plans)
    except Exception:
        raise InputError("Error retrieving meal plan")

@app.route("/api/recommended_recipes", methods=['GET'])
@cross_origin()
def get_recommended_recipes() -> list[str]:
    recipe_id = request.args.get('recipeId')
    return dumps(recommended_recipes(recipe_id), default=str)
