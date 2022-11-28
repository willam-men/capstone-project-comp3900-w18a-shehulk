from datetime import datetime
import json
from uuid import UUID
from peewee import fn

from project.models.orm import RecipesOrm, UserOrm, IngredientsOrm
from project.models.schemas import Recipe, RecipeStatus, User
from project.error import AccessError, InputError, NotFoundError


def fill_recipe_fields(recipe: dict, current_user: User) -> Recipe:
    """Formats status, authorname, authorId and authorPfp fields in the recipe

    Args:
        recipe (dict): Recipe being updated
        current_user (dict): Details of current user logged in

    Returns:
        Recipe: Updated recipe with the reformatted fields
    """

    # At the moment, we only can have published recipes
    recipe["status"] = RecipeStatus.PUBLISHED.value
    recipe["authorName"] = current_user.name
    recipe["authorId"] = current_user.userId
    recipe["authorPfp"] = current_user.pfp
    return recipe


def insert_recipe(recipe: Recipe) -> UUID:
    """Insert recipe into database

    Args:
        recipe (Recipe): recipe to be inserted into database

    Raises:
        ValueError: If there is an error when inserting the recipe into the database

    Returns:
        UUID: Recipe id of the new recipe inserted
    """
    try:
        recipe_obj = RecipesOrm.create(status=recipe.get('status'), title=recipe.get('title'), description=recipe.get('description'),
                                       authorName=recipe.get('authorName'), authorId=recipe.get('authorId'), authorPfp=recipe.get('authorPfp'),
                                       servings=recipe.get('servings'), method=recipe.get('method'), mealType=recipe.get('mealType'),
                                       utensils=recipe.get('utensils'), dietaries=recipe.get('dietaries'), difficulty=recipe.get('difficulty'),
                                       cuisine=recipe.get('cuisine'), prepTime=recipe.get('prepTime'), cookTime=recipe.get('cookTime'),
                                       ingredients=recipe.get('ingredients'), photo=recipe.get('photo'), lastUpdated=datetime.now())
    except Exception:
        raise ValueError('Unable to insert recipe')
    return recipe_obj.id


def edit_recipe(recipe: Recipe) -> UUID:
    """Update recipe in database

    Args:
        recipe (Recipe): details of the recipe to be updated

    Raises:
        ValueError: If there is an error updating the recipe in the database

    Returns:
        UUID: Recipe id of the recipe updated
    """
    try:
        RecipesOrm.update(title=recipe.get('title'), description=recipe.get('description'), servings=recipe.get('servings'), method=recipe.get('method'), mealType=recipe.get('mealType'), utensils=recipe.get('utensils'), dietaries=recipe.get(
            'dietaries'), difficulty=recipe.get('difficulty'), cuisine=recipe.get('cuisine'), prepTime=recipe.get('prepTime'), cookTime=recipe.get('cookTime'), photo=recipe.get('photo'), ingredients=recipe.get('ingredients'), lastUpdated=datetime.now()).where(RecipesOrm.id == recipe.get('id')).execute()
    except Exception:
        raise ValueError('Unable to insert recipe')
    return recipe.get('id')


def delete_recipe(recipe_id: UUID) -> json:
    """Delete a recipe from the database

    Args:
        recipe_id (uuid): id of the recipe to be deleted

    Returns:
        json: Empty json
    """
    try:
        q = RecipesOrm.delete().where(RecipesOrm.id == recipe_id).execute()
    except Exception as e:
        return ValueError("There was an error when deleting the recipe")
    return json.dumps({})


def update_published_recipes_for_user(recipe_id: UUID, current_user: User) -> None:
    """Adda new published recipe in the user table

    Args:
        recipe_id (uuid): id of the recipe that is newly published
        current_user (User): details of the user logged in

    Raises:
        ValueError: If there was an error when updating the user profile with the newly published recipe
    """
    user_id = current_user.userId
    try:
        user_query = UserOrm.select(UserOrm.publishedRecipes).where(
            UserOrm.id == user_id).dicts().first()
        updated_user = user_query['publishedRecipes']
        updated_user.append(recipe_id)
        user_query = UserOrm.update(
            publishedRecipes=updated_user).where(UserOrm.id == user_id)
        user_query.execute()
    except Exception:
        raise ValueError('Unable to update user profile to publish recipe')
    return


