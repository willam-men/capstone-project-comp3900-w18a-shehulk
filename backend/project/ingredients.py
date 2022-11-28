import json
from uuid import UUID

from project.error import InputError
from project.models.orm import IngredientsOrm, RecipesOrm


def find_differences_ingredients(ingredients_old: list[dict], ingredients_new: list[dict]) -> dict:
    """Find differences in list of ingredients

    Args:
        ingredients_old (list[dict]): List of ingredients in existing recipe
        ingredients_new (list[dict]): List of ingredients in updated recipe

    Returns:
        dict: {"remove": list of ingredients that have been removed, "add": list of ingredients that have been added}
    """
    ing_old = [old['ingredient'] for old in ingredients_old]
    ing_new = [new['ingredient'] for new in ingredients_new]
    remove = [ing for ing in ing_old if ing not in set(ing_new)]
    add = [ing for ing in ing_new if ing not in set(ing_old)]
    return {"remove": remove, "add": add}


def add_ingredients_to_recipe(ingredients_add: list[str], ingredients_remove: list[str], recipe_id: UUID) -> json:
    """Add recipe_id to ingredientsorm for the list of ingredients given

    Args:
        ingredients (list[str]): list of ingredients
        recipe_id (UUID): id of recipe

    Raises:
        InputError: Error in adding the recipe id to the ingredientsorm

    Returns:
        json: empty json if successful
    """
    for ingredient in ingredients_add:
        try:
            ingredient_dict = IngredientsOrm.select(IngredientsOrm.recipes).where(IngredientsOrm.ingredient == ingredient).dicts().first()
            recipe_list = ingredient_dict.get('recipes')
            recipe_list.append(recipe_id)
            IngredientsOrm.update(recipes=recipe_list).where(IngredientsOrm.ingredient == ingredient).execute()
        except Exception:
            raise InputError(f'Unable to add {recipe_id} to the ingredient: {ingredient}')
    for ingredient in ingredients_remove:
        try:
            ingredient_dict = IngredientsOrm.select(IngredientsOrm.recipes).where(IngredientsOrm.ingredient == ingredient).dicts().first()
            recipe_list = ingredient_dict.get('recipes')
            recipe_list.remove(recipe_id)
            IngredientsOrm.update(recipes=recipe_list).where(IngredientsOrm.ingredient == ingredient).execute()
        except Exception:
            raise InputError(f'Unable to remove {recipe_id} from the ingredient: {ingredient}')
    return json.dumps({})

def get_old_ingredients(recipe_id: UUID) -> list[dict]:
    """Get ingredients from recipe with recipe_id

    Args:
        recipe_id (UUID): id of recipe we are finding the ingredients of

    Returns:
        list[dict]: List of ingredients 
    """
    try:
        ingred_dict = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id==recipe_id).dicts().first()
    except Exception:
        raise InputError("Unable to find ingredients")
    return ingred_dict['ingredients']
