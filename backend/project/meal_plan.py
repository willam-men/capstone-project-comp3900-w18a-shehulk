
from uuid import UUID
from project.models.orm import RecipesOrm
from project.error import InputError
from project.models.orm import UserOrm


def get_meal_plan(user_id: int) -> list[dict]:
    """Get meal plan for user

    Args:
        user_id (int): id of user

    Raises:
        InputError: Error when selecting meal plan for user

    Returns:
        list[dict]: list of recipes in meal plan in the form {id: recipeId (UUID)}
    """
    try:
        meal_plans = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == user_id).dicts().first()['mealPlans']
        meal_plan_list = []
        for meal_plan in meal_plans:
            meal_plan_list.append({"id": meal_plan})
    except Exception:
        raise InputError("Couldn't select meal plans")
    return meal_plan_list

def add_meal_plan(recipe_id: UUID, user_id: int) -> bool:
    """Add meal plan to a user

    Args:
        recipe_id (UUID): recipe being added to meal plan
        user_id (int): id of user

    Raises:
        InputError: If there is an error adding the recipe to the meal plan

    Returns:
        bool: Whether a recipe was added to the meal plan
    """
    try:
        meal_plan = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == user_id).dicts().first()['mealPlans']
        if (recipe_id in meal_plan):
            return False
        meal_plan.append(recipe_id)
        UserOrm.update(mealPlans=meal_plan).where(UserOrm.id ==user_id).execute()
    except Exception as e:
        raise InputError(e)
    return True

def delete_meal_plan(recipe_id: UUID, user_id: int) -> bool:
    """Delete meal plan to a user

    Args:
        recipe_id (UUID): recipe being deleted from meal plan
        user_id (int): id of user

    Raises:
        InputError: If there is an error deleting the recipe to the meal plan

    Returns:
        bool: Whether a recipe was deleted from the meal plan
    """
    try:
        meal_plans = UserOrm.select(UserOrm.mealPlans).where(UserOrm.id == user_id).dicts().first()['mealPlans']
        if (meal_plans.count(recipe_id) == 0):
            raise InputError(f"{recipe_id} was not in the meal plan previously")
        meal_plans.remove(recipe_id)
        UserOrm.update(mealPlans=meal_plans).where(UserOrm.id ==user_id).execute()
    except Exception:
        raise InputError(f"Couldn't remove {recipe_id} to the meal plan")
    return True

def get_ingredients_meal_plan(recipe_ids: list[UUID]) -> list[str]:
    """Get ingredients needed to make the recipes in the meal plan

    Args:
        recipe_ids (list[UUID]): list of recipes in meal plan

    Raises:
        InputError: If there is an error retrieving ingredients for the recipes in the meal plan
    
    Returns:
        list[str]: List of ingredients needed to make the recipes in the meal plan
    """
    try:
        ingredient_set = set([])
        for recipe_id in recipe_ids:
            ingredients = RecipesOrm.select(RecipesOrm.ingredients).where(RecipesOrm.id==recipe_id).dicts().first()['ingredients']
            for ing in ingredients:
                ingredient_set.add(ing['ingredient'])
        return list(ingredient_set)
    except Exception:
        raise InputError("Error retrieving ingredients for meal plan")