def get_recipe(recipe_id: UUID) -> dict:
    """Get recipe with recipe_id given

    Args:
        recipe_id (uuid): recipe id of the recipe we are trying to find

    Raises:
        InputError: recipe does not exist in database

    Returns:
        dict: details of the recipe being found
    """
    try:
        UUID(recipe_id)
    except ValueError:
        raise NotFoundError("This recipe does not exist")
    recipe = RecipesOrm.select().where(RecipesOrm.id == recipe_id).dicts().first()
    if recipe is None:
        raise NotFoundError("This recipe does not exist")
    user_query = UserOrm.select(UserOrm.name, UserOrm.title, UserOrm.profilePic).where(
        UserOrm.id == recipe.get('authorId')).dicts().first()
    recipe['authorTitle'] = user_query['title']
    recipe['authorName'] = user_query['name']
    recipe['authorPfp'] = user_query['profilePic']
    if not recipe:
        raise NotFoundError("This recipe does not exist.")
    recipe['likes'] = len(recipe['likedList'])
    extraField = ['savedList', 'lastUpdated', 'status']
    for field in extraField:
        recipe.pop(field)
    return recipe


def get_recipes_by_page() -> list[dict]:
    """Get a list of all recipes in the database

    Raises:
        InputError: No recipes currently exist in the database

    Returns:
        list[dict]: list of all recipes in the database
    """
    recipes = list(RecipesOrm.select(RecipesOrm.id).order_by(-fn.cardinality(RecipesOrm.likedList), RecipesOrm.title).dicts())
    if not recipes:
        raise InputError("No recipes exist")
    return recipes


def like_recipe(user: int, recipe: UUID) -> None:
    """User likes a recipe

    Args:
        user (int): user id that is liking the recipe
        recipe (uuid): id of the recipe they are liking

    Raises:
        InputError: recipe does not exist/ has already been liked
    """
    recipe_query = RecipesOrm.select(RecipesOrm.likedList).where(
        RecipesOrm.id == recipe).dicts().first()
    if not recipe_query:
        raise InputError("Recipe does not exist")
    liked_list = recipe_query['likedList']
    if user in liked_list:
        raise InputError("Recipe has already been liked")
    liked_list.append(user)
    recipeOrm = RecipesOrm.update(
        likedList=liked_list).where(RecipesOrm.id == recipe)
    recipeOrm.execute()
    return


def unlike_recipe(user: int, recipe: UUID) -> None:
    """User unlikes a recipe

    Args:
        user (int): user id that is unliking the recipe
        recipe (uuid): id of the recipe they are unliking

    Raises:
        InputError: recipe does not exist/ has not previously been liked
    """
    recipe_query = RecipesOrm.select(RecipesOrm.likedList).where(
        RecipesOrm.id == recipe).dicts().first()
    if not recipe_query:
        raise InputError("Recipe does not exist")
    liked_list = recipe_query['likedList']
    if user not in liked_list:
        raise InputError("Recipe is not currently liked")
    liked_list.remove(user)
    recipeOrm = RecipesOrm.update(
        likedList=liked_list).where(RecipesOrm.id == recipe)
    recipeOrm.execute()
    return


def get_recipes_by_user(user: int) -> list[dict]:
    """Get recipes published by a user

    Args:
        user (int): id of user logged in

    Returns:
        list[dict]: list of all recipes that have been published by a user
    """
    recipe_query = list(RecipesOrm.select(RecipesOrm.id, RecipesOrm.likedList).where(
        RecipesOrm.authorId == user).order_by(RecipesOrm.lastUpdated).dicts())
    if not recipe_query:
        raise InputError("No recipes have been made")
    for recipe in recipe_query:
        recipe['likes'] = len(recipe['likedList'])
        recipe.pop('likedList')
    return recipe_query


def get_recipes_by_subscription(user: int) -> list[str]:
    """Get all recipes that a user has subscribed to the author

    Args:
        user (int): id of current user logged in

    Raises:
        InputError: current user logged in does not exist in the database

    Returns:
        list[str]: list of recipes which have been published by an author they have subscribed to
    """
    user_query = UserOrm.select(UserOrm.followingIds).where(
        UserOrm.id == user).dicts().first()
    if not user_query:
        raise InputError("This user does not exist")
    recipes = []
    for sub in user_query['followingIds']:
        sub_query = list(RecipesOrm.select(RecipesOrm.id, RecipesOrm.lastUpdated).where(
            RecipesOrm.authorId == sub).dicts())
        if not sub_query:
            continue
        recipes += sub_query
    sorted_recipes = sorted(recipes, key=lambda d: d['lastUpdated'])
    sorted_recipes.reverse()
    for recipe in sorted_recipes:
        recipe.pop('lastUpdated')
    return sorted_recipes


