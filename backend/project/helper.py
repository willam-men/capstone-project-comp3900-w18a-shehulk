from json import loads
from urllib.request import urlopen

import pybase64
import random

## This file contains helper functions to convert code to sql for insert
def urlToRecipe(url):
    """
    Arguments:
        url of the form: https://www.kitchenstories.com/en/recipes/{recipe name}
        for example : https://www.kitchenstories.com/en/recipes/kung-pao-cauliflower
    Returns dictionary in the form:
    {
        "title" : string,
        "description" : string,
        "servings" : string,
        "difficulty" : string,
        "prepTime" : string,
        "cookTime" : string,
        "utensils" : {string},
        "ingredients" : 
            [{
                "ingredient" : string,
                "quantity" : string,
                "units" : string,
            }],
        "method" : {string},
        "cuisine" : {string},
        "dietaries" : {string}
        "mealType": string
    }
    
    """
    url = url.replace("www.kitchenstories.com/en", "web-bff.services.kitchenstories.io/api")
    url = url + "/"
    html = loads(urlopen(url).read())
    recipe = {}
    # Adds utensils to dictionary
    utensils = []
    for utensil in html["utensils"]:
        utensils.append(utensil['name']['rendered'].capitalize())
    recipe['utensils'] = str(utensils).replace("\'", "\"").replace("\'", "\"").replace('[', '{').replace(']', '}')

    unit = 'metric'
    if random.randint(0,9) % 2:
        unit = 'imperial'

    # Adds ingredients to dictionary
    ingredients = '['
    for ingredient in html["ingredients"][0]["list"]:
        currIngredient = {}
        amount = ''
        measurementUnit = ''
        ingredient_name = ingredient['name']['rendered']
        currIngredient['ingredient'] = ingredient_name

        if (ingredient_name.find("(") != -1):
            currIngredient['ingredient'] = ingredient_name.split('(')[0]
        
        if 'measurement' in ingredient:
            if unit in ingredient['measurement']:
                amount = ingredient['measurement'][unit]['amount']
                if 'unit' in ingredient['measurement'][unit]:
                    measurementUnit = ingredient['measurement'][unit]['unit']['name']['rendered']
        currIngredient['units'] = measurementUnit
        currIngredient['quantity'] = amount
        if ingredients != '[':
            ingredients += ', ' + str(currIngredient).replace("\'", "\"")
        else: 
            ingredients += str(currIngredient).replace("\'", "\"")
    
    recipe['ingredients'] = ingredients + ']'

    # adds fields to dictionary
    recipe['title'] = html['title']
    if (html.get('chefs_note') is not None):
        recipe['description'] = html['chefs_note']
    else:
        recipe['description'] = 'null'
    recipe['servings'] = html['servings']['amount']
    recipe['difficulty'] = html['difficulty'].capitalize()
    recipe['prepTime'] = str(html['duration']['preparation']) + " mins"
    recipe['cookTime'] = str(html['duration']['baking']) + " mins"

    # add cuisines, dietaries, and mealType fields to the dictionary
    cuisines = []
    dietaries = []
    mealType = ''
    for tag in html['tags']:
        if tag['type'] == 'meal' and (tag['title'] in ['dessert', 'breakfast']) and mealType == '':
            mealType = tag['title']
        if tag['type'] == 'cuisine':
            cuisines.append(tag['title'].capitalize())
        if tag['type'] == 'occasion' and 'dinner' in tag['title'] and mealType == '':
            meal = 'Dinner'
            if random.randint(0,9) % 2:
                meal = 'Lunch'
            mealType = meal
        if tag['type'] == 'diet':
            dietaries.append(tag['title'].capitalize())
    if cuisines != []:
        recipe['cuisine'] = str(cuisines).replace("\'", "\"").replace('[', '{').replace(']', '}')
    else:
        recipe['cuisine'] = '{}'
    if dietaries != []:
        recipe['dietaries'] = str(dietaries).replace("\'", "\"").replace('[', '{').replace(']', '}')
    else:
        recipe['dietaries'] = '{}'
    if mealType != '':
        recipe['mealType'] = mealType
    
    # Adds method to dictionary
    method = []
    for step in html["steps"]:
        method.append(step['text'])
    recipe['method'] = str(method).replace("\'", "\"").replace('[', '{').replace(']', '}')

    return recipe

def change_formatting(recipe: dict, author: dict) -> str:
    """
    Arguments:
        recipe: dict of form in urlToRecipe function
        author: dict in form {
            "userId": int,
            "name": str,
            "pfp": str
        }
    Returns a comma separated list of the recipe in the form to insert into sql
    
    """
    recipe_list = "'" + recipe['title'] + "'"
    to_append = [recipe.get('description'), author, recipe['servings'], recipe['ingredients'], recipe['method'], 
                recipe.get('mealType'), recipe['utensils'], recipe['dietaries'], recipe['difficulty'], recipe['cuisine'], recipe['prepTime'], recipe['cookTime']]
    for item in to_append:
        if item == 'null' or type(item) is int:
            recipe_list += ",\n" + str(item).replace("\'", "")
        else:
            recipe_list += ",\n" + "'" + str(item) + "'"

    return recipe_list

def add_brackets():
    ingredients = open("ingredients_after.txt", "r")
    data = ingredients.read()
    data_split = data.split(', ')
    data.close()
    index = 0
    for ingredient in data_split:
        ingredient_bracket = '(' + ingredient + ')'
        data_split[index]=ingredient_bracket
        index+=1

if __name__ == "__main__":
    add_brackets()
    author_list = [
        '[{"userId": 1, "name": "Test User 1", "pfp": null}]',
        '[{"userId": 2, "name": "Test User 2", "pfp": null}]',
        '[{"userId": 3, "name": "Test User 3", "pfp": null}]',
        '[{"userId": 4, "name": "Test User 4", "pfp": null}]',
        '[{"userId": 5, "name": "Test User 5", "pfp": null}]'
    ]

    urls = ["https://www.kitchenstories.com/en/recipes/braised-large-shrimp",
    "https://www.kitchenstories.com/en/recipes/steamed-pork-buns",
    "https://www.kitchenstories.com/en/recipes/sichuan-style-crispy-pork-belly",
    "https://www.kitchenstories.com/en/recipes/bbq-pork-ribs-in-the-oven-with-charred-corn-salad",
    "https://www.kitchenstories.com/en/recipes/glass-noodle-salad-with-lemongrass-dressing",
    "https://www.kitchenstories.com/en/recipes/watermelon-beet-salad-with-cherry-tomatoes"
    ]
    for url in urls:
        try:
            recipe = urlToRecipe(url)
            author = random.randint(0, 4)
            recipe_str = change_formatting(recipe, author_list[author])
        except Exception:
            pass
