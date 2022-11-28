
import json
from collections import Counter
from uuid import UUID
from project.error import InputError
from project.models.orm import UserOrm, RecipesOrm, IngredientsOrm


def add_list_to_pantry(add: list[str], delete: list[str], user_id: int) -> json:
    """Add a list of ingredients to a user's pantry. Doesn't add ingredients if they are already in the list of ingredients

    Args:
        ingredients_list (list[str]): ingredient list to add to the pantry
        user_id (int): id of user who is updating their pantry

    Raises:
        InputError: Error in updating pantry 

    Returns:
        json: {"ingredients": list[str] of the consolidated ingredients in pantry}
    """
    try:
        existing_ingredients = UserOrm.select(UserOrm.pantry).where(UserOrm.id == user_id).dicts().first()
        pantry_list = existing_ingredients['pantry']
        ## add ingredients in 'add' list
        for ingredient in add:
            if ingredient not in pantry_list:
                pantry_list.append(ingredient)
        ## delete ingredients in 'delete' list
        for ingredient in delete:
            ## remove function throws an error if 'ingredient' doesn't exist
            pantry_list.remove(ingredient)
        UserOrm.update(pantry = pantry_list).where(UserOrm.id == user_id).execute()
    except Exception:
        raise InputError("Error when updating the pantry.")
    return json.dumps({"pantry": pantry_list})

def get_pantry(user_id: int) -> dict:
    """Get pantry of the current user logged in

    Args:
        user_id (int): id of user who is updating their pantry
    
    Raises:
        InputError: Error when getting the current user's pantry

    Returns:
        dict: {"pantry": list of ingredients in pantry}
    """
    try:
        existing_ingredients = UserOrm.select(UserOrm.pantry).where(UserOrm.id == user_id).dicts().first()
    except Exception:
        raise InputError("Error when getting pantry")
    return {"pantry": existing_ingredients['pantry']}

def find_the_missing_ingredients(recipe_ids: list[UUID], pantry: list[str]) -> json:
    """Find the missing ingredients

    Args:
        recipe_ids (list[UUID]): list of recipe ids
        pantry (list[str]): list of ingredients in pantry

    Raises:
        InputError: A recipe id does not exist

    Returns:
        json: {"ingredients": list of missing ingredients}
    """
    missing_ingredients = []
    for id in recipe_ids:
        try:
            ingredients = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id == id).dicts().first()
            for ingredient in ingredients['ingredients']:
                ingred_name = ingredient.get('ingredient')
                if ingred_name not in pantry and ingred_name not in missing_ingredients:
                    missing_ingredients.append(ingred_name)
        except Exception:
            raise InputError(f"A recipe with the id {id} does not exist")
    return {"ingredients": missing_ingredients}

def is_makeable(user_id: int, recipe_id: UUID) -> bool:
    """Works out whether a recipe is a makeable with a user's current pantry

    Args:
        user_id (int): id of user 
        recipe_id (UUID): id of recipe

    Returns:
        bool: Whether a recipe is makeable
    """
    pantry = get_pantry(user_id).get('pantry')
    try:
        ingredients = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id == recipe_id).dicts().first()
    except Exception:
        raise InputError(f"A recipe with the id {id} does not exist")
    for ingredient in ingredients['ingredients']:
        ingred_name = ingredient.get('ingredient')
        if ingred_name not in pantry:
            return False
    return True

def find_recipes_based_on_pantry(pantry: list[str]) -> json:
    """Find recipes based on ingredients in the pantry

    Args:
        pantry (list[str]): list of ingredients in a user's pantry

    Returns:
        json: Contains one key, "recipes", which stores a list of recipes in the following format: {
            recipe_id (uuid): number of missing ingredients
        }
    """
    recipes = []
    for ingredient in pantry:
        # find all recipe that uses that ingredient
        recipes_using_ing = IngredientsOrm.select(IngredientsOrm.recipes).where(IngredientsOrm.ingredient==ingredient).dicts().first()['recipes']
        recipes.extend(recipes_using_ing)
    summary = Counter(recipes)
    summary_dict = dict(summary)
    makeable_recipes = []
    ## work out how many ingredients are missing for each recipe
    for id in summary.keys():
        ing = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id == id).dicts().first()
        num_ing = len(ing['ingredients'])
        if ((num_ing - summary_dict.get(id)) == 0):
            makeable_recipes.append({"id": id})
    return makeable_recipes