def search_recipes(filters: list[str], title: str, method: list[str], include: list[str], exclude: list[str], mealtypes: list[str]) -> list:
    """Find recipes that match the given search filters 

    Args:
        filters (list[str]): list of filters (title, method, include, exclude, mealtypes) that have been given for the search
        title (str): title of recipe to include in search
        method (list[str]): method of recipe to include in search
        include (list[str]): ingredients to include in search
        exclude (list[str]): ingredients to exclude in search
        mealtypes (list[str]): mealtypes to include in search

    Returns:
        list: list of recipe ids that meet the given search criteria
    """
    recipe_query = list(RecipesOrm.select(RecipesOrm.id, RecipesOrm.title, RecipesOrm.method, RecipesOrm.ingredients, RecipesOrm.mealType).dicts())
    recipes = []
    for recipe in recipe_query:
        should_insert = True
        for filter in filters:
            if filter == 'title':
                should_insert = should_insert and filter_title(recipe, title)
            if filter == 'method':
                should_insert = should_insert and filter_method(recipe, method)
            if filter == 'include':
                should_insert = should_insert and filter_include(
                    recipe, include)
            if filter == 'exclude':
                should_insert = should_insert and filter_exclude(
                    recipe, exclude)
            if filter == 'mealtypes':
                should_insert = should_insert and filter_mealtypes(
                    recipe, mealtypes)
        if should_insert:
            recipes.append({"id": recipe['id']})
    return recipes


def filter_title(recipe: dict, title: str) -> bool:
    """Returns whether the 'title' is part of a given recipe title

    Args:
        recipe (dict): recipe information
        title (str): title to match

    Returns:
        bool: whether the 'title' is part of a given recipe title
    """
    if title.lower() in recipe['title'].lower():
        return True
    return False


def filter_method(recipe: dict, method: list[str]) -> bool:
    """Returns whether the 'method' is part of a given recipe method

    Args:
        recipe (dict): recipe information
        title (str): method to match

    Returns:
        bool: whether the 'method' is part of a given recipe method
    """
    for step in recipe['method']:
        if method.lower() in step.lower():
            return True
    return False


def filter_include(recipe: dict, include: list[str]) -> bool:
    """Returns whether a recipe includes any of the ingredients from a given list

    Args:
        recipe (dict): recipe information
        include (list[str]): list of ingredients

    Returns:
        bool: whether a recipe includes any of the ingredients from a given list
    """
    ingredients = set(include)
    for ingredient in recipe['ingredients']:
        if ingredient['ingredient'] in ingredients:
            ingredients.discard(ingredient['ingredient'])
        if len(ingredients) == 0:
            return True
    return False


def filter_exclude(recipe: dict, exclude: list[str]) -> bool:
    """Returns whether a recipe excludes all of the ingredients from a given list

    Args:
        recipe (dict): recipe information
        include (list[str]): list of ingredients

    Returns:
        bool: whether a recipe excludes all of the ingredients from a given list
    """
    for ingredient in recipe['ingredients']:
        if ingredient['ingredient'] in exclude:
            return False
    return True


def filter_mealtypes(recipe: dict, mealtypes: list[str]) -> bool:
    """Returns whether a recipe is of one of the mealtypes given

    Args:
        recipe (dict): recipe information
        mealtypes (list[str]): list of mealtypes

    Returns:
        bool: whether a recipe is of one of the mealtypes given
    """
    if recipe['mealType'] in mealtypes:
        return True
    return False


def author_matches(recipe_id: UUID, curr_user_id: int) -> bool:
    """Works out whether current user matches the author of the recipe

    Args:
        recipe_id (UUID): id of recipe
        curr_user_id (int): id of current user logged in

    Returns:
        bool: whether current user matches the author of the recipe
    """
    author = RecipesOrm.select(RecipesOrm.authorId).where(RecipesOrm.id == recipe_id).dicts()
    if (author == curr_user_id):
        return True
    return False


def recommended_recipes(recipe_id: UUID) -> list:
    """Return a maximum of 9 recipes that are most similar to the given recipe

    Args:
        recipe_id (UUID): recipe id of given recipe

    Raises:
        NotFoundError: recipe does not exist

    Returns:
        list: list of recipe ids of recipes that are most similar to given recipe
    """
    recipe_query = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id == recipe_id).dicts().first()['ingredients']
    if not recipe_query:
        raise NotFoundError("This recipe does not exist")
    recipes = {}
    for num, ingredient in enumerate(recipe_query, start=2):
        recipes_query = IngredientsOrm.select(IngredientsOrm.recipes).where(IngredientsOrm.ingredient==ingredient['ingredient']).dicts().first()['recipes']
        if not recipes_query:
            continue
        for recipe in recipes_query:
            if recipe in recipes:
                recipes[recipe] += 1/num
            else:
                recipes[recipe] = 1/num
    recs = [{ "id": key } for (key, val) in sorted(recipes.items(), key=lambda d: -d[1])][1:10]
    return recs
