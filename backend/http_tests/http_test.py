import random
import requests
import time
from recipe_photo import recipe_pic
from pfp import pfp

asleep = 1
asleep2 = 1

###############################################################################
def test_generate_data():
    # Pytest being run for tests and not to generate data
    recipes = requests.get(f"http://localhost:5001/api/recipes")
    if recipes.status_code == 200:
        return

    # Makes users for test data
    user1 = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user1@gmail.com",
        "password" : "Password1!",
        "username" : "charlxtte",
        "name" : "Shallot Shan"
    }).json()['token']
    time.sleep(asleep)
    user2 = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user2@gmail.com",
        "password" : "Password1!",
        "username" : "Guzman",
        "name" : "Guzman Gomez"
    }).json()['token']
    time.sleep(asleep)
    user3 = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user3@gmail.com",
        "password" : "Password1!",
        "username" : "toughestcookinthekitchen",
        "name" : "Colette Tatou"
    }).json()['token']
    time.sleep(asleep)
    user4 = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user4@gmail.com",
        "password" : "Password1!",
        "username" : "Bob",
        "name" : "Bob"
    }).json()['token']
    time.sleep(asleep)
    user5 = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user5@gmail.com",
        "password" : "Password1!",
        "username" : "yummyyummy",
        "name" : "Happy Grillmore"
    }).json()['token']
    time.sleep(asleep)
    # Makes recipes for test data
    recipe1 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Garlic Broccolini",
        "description": "This is a Garlic Broccolini recipe", 
        "utensils": ["Garlic Press", "Large skillet"],
        "ingredients": 
        [
            {"quantity": "1", "units": "Bunches", "ingredient": "Broccolini", "extraInstructions":""}, 
            {"quantity": "2", "units": "cloves", "ingredient": "Garlic", "extraInstructions":""}, 
            {"quantity": "1/2", "units": "tsp", "ingredient": "Dijon mustard", "extraInstructions":""},
            {"quantity": "1/4", "units": "tsp", "ingredient": "Salt", "extraInstructions":""},
            {"quantity": "3/4", "units": "cup", "ingredient": "Olive oil", "extraInstructions":""}
        ],
        "servings": 2,
        "method": ["Rinse the Broccolini under cold water and shake off the excess water. Trim about 2cm off the bottom off the Broccolini stems.",
            "Heat the oil in a large straight skillet over medium-high heat until shimmering. Add the Broccolini and saute until the Broccolini is bright green and some of the stems and tips of the florets are lightly charred, 5 to 7 minutes.",
            "Press the garlic in a garlic press, and add the salt. Continue to saute for about 30 seconds. Add the water, cover and cook until the Broccolini is a vibrant green (1-2 minutes). Serve immediately."],
        "difficulty": "Easy",
        "mealType": "Side",
        "cuisine": ["Greek"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['broccolini'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 20 mins"
    }).json()['id']
    
    recipe2 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Potato Fries",
        "description": "This is a potato fries recipe", 
        "utensils": ["Wok", "Large bowl"],
        "ingredients": 
        [
            {"quantity": "6", "units": "", "ingredient": "Potatoes", "extraInstructions":"peeled"}, 
			{"quantity": "", "units": "", "ingredient": "Oil", "extraInstructions":""}, 
			{"quantity": "1/2", "units": "tsp", "ingredient": "Sea salt", "extraInstructions":""},
			{"quantity": "1/4", "units": "tsp", "ingredient": "Cracked black pepper", "extraInstructions":""}
		],
        "servings": 2,
        "method": 
        [
            "Cut potatos into 4mm thick slices. Layer between sheets of paper towel to remove excess moisture. Stand for 10 minutes",
		    "Heat oil in a wok or large deep frying pan over medium-high heat. Deep-fry potato in batches until potato rises to the surface and turns opaque. Using a slotted spoon, transfer fries to a tray lined with paper towel. Cool for 10 minutes.",
		    "Transfer to a bowl and add salt and pepper. Toss to coat."
        ],
        "difficulty": "Easy",
        "mealType": "Side",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['chips'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 10 mins"
    }).json()['id']
    
    recipe3 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user3,
        "title" : "Garlic Mayonaise",
        "description": "This is a Garlic Mayonaise recipe", 
        "utensils": ["Hand immersion blender"],
        "ingredients": 
        [
            {"quantity": "1", "units": "", "ingredient": "Egg", "extraInstructions":"room temperature"}, 
            {"quantity": "1", "units": "clove", "ingredient": "Garlic", "extraInstructions":"peeled"}, 
            {"quantity": "1/2", "units": "tsp", "ingredient": "Dijon mustard", "extraInstructions":""},
            {"quantity": "1/4", "units": "tsp", "ingredient": "Salt", "extraInstructions":""},
            {"quantity": "3/4", "units": "cup", "ingredient": "Olive oil", "extraInstructions":""}
        ],
        "servings": 8,
        "method": 
        [
            "Combine egg, garlic, lemon juice, Dijon mustard, salt and pepper in a bow. Whisk with a fork until well combined. Using a hand immension blender, slowly add olive oil in a small stream and blend until creamy"
        ],
        "difficulty": "Easy",
        "mealType": "Side",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['garlic_mayo'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 10 mins"
    }).json()['id']
    
    recipe4 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "One-pot pasta",
        "description": "This is a One-pot pasta recipe", 
        "utensils": ["Cutting board", "Knife", "Cooking spoon", "Frying pan (deep)", "Fine grater"],
        "ingredients": 
        [
            {"ingredient": "Spaghetti", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Baby spinach", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Cherry tomatoes", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Vegetable broth", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Onion", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Thyme", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Basil", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Parmesan cheese", "units": "", "quantity": "", "extraInstructions": "grated"}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "", "quantity": "", "extraInstructions": "for frying"}, 
            {"ingredient": "Basil", "units": "", "quantity": "", "extraInstructions": "for serving"}
        ],
        "servings": 2,
        "method": 
        [
            "Clean spinach. Cut onion into thin strips, finely chop garlic, and halve cherry tomatoes.", 
            "Then, heat some olive oil in a deep pan. Saute garlic and onion for approx. 3 û 5 min. until fragrant and translucent.", 
            "Now, add pasta, baby spinach, cherry tomatoes, thyme, and basil to the pan and pour in the vegetable stock. Stirring occasionally, simmer for approx. 10 û 12 min. until the liquid has reduced.", 
            "Season generously with salt and pepper. Serve sprinkled with basil and freshly grated Parmesan."
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Italian"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['one_pot'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe5 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "Pasta with bacon cream sauce",
        "description": "This is a Pasta with bacon cream sauce recipe", 
        "utensils": ["Colander", "Large pot", "Cutting board", "Knife", "Large frying pan", "Cooking spoon"],
        "ingredients": 
        [
            {"ingredient": "Spaghetti", "units": "oz", "quantity": 9.0, "extraInstructions": ""}, 
            {"ingredient": "Mushrooms", "units": "oz", "quantity": 1.75, "extraInstructions": ""}, 
            {"ingredient": "Onion", "units": "", "quantity": "", "extraInstructions": "small"}, 
            {"ingredient": "Smoked bacon", "units": "oz", "quantity": 2.5, "extraInstructions": ""}, 
            {"ingredient": "Heavy cream", "units": "cups", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Chicken stock", "units": "cups", "quantity": 0.25, "extraInstructions": ""}, 
            {"ingredient": "Parmesan", "units": "oz", "quantity": 2.25, "extraInstructions": "grated"}, 
            {"ingredient": "Vegetable oil for frying", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Cook the spaghetti, according to package instructions, in salted boiling water for approx. 9 - 12 min. until al dente. Drain the water and set pasta aside.", 
            "Cut mushrooms into thin slices. Finely dice onion and bacon.", 
            "SautΘ bacon in a large frying pan with some vegetable oil. Add onion and mushrooms and continue to sautΘ.", 
            "Add cream and chicken stock and cook over medium-low heat for approx. 2 - 3 min.", 
            "Toss spaghetti in the sauce. Add Parmesan, toss again, and season with salt and pepper to taste before serving."
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Italian"],
        "dietaries": [],
        "photo": recipe_pic['creamy_bacon'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe6 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Vietnamese-inspired summer rolls",
        "description": "This is a Vietnamese-inspired summer rolls recipe", 
        "utensils": ["Spiral slicer", "Cutting board", "Knife", "Tongs", "2 frying pans", "Bowl"],
        "ingredients": 
        [
            {"ingredient": "Carrot", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Thai basil", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Cilantro", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Mint", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Tofu", "units": "g", "quantity": 200.0, "extraInstructions": ""}, 
            {"ingredient": "Bell pepper", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Green onions", "units": "", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Lettuce", "units": "", "quantity": 0.5, "extraInstructions": "e.g., iceberg, romaine"}, 
            {"ingredient": "Peanuts", "units": "g", "quantity": 60.0, "extraInstructions": ""}, 
            {"ingredient": "Rice wrappers", "units": "", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Sesame seeds", "units": "g", "quantity": 60.0, "extraInstructions": ""}, 
            {"ingredient": "Peanut sauce", "units": "ml", "quantity": 200.0, "extraInstructions": "satay sauce"}, 
            {"ingredient": "Vegetable oil for frying", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 5,
        "method": 
        [
            "Using a spiral slicer, cut carrot into thin strips.", 
            "Roughly chop Thai basil, cilantro, and mint. Cut tofu into thin rectangles. Cut pepper, onions, and lettuce into strips.", 
            "Using a grease-free pan, toast nuts over medium-low heat for approx. 3 û 5  min. until fragrant. In a frying pan, sautΘ tofu in some vegetable oil over medium-high heat for approx. 2 û 3 min. per side or until golden brown. Season with salt and pepper.", 
            "Dip rice wrappers evenly into water and allow to soak for approx. 1 min. \r\nGently shake to remove excess water. Set aside on a plate or cutting board.", 
            "In the middle of the rice wrapper, layer tofu, carrot, pepper, peanuts, sesame seeds, green onions, and chopped herbs. Finish off with a dollop of peanut sauce.", 
            "In the same way you wrap a tortilla, fold the edges of the rice wrapper towards the center, bring forward the bottom, and roll forward with your thumbs until the roll is tight. Garnish the roll with sesame seeds and serve with a dipping sauce of your choice. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Vietnamese", "Asian"],
        "dietaries": ["Vegetarian", "Vegan", "Gluten free"],
        "photo": recipe_pic['vietnamese_rolls'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe7 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Rainbow summer rolls",
        "description": "This is a Rainbow summer rolls recipe", 
        "utensils": ["Citrus press", "Cutting board", "Knife", "Small bowl", "Large bowl"],
        "ingredients": 
        [
            {"ingredient": "Ginger", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Chili", "units": "g", "quantity": 5.0, "extraInstructions": ""}, 
            {"ingredient": "Rice vinegar", "units": "tbsp", "quantity": 4.0, "extraInstructions": ""}, 
            {"ingredient": "Soy sauce", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sesame oil", "units": "tbsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Agave syrup", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Lime", "units": "", "quantity": 1.0, "extraInstructions": "juice"}, 
            {"ingredient": "Sesame seeds", "units": "tsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Carrots", "units": "", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Cucumber", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Red cabbage", "units": "g", "quantity": 200.0, "extraInstructions": ""}, 
            {"ingredient": "Mango", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Radishes", "units": "", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Avocado", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Cress", "units": "g", "quantity": 50.0, "extraInstructions": ""}, 
            {"ingredient": "Rice paper", "units": "sheets", "quantity": 7.0, "extraInstructions": "22 cm/8.5 in"}, 
            {"ingredient": "Water", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 7,
        "method": 
        [
            "Finely chop the ginger and chill. Mix with the rice vinegar, soy sauce, water, sesame oil, agave syrup, lime juice, and sesame seeds in a bowl. Set aside.", 
            "Peel and slice the carrots, and chop the cucumber and red cabbage into fine matchsticks. Finely slice mango, radish and avocado. Cut the cress.", 
            "Add some water to a deep bowl. Wet the rice paper with water and lay flat on a clean work surface. Assemble all ingredients except the sauce on the rice paper. Fold one side of the rice paper over the filling, then fold in the sides. Roll into a log, ensuring the sides are sealed tightly. Repeat with remaining rice paper and serve with sauce. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Vietnamese", "Asian"],
        "dietaries": ["Vegetarian", "Vegan", "Gluten free"],
        "photo": recipe_pic['summer_rolls'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe8 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user3,
        "title" : "Easy Italian lasagna",
        "description": "This is a Easy Italian lasagna recipe", 
        "utensils": ["Cutting board", "Knife", "Peeler", "Pot", "Cooking spoon", "Oven", "Saucepan (small)", "Whisk", "Baking dish", "Ladle", "Grater"],
        "ingredients": 
        [
            {"ingredient": "Garlic", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Onion", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Carrots", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Ground beef", "units": "lb", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Canned crushed tomatoes", "units": "oz", "quantity": 28.0, "extraInstructions": ""}, 
            {"ingredient": "Dried oregano", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Unsalted butter", "units": "stick", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Flour", "units": "cup", "quantity": 0.33, "extraInstructions": ""}, 
            {"ingredient": "Milk", "units": "cups", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Ground nutmeg", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Lasagna noodles", "units": "oz", "quantity": 6.0, "extraInstructions": ""}, 
            {"ingredient": "Parmesan cheese", "units": "oz", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 6,
        "method": 
        [
            "Finely chop garlic. Peel and dice onion and carrots.", 
            "Heat some olive oil in a large pot and sautΘ onions, carrots, and garlic. Add ground beef to brown, breaking it up with a cooking spoon. Season with salt and pepper.", 
            "Now, add crushed tomatoes and season again with salt and pepper. Simmer covered over medium heat for approx. 15 - 20 min. Stir in dried oregano.", 
            "Meanwhile, preheat oven to 200░C/390░F. For the bΘchamel sauce, melt butter in a small sauce pan. Add flour and sautΘ, stirring constantly to form a roux.", 
            "Add cold milk in portions and reduce over medium heat, stirring occasionally, for approx. 5 û 8 min. Season with nutmeg and salt and pepper.", 
            "Cover bottom of baking dish with a layer of meat sauce. Top with lasagna sheets and bΘchamel sauce. Repeat procedure until ingredients are used up. Finish off with bΘchamel sauce.", 
            "Top with freshly grated Parmesan and bake in preheated oven at 200░C/390░F for approx. 30 û 40 min. on the middle rack until golden. Serve hot in baking dish."
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["Italian", "European"],
        "dietaries": [],
        "photo": recipe_pic['lasagna'],
        "prepTime": "0 hours 40 mins",
        "cookTime": "0 hours 30 mins"
    }).json()['id']
    
    recipe9 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "Gnocchi with peas and Parmesan",
        "description": "This is a Gnocchi with peas and Parmesan recipe", 
        "utensils": ["Fine grater", "Citrus press", "Cutting board", "Knife", "Frying pan", "Potato masher", "Large bowl"],
        "ingredients": 
        [
            {"ingredient": "Gnocchi", "units": "g", "quantity": 500.0, "extraInstructions": ""}, 
            {"ingredient": "Frozen peas", "units": "g", "quantity": 250.0, "extraInstructions": ""}, 
            {"ingredient": "Parmesan cheese", "units": "g", "quantity": 100.0, "extraInstructions": "grated and divided"}, 
            {"ingredient": "Garlic", "units": "cloves", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Lemon", "units": "", "quantity": 0.5, "extraInstructions": "zest and juice"}, 
            {"ingredient": "Mint", "units": "g", "quantity": 5.0, "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Butter", "units": "tbsp", "quantity": 2.0, "extraInstructions": "divided"}, 
            {"ingredient": "Chicken broth", "units": "ml", "quantity": 200.0, "extraInstructions": ""}, 
            {"ingredient": "Red chili flakes", "units": "tsp", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Finely chop garlic and chiffonade mint leaves. Zest lemon and squeeze the juice.", 
            "Heat olive oil and half of the butter in a frying pan over medium-high heat and fry the gnocchi until crispy, approx. 5 min.", 
            "In a large bowl, defrost peas in boiling water for approx. 2 min., then drain and roughly mash with a potato masher.", 
            "Add chopped garlic to gnocchi in the frying pan and sautΘ for approx. 2 min. Add the chicken broth and the mashed peas, mix well, and leave to simmer for approx. 3 min.", 
            "Add some of the Parmesan to the pan, stir, and reduce the heat. Add remaining butter, lemon juice, and lemon zest, and adjust seasoning with salt, pepper, and red chili flakes. Sprinkle with fresh mint and serve with the remaining Parmesan. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Italian"],
        "dietaries": [],
        "photo": recipe_pic['pea_gnocchi'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe10 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "Easy tomato tart",
        "description": "This is a Easy tomato tart recipe", 
        "utensils": ["Oven", "Fine grater", "Mandoline", "Cutting board", "Knife", "Baking dish", "Bowl (small)", "Baking sheet", "Parchment paper", "Paper towels"],
        "ingredients": 
        [
            {"ingredient": "Puff pastry sheet", "units": "sheet", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Mixed tomatoes", "units": "g", "quantity": 450.0, "extraInstructions": ""}, 
            {"ingredient": "Grainy mustard", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "clove", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "CrΦme fraεche", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Thyme", "units": "sprigs", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 4,
        "method": 
        [
            "Preheat the oven to 200C/400F. Finely chop or grate the garlic. Slice larger tomatoes very thinly using a vegetable slicer, if you have one. Cut cherry tomatoes in half. Place in a baking dish, salt, and let stand for about 10 min to release some of the liquid.", 
            "Mix mustard, crΦme fraεche, and garlic in a small bowl. If necessary, line a baking tray with baking paper, then roll out the puff pastry on it. Poke a few holes in the center of the dough with a fork. Spread on the mustard mixture in a thin layer. Dab the tomatoes with kitchen paper and spread them out on the pastry. Leave a margin of about 1 cm.", 
            "Drizzle with olive oil. Season with pepper and a little sugar. Pluck the thyme from the stems and sprinkle on the tart. Fold the edges of the puff pastry and press lightly at the corners. Place in the preheated oven and bake for about 20-25 minutes at 200░C/400║F until the edges are golden brown. Remove from oven, slice, and enjoy warm or at room temperature. Garnish with more fresh thyme if desired. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["French", "European"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['tomato_tart'],
        "prepTime": "0 hours 10 mins",
        "cookTime": "0 hours 20 mins"
    }).json()['id']
    
    recipe11 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Make classic tiramisu",
        "description": "For this recipe I used strong and freshly brewed espresso, not the instant powder. It makes a difference, trust me. Make sure to not soak the ladyfingers, but just quickly dunk them in the Amaretto-espresso mixture. That way they will stay soft and melt together with the rich cream, but won''t be mushy. If Amaretto isn''t your favorite, you can leave it outùI personally prefer my tiramisu without it. Please note that we have updated the images, condensed the steps, and added a new video to this recipe. However, the original recipe remains unchanged.", 
        "utensils": ["Bowl (large)", "Hand mixer with beaters", "Rubber spatula", "Baking dish", "Fine grater", "Fine sieve"],
        "ingredients": 
        [
            {"ingredient": "Mascarpone cheese", "units": "cup", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Ladyfingers", "units": "oz", "quantity": 8.0, "extraInstructions": ""}, 
            {"ingredient": "Eggs", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "ConfectionerÆs sugar", "units": "cup", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Espresso", "units": "cup", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Amaretto", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Bittersweet chocolate", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Unsweetened cocoa powder", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 6,
        "method": 
        [
            "Separate eggs. Beat egg yolks with some confectionerÆs sugar until pale and fluffy. Add Amaretto and mascarpone. Beat until smooth.", 
            "Beat egg whites with a pinch of salt until stiff peaks form. Slowly whisk in the remaining confectionerÆs sugar. Carefully fold beaten egg whites into mascarpone cream.", 
            "Combine espresso and remaining Amaretto in a shallow dish. Quickly dip ladyfingers in espresso mixture and then layer soaked ladyfingers in bottom of the serving dish. Cover with a layer of mascarpone cream and top with a fine layer of grated chocolate.", 
            "Repeat layering process until all ingredients are used up. Finish up with a layer of mascarpone cream, finely grated chocolate, and a dusting of unsweetened cocoa powder. Refrigerate for at least 3 hours before serving. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Dessert",
        "cuisine": ["Italian"],
        "dietaries": ["Vegetarian", "No Nuts"],
        "photo": recipe_pic['tiramisu'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe12 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Apple Marzipan Cake",
        "description": "This apple cake tastes best with fresh apples from the garden or farmer''s market. To dial up the marizpan flavor, you can also add an extra 100g / 3.5 oz between the cake batter and the apple layer before it goes in the oven. Delicious!", 
        "utensils": ["Oven", "Paring knife", "Baking pan", "2 bowls (large)", "1 hand mixer with beaters", "Fine sieve"],
        "ingredients": 
        [
            {"ingredient": "Apples", "units": "", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Marzipan", "units": "g", "quantity": 180.0, "extraInstructions": ""}, 
            {"ingredient": "Lemon juice", "units": "tbsp", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Unsalted butter", "units": "g", "quantity": 200.0, "extraInstructions": ""}, 
            {"ingredient": "Raw sugar", "units": "g", "quantity": 80.0, "extraInstructions": ""}, 
            {"ingredient": "Vanilla sugar", "units": "tbsp", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Ground cinnamon", "units": "tsp", "quantity": 1.5, "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "tsp", "quantity": 0.33, "extraInstructions": ""}, 
            {"ingredient": "Whole milk", "units": "ml", "quantity": 50.0, "extraInstructions": ""}, 
            {"ingredient": "Amaretto", "units": "ml", "quantity": 70.0, "extraInstructions": ""}, 
            {"ingredient": "Eggs", "units": "", "quantity": 4.0, "extraInstructions": ""}, 
            {"ingredient": "Flour", "units": "g", "quantity": 250.0, "extraInstructions": ""}, 
            {"ingredient": "Baking powder", "units": "tsp", "quantity": 2.5, "extraInstructions": ""}, 
            {"ingredient": "Heavy cream", "units": "ml", "quantity": 200.0, "extraInstructions": ""}, 
            {"ingredient": "Sliced almonds", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Unsalted butter", "units": "", "quantity": "", "extraInstructions": "for greasing"}, 
            {"ingredient": "Flour", "units": "", "quantity": "", "extraInstructions": "for greasing"}
        ],
        "servings": 8,
        "method": 
        [
            "Preheat the oven to 175░C/345░F. Wash and quarter the apples, remove the cores and sprinkle them with lemon juice. Set aside. Grease and flour the baking pan.", 
            "In a large bowl, beat the butter with cane sugar, half of the vanilla sugar, cinnamon and salt until frothy. Crumble in the marzipan and beat until combined. Crack in the eggs, one by one, and mix well between each addition. Stir in the milk and amaretto at low speed and then add the flour and baking powder. Mix slowly into a smooth batter.", 
            "Pour batter into the baking pan. Arrange the apples in concentric circles on top of the batter. Scatter some sliced almonds on top. Bake at 175░C/345░F for approx. 1 hr. Remove and let cool. In a bowl, whip the heavy cream and the remaining vanilla sugar until stiff. Dust the cake with powdered sugar and serve with the vanilla cream. Enjoy!"
        ],
        "difficulty": "Medium",
        "mealType": "Dessert",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['apple_marzipan'],
        "prepTime": "0 hours 35 mins",
        "cookTime": "0 hours 60 mins"
    }).json()['id']
    
    recipe13 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user3,
        "title" : "Russian salad",
        "description": "This is a Russian salad recipe", 
        "utensils": ["Skimmer", "Saucepan", "Cutting board", "Knife", "Bowl", "Whisk", "Citrus press", "Cooking spoon"],
        "ingredients": 
        [
            {"ingredient": "Eggs", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pickled herring", "units": "oz", "quantity": 9.0, "extraInstructions": ""}, 
            {"ingredient": "Ham", "units": "oz", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Chicken", "units": "oz", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Sausage", "units": "", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Gherkins", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Chives", "units": "tbsp", "quantity": 5.0, "extraInstructions": ""}, 
            {"ingredient": "Potatoes", "units": "", "quantity": "", "extraInstructions": "medium-sized"}, 
            {"ingredient": "Carrots", "units": "", "quantity": "", "extraInstructions": "medium-sized"}, 
            {"ingredient": "Peas", "units": "cups", "quantity": 1.0, "extraInstructions": "frozen"}, 
            {"ingredient": "Mustard", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Vegetable oil", "units": "cups", "quantity": 1.25, "extraInstructions": ""}, 
            {"ingredient": "Lemon", "units": "", "quantity": "", "extraInstructions": "zest and juice"}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Ice", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 8,
        "method": 
        [
            "Add two thirds of the eggs to a saucepan and cover with cold water. Bring to a boil and allow to cook for 7 û 8 min. Remove from saucepan and immediately transfer to an ice bath or rinse with cold water. Peel when cool enough to handle.", 
            "Slice eggs. Dice pickled herring, cooked meat, and gherkins. Finely chop chives. Peel potatoes and carrot and cut into small cubes.", 
            "Add carrot cubes to a saucepan with lightly salted boiling water and blanch for approx. 3 û 4 min. Remove from water and immediately transfer to an ice bath.", 
            "Then, add peas to boiling water and blanch for approx. 2 û 3 min. Transfer to ice bath and allow to cool for approx. 3 û 5 min. Remove carrots and peas from ice bath and set aside.", 
            "In another saucepan, bring lightly salted water to a boil. Add potato cubes and continue to cook for approx. 10 û 13 min. until cooked through. Then remove from water and set aside.", 
            "Separate remaining eggs and add egg yolk to a bowl. Add mustard and whisk to combine.", 
            "In a steady stream, add vegetable oil to egg yolks while stirring constantly. Whisk until fully incorporated. Then, season to taste with salt, pepper, and lemon juice.", 
            "Add potatoes, carrots, peas, gherkins, eggs, cooked meat, pickled herring, and chives to a large bowl. Add mayonnaise and season to taste with salt, pepper, and zest and juice of remaining lemon. Mix carefully to combine all ingredients."
        ],
        "difficulty": "Hard",
        "mealType": "Main",
        "cuisine": ["Eastern-Europe"],
        "dietaries": ["Gluten Free", "Dairy Free"],
        "photo": recipe_pic['russian_salad'],
        "prepTime": "0 hours 90 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe14 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "Kid approved pasta salad",
        "description": "This is a Kid approved pasta salad recipe", 
        "utensils": ["Cutting board", "Knife", "Large saucepan", "Cooking spoon", "Small bowl", "Large bowl"],
        "ingredients": 
        [
            {"ingredient": "Bell pepper", "units": "", "quantity": "", "extraInstructions": "red"}, 
            {"ingredient": "Vienna sausages", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Tomatoes", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Chives", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Green onion", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pasta", "units": "cups", "quantity": 2.0, "extraInstructions": "e.g., farfalle, fusili, etc"}, 
            {"ingredient": "Mustard", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Broth", "units": "cup", "quantity": 0.5, "extraInstructions": "e.g., vegetable, chicken"}, 
            {"ingredient": "White balsamic vinegar", "units": "tbsp", "quantity": 1.5, "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 6,
        "method": 
        [
            "Cut bell pepper into strips. Cut sausages into bite-sized pieces. Dice tomatoes. Roughly chop chives. Thinly slice green onions.", 
            "In a large saucepan, cook pasta in salted boiling water, according to package instructions, for approx. 8 û 10 min. Drain and set aside.", 
            "For the dressing, mix together mustard, broth, vinegar, chopped chives, salt, and pepper in a small bowl.", 
            "In a large bowl, mix together cooked pasta, cut peppers, chopped green onions, tomatoes, sausages, and dressing. Season once more with salt and pepper. Stir until well combined and allow to sit for approx. 20 min. before serving. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Italian", "American"],
        "dietaries": [],
        "photo": recipe_pic['easy_pasta'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe15 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "Mediterranean pasta with pimientos",
        "description": "This is a Mediterranean pasta with pimientos recipe", 
        "utensils": ["Large sauce pan", "Colander", "Cutting board", "Knife", "Large frying pan", "Cooking spoon"],
        "ingredients": 
        [
            {"ingredient": "Pasta", "units": "cups", "quantity": 3.33, "extraInstructions": "e.g. orecchiette"}, 
            {"ingredient": "Peppers", "units": "lb", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Zucchini", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Carrot", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Dried tomatoes in oil", "units": "cup", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Pureed tomatoes", "units": "fl oz", "quantity": 13.5, "extraInstructions": ""}, 
            {"ingredient": "Red onion", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Chili pepper", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Rosemary", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Thyme", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Vegetable oil for frying", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Cook pasta according to the package instructions in salted, boiling water until al dente. Drain and set to one side.", 
            "Meanwhile, remove the seeds from the chili pepper and chop finely. Finely dice zucchini, carrot, onion, garlic and dried tomatoes.", 
            "Finely chop rosemary and thyme.", "Fry vegetables in some vegetable oil and season with sugar, salt and pepper. Pour in pureed tomatoes, chopped herbs, and chili. Saute for approx. 5 - 10 min. until sauce has thickened.", 
            "In a second pan, fry Padr≤n peppers in some vegetable oil and add plenty of salt. Toss the noodles in the sauce and serve in a deep dish with the fried Padr≤n peppers on top."
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["Spanish"],
        "dietaries": ["Vegetarian", "Vegan"],
        "photo": recipe_pic['mediteranean'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe16 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Cauliflower steak",
        "description": "This is a Cauliflower steak recipe", 
        "utensils": ["Citrus zester", "Oven", "Cutting board", "Knife", "Citrus juicer", "Hand blender", "Small saucepan", "Cooking spoon", "Spatula", "Large ovenproof frying pan"],
        "ingredients": 
        [
            {"ingredient": "Cauliflower", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Rice milk", "units": "ml", "quantity": 150.0, "extraInstructions": ""}, 
            {"ingredient": "Tangerines", "units": "", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sage", "units": "leaves", "quantity": 6.0, "extraInstructions": ""}, 
            {"ingredient": "Cloves", "units": "", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Anise seeds", "units": "tbsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "tbsp", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Vegetable oil for frying", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Preheat oven to 180C/350F. Zest half the tangerines. Finely slice sage. Remove leaves from cauliflower and cut two thumb-thick steaks from the middle and set aside. Roughly chop remaining cauliflower.", 
            "Juice all the tangerines and add reserved zest to juice.", "Add chopped cauliflower, rice milk, and cloves to a small saucepan. Salt to taste. Cook for approx. 15 min. until cauliflower is soft. Remove cloves and puree until smooth with a hand blender. Stir in olive oil and keep warm.", 
            "In the meantime, heat some vegetable oil in a large ovenproof frying pan. Fry cauliflower steaks over medium heat for approx. 4 - 6 min. on each side until nicely browned. Sprinkle with sage and anise.", 
            "Transfer cauliflower steaks to preheated oven and bake at 180░C/350░F for approx. 15 û 20 min.", 
            "Serve cauliflower steaks on a bed of cauliflower puree. Drizzle tangerine juice over cauliflower steaks. Salt to taste and enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian", "Vegan"],
        "photo": recipe_pic['cauliflower'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe17 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Braised large shrimp",
        "description": "This is a Braised large shrimp recipe", 
        "utensils": ["Cutting board", "Knife", "Frying pan", "Cooking spoon", "Small bowl"],
        "ingredients": 
        [
            {"ingredient": "Ginger", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Spring onions", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Large shrimp", "units": "", "quantity": "", "extraInstructions": "12 û 15, unpeeled"}, 
            {"ingredient": "Red wine", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Soy sauce", "units": "", "quantity": "", "extraInstructions": "light"}, 
            {"ingredient": "Soy sauce", "units": "", "quantity": "", "extraInstructions": "dark"}, 
            {"ingredient": "Potato starch", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Water", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Vegetable oil for frying", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 4,
        "method": 
        [
            "Finely chop garlic. Cut ginger and spring onion into thin strips.", 
            "Heat some vegetable oil in a frying pan over medium heat. Add shrimp and sautΘ for approx. 1 min. on each side until red.", 
            "Add garlic, ginger, and spring onions to the pan. Deglaze with red wine. Season with salt and sugar. Then, add light and dark soy sauce.", 
            "Add parts of the water. Bring to a simmer, cover, and allow to cook on low-medium heat for approx. 3 û 4 min.", 
            "Dissolve starch in the remaining water. Mix well to avoid lumps and stir into the sauce. Return to a simmer and immediately remove from heat. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Chinese"],
        "dietaries": [],
        "photo": recipe_pic['shrimp'],
        "prepTime": "0 hours 25 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe18 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user3,
        "title" : "Steamed pork buns",
        "description": "This is a Steamed pork buns recipe", 
        "utensils": ["Measuring cup", "Large mixing bowl", "Spatula", "Spoon", "Cutting board", "Knife", "Large pot", "Rolling pin", "Steam basket"],
        "ingredients": 
        [
            {"ingredient": "Ground pork", "units": "lbs", "quantity": 1.1, "extraInstructions": ""}, 
            {"ingredient": "Flour", "units": "oz", "quantity": 9.0, "extraInstructions": ""}, 
            {"ingredient": "Water", "units": "cup", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Scallions", "units": "oz", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Yeast", "units": "oz", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Ginger", "units": "oz", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Oyster sauce", "units": "tsp", "quantity": 4.0, "extraInstructions": ""}, 
            {"ingredient": "White pepper", "units": "tbsp", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Five-spice powder", "units": "tbsp", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Light soy sauce", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Dark soy sauce", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sesame oil", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Flour for dusting", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 6,
        "method": 
        [
            "Dissolve yeast in warm water, add flour and work into a dough. Set aside to rest for approx. 2 hrs.", 
            "Finely slice the scallions and chop the ginger. In another mixing bowl, add scallions and ginger to the pork along with salt, white pepper, five-spice powder, light soy sauce, dark soy sauce, oyster sauce and sesame oil. If needed, add a little water to loosen the mixture. Stir well to combine and set aside.", 
            "Bring a large pot of water to a boil. Roll the dough into a log shape and cut into 15 equal portions. Dust the work surface with flour, then use a rolling pin to roll out the pieces of dough into equal-sized circles, rotating the dough as you roll it to ensure an even thickness. Place a spoonful of the pork filling in the center of each dough circle and gently pull and pinch the edges together to make a tight seal. Set aside to rise for 20 min.", 
            "Transfer buns to a steam basket set over boiling water and steam for approx. 15 min.  Allow to cool and enjoy!"
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["Chinese", "Asian"],
        "dietaries": ["Dairy Free"],
        "photo": recipe_pic['steamed_buns'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 15 mins"
    }).json()['id']
    
    recipe19 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "Sichuan-style crispy pork belly",
        "description": "This is a Sichuan-style crispy pork belly recipe", 
        "utensils": ["Slotted spoon", "Cutting board", "Knife", "Large pot", "Wok"],
        "ingredients": 
        [
            {"ingredient": "Pork belly", "units": "g", "quantity": 500.0, "extraInstructions": ""}, 
            {"ingredient": "Red bell pepper", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Green bell pepper", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Green onion", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Onion", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "cloves", "quantity": 3.0, "extraInstructions": ""}, 
            {"ingredient": "Ginger", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Fermented bean paste", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tbsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Red chili flakes", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sweet bean sauce", "units": "tbsp", "quantity": 2.0, "extraInstructions": "Tian Mian Jiang"}, 
            {"ingredient": "Chili sauce", "units": "tbsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Soy sauce", "units": "tbsp", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Oil for frying", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 4,
        "method": 
        [
            "Fill pot a third of the way with water and poach pork belly for approx. 10 min. in boiling water. Drain and slice pork into thin slices. Dice bell peppers into bite-sized pieces. Chop green onion, onion, garlic, and ginger.", 
            "Heat oil in a wok over medium-high heat and fry pork until golden brown. Add fermented bean paste, garlic, and ginger and sautΘ for approx. 2 min. Add the bell peppers and season with sugar, red chili flakes, sweet bean sauce, chili sauce, soy sauce, salt, and pepper to taste. SautΘ for approx. 2 more min. Serve in a large bowl. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Chinese", "Asian"],
        "dietaries": ["Dairy Free"],
        "photo": recipe_pic['sichuan'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe20 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "BBQ ribs with charred corn salad",
        "description": "This is a BBQ ribs with charred corn salad recipe", 
        "utensils": ["Bowl (small)", "Large ovenproof pot with lid", "Oven", "Frying pan", "Knife", "Cutting board", "Citrus press", "Bowl (large)"],
        "ingredients": 
        [
            {"ingredient": "Pork ribs", "units": "lbs", "quantity": 4.4, "extraInstructions": ""}, 
            {"ingredient": "Sweet corn", "units": "", "quantity": "", "extraInstructions": "cooked"}, 
            {"ingredient": "Smoked paprika powder", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Garlic powder", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Fennel seeds", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Worcestershire sauce", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Maple syrup", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Chili powder", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Ketchup", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Red onion", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Jalapeno", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Cherry tomatoes", "units": "oz", "quantity": 5.25, "extraInstructions": ""}, 
            {"ingredient": "Avocado", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Cilantro", "units": "oz", "quantity": 1.25, "extraInstructions": ""}, 
            {"ingredient": "Lime", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}, 
            {"ingredient": "Sunflower oil", "units": "", "quantity": "", "extraInstructions": "for frying"}
        ],
        "servings": 4,
        "method": 
        [
            "To make the marinade, add smoked paprika powder, garlic powder, fennel seeds, Worcestershire sauce, maple syrup, chili powder, and ketchup to a bowl. Season with salt and pepper and mix well. Place ribs in a large ovenproof pot with lid and cover with the marinade until evenly coated. Cover with the lid and transfer to the fridge to marinate for at least 2 hrs. or, at best, overnight.", 
            "Preheat oven to 150░C/300░F. Transfer pot to the oven and bake for 45 min.", 
            "To make the corn salad, first heat some sunflower oil in a frying pan. Add corn to the pan and fry on all sides until golden. Set aside to cool.", 
            "Halve the onion, then slice. Deseed jalape±o and slice finely. Quarter cherry tomatoes. Halve avocado, pit, then scoop out the flesh and chop into pieces. Finely slice cilantro. Slice corn off the cob. Juice lime. Add all ingredients to a bowl along with olive oil and season with salt and pepper. Toss well to combine and season.", 
            "After the ribs have cooked for 45 min., increase the heat to 200░C/390░F. Take out the pot and remove the lid. Return the pot to the oven and let cook for a further 10 min. Serve ribs with the charred corn salad. Enjoy!"
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["American"],
        "dietaries": ["Dairy Free"],
        "photo": recipe_pic['ribs'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 55 mins"
    }).json()['id']
    
    recipe21 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Glass noodle salad with lemongrass dressing",
        "description": "This is a Glass noodle salad with lemongrass dressing recipe", 
        "utensils": ["Knife", "Cutting board", "Pot", "Saucepan", "Citrus press", "5 bowls"],
        "ingredients": 
        [
            {"ingredient": "Glass noodles", "units": "g", "quantity": 250.0, "extraInstructions": ""}, 
            {"ingredient": "Cucumber", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Carrot", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Yellow bell pepper", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Mango", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Snow peas", "units": "g", "quantity": 150.0, "extraInstructions": ""}, 
            {"ingredient": "Lime", "units": "", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Chili", "units": "", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Lemongrass", "units": "stalk", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Sesame oil", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Soy sauce", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Rice vinegar", "units": "tsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Mint", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Cilantro", "units": "g", "quantity": 10.0, "extraInstructions": ""}, 
            {"ingredient": "Roasted peanuts", "units": "", "quantity": "", "extraInstructions": "for garnish"}, 
            {"ingredient": "Sesame seeds", "units": "", "quantity": "", "extraInstructions": "for garnish"}
        ],
        "servings": 4,
        "method": 
        [
            "Halve cucumber and slice into half moons. Slice carrot, bell pepper, and mango into matchsticks. Roughly chop peanuts.", 
            "Bring a saucepan of salted water to a boil. Blanch snow peas for approx. 30 sec. Drain, let cool, and slice diagonally. Cook glass noodles according to package instructions.", 
            "Juice the limes and finely slice chili. Tenderize lemongrass with the back of a knife, then finely slice. In a bowl, combine lemongrass, lime juice, sesame oil, soy sauce, sugar, rice vinegar, and chili. Mix well.", 
            "Divide glass noodles into serving bowls. Top with sliced vegetables, mango, and salad dressing. Garnish with fresh mint and cilantro, peanuts, and sesame seeds. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Vietnamese", "Asian"],
        "dietaries": ["Dairy Free", "Vegetarian", "Vegan"],
        "photo": recipe_pic['glass_noodle'],
        "prepTime": "0 hours 45 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']
    
    recipe22 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user1,
        "title" : "Watermelon-beet salad with cherry tomatoes",
        "description": "This is a Watermelon-beet salad with cherry tomatoes recipe", 
        "utensils": ["Frying pan", "Large bowl", "Cutting board", "Knife", "Bowl", "Whisk"],
        "ingredients": 
        [
            {"ingredient": "Watermelon", "units": "g", "quantity": 500.0, "extraInstructions": ""}, 
            {"ingredient": "Cherry tomatoes", "units": "", "quantity": 12.0, "extraInstructions": ""}, 
            {"ingredient": "Red beets", "units": "g", "quantity": 300.0, "extraInstructions": "cooked"}, 
            {"ingredient": "Pine nuts", "units": "g", "quantity": 50.0, "extraInstructions": ""}, 
            {"ingredient": "Romaine lettuce", "units": "head", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Chili pepper", "units": "", "quantity": 1.0, "extraInstructions": ""}, 
            {"ingredient": "Lemon", "units": "", "quantity": 0.5, "extraInstructions": "zest and juice"}, 
            {"ingredient": "White balsamic vinegar", "units": "ml", "quantity": 100.0, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tbsp", "quantity": 2.0, "extraInstructions": ""}, 
            {"ingredient": "Salt", "units": "tsp", "quantity": 0.5, "extraInstructions": ""}, 
            {"ingredient": "Olive oil", "units": "ml", "quantity": 100.0, "extraInstructions": ""}
        ],
        "servings": 4,
        "method": 
        [
            "Toast pine nuts in a frying pan over medium-high heat until fragrant and lightly browned.", 
            "Wash and dry romaine lettuce. Cut into thin strips and set aside. Cube red beets and add to a large bowl. Peel watermelon and dice. Halve cherry tomatoes and add to the bowl with red beets and watermelon.", 
            "Halve chili, remove the seeds, and finely dice. Zest and juice lemon. Add lemon zest, juice, balsamic vinegar, chili pepper, sugar, salt, and olive oil to a bowl, and stir until well combined.", 
            "Serve the watermelon-beet salad with shredded romaine lettuce, toasted pine nuts, and balsamic vinaigrette. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["American"],
        "dietaries": ["Dairy Free", "Vegetarian", "Vegan"],
        "photo": recipe_pic['watermelon_beet'],
        "prepTime": "0 hours 25 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe23 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Eggs on avocado toast",
        "description": "Delicious eggs on toast.", 
        "utensils": ["Grill pan", "Citrus juicer", "Cups", "Knife", "Medium saucepan", "Spoon"],
        "ingredients": 
        [
            {"ingredient": "Eggs", "units": "", "quantity": 2, "extraInstructions": ""}, 
            {"ingredient": "Rye bread", "units": "", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Lime", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Avocado", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "White vinegar", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""}  
        ],
        "servings": 2,
        "method": 
        [
            "Toast bread in an ungreased grill pan, approx. 2 – 3 min. per side.", 
            "Juice lime. Remove pit from avocado. Slice avocado and layer slices on top of the toast. Season with lime juice, salt, and pepper.", 
            "In a medium saucepan, bring salted water to a boil. Then reduce heat and add white vinegar. Crack eggs into separate cups. Stir water continuously with a cooking spoon to form a whirlpool. Then carefully pour eggs, one by one, into water. Cook eggs for 3 – 4 min, then use a slotted spoon to gently remove from water.",
            "Set on top of toast and season with salt and pepper to taste. Enjoy!"
        ],
        "difficulty": "Easy",
        "mealType": "Breakfast",
        "cuisine": ["American"],
        "dietaries": ["Dairy Free", "Vegetarian"],
        "photo": recipe_pic['eggs_on_toast'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe24 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user3,
        "title" : "Turkish scrambled eggs",
        "description": "Scrambled eggs, the Turkish way.", 
        "utensils": ["Frying pan", "Cutting board", "Cooking spoon", "Knife"],
        "ingredients": 
        [
            {"ingredient": "Eggs", "units": "", "quantity": 4, "extraInstructions": ""}, 
            {"ingredient": "Onion", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Bell peppers", "units": "", "quantity": 3, "extraInstructions": ""},
            {"ingredient": "Parsley", "units": "g", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "White vinegar", "units": "tbsp", "quantity": 15, "extraInstructions": ""},
            {"ingredient": "Canned crushed tomatoes", "units": "ml", "quantity": 400, "extraInstructions": ""},
            {"ingredient": "Chili flakes", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Feta", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Pepper", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Sugar", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Rye bread", "units": "", "quantity": "", "extraInstructions": "for frying"},
            {"ingredient": "Olive oil", "units": "", "quantity": "", "extraInstructions": "for serving"}
        ],
        "servings": 4,
        "method": 
        [
            "Peel and mince onion. Wash yellow and green bell pepper, remove seeds and finely dice. Pluck parsley leaves from the stems and finely chop.", 
            "In a large frying pan, heat olive oil over medium-high heat. Add onion and sauté for approx. 2 min. Add yellow and green bell pepper and sauté for approx. 3 min. more. Reduce heat and add canned crushed tomatoes. Season to taste with salt, pepper, and sugar. Add chili flakes, stir to combine, and let simmer for approx. 5 min.", 
            "With a cooking spoon, create hollows in the pepper-tomato mixture and crack an egg in each hollow. Simmer for approx. 1 min., or until eggs are slightly set. Then, stir eggs in circular movements, distributing them around the pan. Simmer for approx. 5 more min., or until eggs have set. Crumble feta over and garnish with chopped parsley. Enjoy with fresh bread!"
        ],
        "difficulty": "Easy",
        "mealType": "Breakfast",
        "cuisine": ["European"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['scrambled_eggs'],
        "prepTime": "0 hours 20 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe25 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "Coffee Cheesecake",
        "description": "Coffee Cheesecake", 
        "utensils": ["Bowl", "Spatula", "Cake platter", "Knife"],
        "ingredients": 
        [
            {"ingredient": "Chocolate cookies", "units": "g", "quantity": 250, "extraInstructions": ""}, 
            {"ingredient": "Butter", "units": "g", "quantity": 40, "extraInstructions": ""},
            {"ingredient": "Sugar", "units": "g", "quantity": 60, "extraInstructions": ""},
            {"ingredient": "Gelatin", "units": "bag", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Water", "units": "ml", "quantity": 150, "extraInstructions": ""},
            {"ingredient": "Cream cheese", "units": "g", "quantity": 500, "extraInstructions": ""},
            {"ingredient": "Yogurt", "units": "g", "quantity": 300, "extraInstructions": ""},
            {"ingredient": "Baileys", "units": "ml", "quantity": 200, "extraInstructions": ""},
            {"ingredient": "Dark chocolate", "units": "g", "quantity": 90, "extraInstructions": ""},
            {"ingredient": "Espresso", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Cream", "units": "ml", "quantity": 80, "extraInstructions": ""}
        ],
        "servings": 12,
        "method": 
        [
            "Place cookies in a freezer bag. Tightly seal bag and crush cookies with a rolling pin.", 
            "In a small saucepan, melt butter over medium heat and add brown sugar. Place crumbled cookies into a large bowl and pour melted butter on top. Stir well to combine.", 
            "Add gelatin to a small bowl with cold water. Leave to soak for approx. 8 – 10 min.",
            "Add cookie crumb mixture to a round baking form, press firmly into bottom of baking form, and transfer to fridge to cool for approx. 10 - 15 min. In the meantime, mix yogurt, cream cheese and Baileys in a large bowl. Put the gelatine into a pan, add brown sugar, bring to a boil and fold in the joghurt-mixture. When cookie crumb has chilled, add yogurt and cream cheese mixture into the baking form. Gently tap on counter to release air bubbles. Transfer to fridge and allow to set for approx. 3 - 4 hours.",
            "Finely chop chocolate and transfer to a large bowl. In a small saucepan, bring espresso powder, cream, and golden syrup to a simmer over medium heat. Pour over chopped chocolate, let stand for approx. 15 – 30 sec., and then stir well to combine.",
            "Carefully run knife around edges of the baking form. Remove cake and transfer to a cake platter. Evenly spread ganache over top of cheesecake. Garnish cake with an outer ring of coffee flavored chocolates. Enjoy with a cold glass of Baileys!"
        ],
        "difficulty": "Medium",
        "mealType": "Dessert",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['coffee_cake'],
        "prepTime": "0 hours 40 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe26 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "Fluffy apple pancakes",
        "description": "Fuwa fuwa", 
        "utensils": ["Bowl", "Spatula", "Cake platter", "Knife", "Whisk", "Hand mixer", "Grater"],
        "ingredients": 
        [
            {"ingredient": "Apples", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Walnuts", "units": "g", "quantity": 150, "extraInstructions": ""},
            {"ingredient": "Eggs", "units": "", "quantity": 4, "extraInstructions": ""},
            {"ingredient": "Milk", "units": "ml", "quantity": 360, "extraInstructions": ""},
            {"ingredient": "Flour", "units": "g", "quantity": 340, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "g", "quantity": 180, "extraInstructions": ""},
            {"ingredient": "Baking powder", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Lime", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Vanilla extract", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Butter", "units": "", "quantity": "", "extraInstructions": "for frying"}
        ],
        "servings": 16,
        "method": 
        [
            "Whisk together flour, some of the sugar, a pinch of salt, and baking powder.",
            "Juice lime. Heat lime juice and the remaining sugar in a frying pan over medium-low heat, stirring often. Once sugar has melted, add walnuts and continue to cook until nuts are caramelized, approx. 3 – 4 min. Remove from heat.",
            "Separate eggs and add egg whites to grease-free stand mixer. Set yolks aside. Beat egg whites on high until soft peaks form.",
            "In a large bowl, whisk together milk and egg yolks.",
            "Sift in flour mixture and mix well, making sure there are no lumps.",
            "Fold egg whites into the batter.",
            "Grate apple into the batter and add vanilla extract. Stir to combine.",
            "Heat some butter in a frying pan over medium heat. Spoon batter into frying pan and cook until golden brown (approx. 2 – 3 min. per side). Transfer to a plate to serve.",
            "To serve, top with caramelized walnuts and dried fruit. Drizzle on maple syrup and enjoy as a delightful breakfast!"
        ],
        "difficulty": "Easy",
        "mealType": "Breakfast",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['apple_pancakes'],
        "prepTime": "0 hours 25 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe27 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user5,
        "title" : "Chicken curry",
        "description": "Hot n spicy.", 
        "utensils": ["Knife", "Food grinder", "Nonstick pan", "Grater"],
        "ingredients": 
        [
            {"ingredient": "Chicken", "units": "g", "quantity": 400, "extraInstructions": ""},
            {"ingredient": "Chicken masala", "units": "tbsp", "quantity": 4, "extraInstructions": ""},
            {"ingredient": "Turmeric powder", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Chili powder", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Garlic-ginger paste", "units": "g", "quantity": 2, "extraInstructions": ""}, 
            {"ingredient": "Yogurt", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Onions", "units": "", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Tomatoes", "units": "", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Oil", "units": "tbsp", "quantity": 8, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Take 200g of boneless chicken. Cut them into pieces of acceptable size.",
            "Put the pieces in a bowl. Add salt, turmeric powder, chilli powder, chicken masala (or meat masala or garam masala) powder, garlic-ginger paste, curd and 1tsp oil.",
            "Mix well. The pieces should have the spices evenly applied. Keep marinated aside for 1hr.",
            "Take 2 medium tomatoes and 2 medium onions. Make puree for each. If you don't have a mixer, you can use the smallest holes in a grater to get puree like paste.",
            "Take a pan. Add 3tsp of oil. Heat on low flame for 2mins. Add onion puree and stir for 2mins. Add tomato puree. Mix well and stir for 2mins. You should see water leaving from sides.",
            "Close lid and let it cook for 10mins. No need to add water. Natural water from tomatoes and chicken should be enough.",
            "Open the lid and stir well. Chicken should look more cooked now. Close lid again and let it cook for 5mins. Use low flame throughout.",
            "Open the lid and mix well. Paste must have thickened. Curry is ready! Serve hot."
        ],
        "difficulty": "Easy",
        "mealType": "Main",
        "cuisine": ["Indian"],
        "dietaries": [""],
        "photo": recipe_pic['chicken_curry'],
        "prepTime": "0 hours 25 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe28 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Thai chicken noodle soup",
        "description": "aroi maad", 
        "utensils": ["Knife", "Cutting board", "Large bowl", "Sauce pan", "Colander", "Grater"],
        "ingredients": 
        [
            {"ingredient": "Chicken", "units": "g", "quantity": 150, "extraInstructions": ""},
            {"ingredient": "Chicken stock", "units": "ml", "quantity": 350, "extraInstructions": ""},
            {"ingredient": "Rice noodles", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Enoki mushrooms", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Ginger", "units": "g", "quantity": 20, "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "clove", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Lemon grass", "units": "stalk", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Celery", "units": "stalk", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Peanut oil", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Carrot", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Green onions", "units": "", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Cilantro", "units": "g", "quantity": 10, "extraInstructions": ""},
            {"ingredient": "Soy sauce", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Oyster sauce", "units": "tbsp", "quantity": 1, "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Lightly smash lemon grass. Peel ginger and grate finely. Peel garlic and remove the green sprout if necessary and chop finely.",
            "Heat up peanut oil and add garlic and ginger to roast. Add soy sauce and oyster sauce and fill with chicken stock. Add lemon grass and kaffir lime leaves and bring everything to a boil.",
            "Cut celery into sticks and the carrot into walnut-sized pieces. Cut the chicken breast into pieces twice as large.",
            "Next, add the celery, carrots, and chicken to the stock and cook on low heat for approx. 5 - 10 min. until fully cooked.",
            "Meanwhile, soak rice noodles in hot water, according to the package instructions.",
            "Cut green onions into fine rings. Then, cut the stalks off enoki mushrooms and finely chop cilantro.",
            "Drain rice noodles and add to the soup, along with the green onions, enoki mushrooms, and cilantro. Serve immediately, so that the mushrooms keep their bite and the cilantro keeps its color."
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["Thai"],
        "dietaries": ["Dairy Free"],
        "photo": recipe_pic['thai_chicken_noodle_soup'],
        "prepTime": "0 hours 30 mins",
        "cookTime": "0 hours 0 mins"
    }).json()['id']

    recipe29 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user2,
        "title" : "Neopolitan pizza",
        "description": "Cheese!", 
        "utensils": ["Spatula", "Whisk", "Large bowl", "Oven", "Baking sheet", "Pastry cutter"],
        "ingredients": 
        [
            {"ingredient": "Italian flour", "units": "g", "quantity": 400, "extraInstructions": ""},
            {"ingredient": "Whole-wheat flour", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Yeast", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Mozzarella", "units": "g", "quantity": 200, "extraInstructions": ""},
            {"ingredient": "Canned crushed tomatoes", "units": "g", "quantity": 400, "extraInstructions": ""}, 
            {"ingredient": "Garlic", "units": "clove", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "tbsp", "quantity": 2, "extraInstructions": ""},
            {"ingredient": "Water", "units": "ml", "quantity": 500, "extraInstructions": ""},
            {"ingredient": "Olive oil", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Basil", "units": "stalk", "quantity": 1, "extraInstructions": ""}
        ],
        "servings": 4,
        "method": 
        [
            "Add Italian flour, whole wheat flour, and dry yeast to a large bowl. Mix with a whisk until combined. Add the lukewarm water. Mix with a rubber spatula until no dry flour is visible. The dough will be relatively moist at this point. Drizzle the surface with a little olive oil, then cover with a kitchen towel or dough cover and leave to rise in a warm place. After approx. 1.5 – 2 hrs, the volume should have doubled and you can continue with step 2. Alternatively, you can leave the dough in the fridge to slowly rise overnight to further develop flavor and get an even puffier result.",
            "Dust a work surface with flour. Tip the dough out of the bowl, fold each side into the centre to trap in some air and turn it over. Use flour as needed to help handle the dough (this will depend on how wet your dough is), but use sparingly. Divide the dough into four equal parts using a dough cutter. Fold each of these pieces using the same method as above. Place each dough ball seam-side down and shape into a firm ball using the edges of your hands and moving in a circular motion. Now either store, individually wrapped, in the fridge for up to 3 days (take out 1 hr. before baking), store in the freezer for up to 3 months (take out at least 8 hrs. before baking) or leave to rest on the work surface for approx. 1 hr. (if you’re in an absolute hurry, you could reduce this resting time) and use immediately.",
            "In the meantime, preheat the oven to the highest setting on the top/bottom heat function and place an inverted baking sheet on the lowest shelf. Once the oven is preheated and the rising time is over, shape each dough ball into a pizza: Flour the work surface and use your fingertips to flatten the ball from the inside out, leaving a thick edge. Use flour as needed. Once your palm can fit in the centre, lift the dough up and use gravity, stretching gently. to help you form a larger pizza. Place on a sheet of parchment paper, which, if you have one, you can place on top of a pizza paddle.",
            "Top your pizza with whatever you like best. I like to use canned tomatoes mixed with fresh garlic, salt and a little olive oil as a base and then add buffalo mozzarella and basil after baking. It’s best not to use too much sauce, 1.5 – 2 tablespoons are usually enough, and be sure to transfer your pizza in the oven with the baking paper immediately after topping so that the raw dough doesn't draw in too much liquid. As soon as the pizza has baked through, after approx. 3 – 4 min., carefully remove the parchment paper from underneath and finish baking the pizza. Keep baking for approx. 8 – 12 min. (the timing will depend on your oven) until your crust is browned. Repeat the process with the remaining dough. If you like, finish with some lemon zest and freshly grated Parmesan.",
            "Happy pizza making—enjoy!"
        ],
        "difficulty": "Medium",
        "mealType": "Main",
        "cuisine": ["Italian"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['neopolitan_pizza'],
        "prepTime": "0 hours 10 mins",
        "cookTime": "0 hours 10 mins"
    }).json()['id']

    recipe30 = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user4,
        "title" : "Oyster mushroom satay",
        "description": "My stomach has mushroom for mushroom.", 
        "utensils": ["Skewers", "Large bowl", "2 bowls", "Pastry brush", "Baking sheet", "Oven", "Knife"],
        "ingredients": 
        [
            {"ingredient": "Oyster mushrooms", "units": "g", "quantity": 450, "extraInstructions": ""},
            {"ingredient": "Soy sauce", "units": "tbsp", "quantity": 3, "extraInstructions": ""},
            {"ingredient": "Sweet soy sauce", "units": "tbsp", "quantity": 4, "extraInstructions": ""},
            {"ingredient": "Peanut butter", "units": "tbsp", "quantity": 4, "extraInstructions": ""},
            {"ingredient": "Coconut milk", "units": "ml", "quantity": 50, "extraInstructions": ""}, 
            {"ingredient": "Chili", "units": "", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Lime juice", "units": "tbsp", "quantity": 3, "extraInstructions": ""},
            {"ingredient": "Ginger", "units": "g", "quantity": 10, "extraInstructions": ""},
            {"ingredient": "Salt", "units": "", "quantity": "", "extraInstructions": ""},
            {"ingredient": "Coriander", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Soak the wooden skewers in warm water for about 30 minutes beforehand. Use your hands to tear the oyster mushrooms into even strips. Then place the mushroom strips closely but evenly spaced on the wooden skewers. This makes about 6-8 skewers.",
            "In a small bowl, mix soy sauce, half of the sweet soy sauce, ground coriander and sesame oil. Using a brush, coat both sides of the mushroom skewers with the marinade. If you're using the grill, grill them in indirect heat for about 5-8 minutes per side, until they are nice and crispy on the outside. If you're using the oven, roast the skewers on a baking tray lined with baking paper at 275°C/530°F top/bottom heat for approx. 7 min. per side and fire up the oven grill for the last few minutes for a crispy finish.",
            "For the sauce, add peanut butter, the remaining sweet soy sauce, coconut milk, chili, lime juice, and ginger to a food processor and puree until a homogeneous but still slightly chunky sauce is formed. Season to taste with a little salt and more lime juice. Coarsely chop a few peanuts and fold about 1 tablespoon into the sauce. Arrange the grilled skewers together with the sauce on a plate. Sprinkle the skewers with the remaining chopped peanuts."
        ],
        "difficulty": "Easy",
        "mealType": "Side",
        "cuisine": ["Asian"],
        "dietaries": ["Vegetarian", "Vegan"],
        "photo": recipe_pic['mushroom_satay'],
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 15 mins"
    }).json()['id']

    # Update user profiles with titles, bio and profile picture
    title1 = requests.post(f"http://localhost:5001/api/profile/1/update", json={
        'token' : user1,
        "title" : "Food Connoisseur",
        "bio" : "I love creating and eating food :)",
        "profile_picture" : pfp['shallot'],
    }).json()
    
    requests.post(f"http://localhost:5001/api/profile/2/update", json={
        'token' : user2,
        "title" : "Big Enchilada",
        "bio" : "I love enchiladas!",
        "profile_picture" : pfp['guzman'],
    }).json()
    
    requests.post(f"http://localhost:5001/api/profile/3/update", json={
        'token' : user3,
        "title" : "Sous Chef",
        "bio" : "L’assaisonnement est parfait.",
        "profile_picture" : pfp['colette'],
    }).json()
    
    requests.post(f"http://localhost:5001/api/profile/4/update", json={
        'token' : user4,
        "title" : "Bobby",
        "bio" : "I am Bob.",
        "profile_picture" : pfp['bob'],
    }).json()
    
    # Make users like random recipes
    recipes = [recipe1, recipe2, recipe3, recipe4, recipe5, recipe6, recipe7, recipe8, recipe9, recipe10, recipe11, recipe12, recipe13, recipe14, recipe15, recipe16, recipe17, recipe18, recipe19, recipe20, recipe21, recipe22]
    for recipe in recipes:
        requests.post(f"http://localhost:5001/api/like", headers={ 'token': user1 }, json={
            'recipeId' : recipe,
        }).json()
        
    for recipe in recipes[::2]:
        requests.post(f"http://localhost:5001/api/like", headers={ 'token': user2 }, json={
            'recipeId' : recipe,
        }).json()
        
    for recipe in recipes[::3]:
        requests.post(f"http://localhost:5001/api/like", headers={ 'token': user3 }, json={
            'recipeId' : recipe,
        }).json()
        
    for recipe in recipes[::4]:
        requests.post(f"http://localhost:5001/api/like", headers={ 'token': user4 }, json={
            'recipeId' : recipe,
        }).json()
        
    for recipe in recipes[::5]:
        requests.post(f"http://localhost:5001/api/like", headers={ 'token': user5 }, json={
            'recipeId' : recipe,
        }).json()
        
    # Make users subscribe to each other
    user_ids = [1,2,3,4,5]
    for id in user_ids[1:]:
        requests.post(f"http://localhost:5001/api/subscribe", headers={ 'token': user1 }, json={
            'userId' : id,
        })
        
    for id in user_ids[:-1]:
        requests.post(f"http://localhost:5001/api/subscribe", headers={ 'token': user2 }, json={
            'userId' : id,
        })
        
    for id in user_ids[::2]:
        requests.post(f"http://localhost:5001/api/subscribe", headers={ 'token': user5 }, json={
            'userId' : id,
        })
        
    requests.post(f"http://localhost:5001/api/subscribe", headers={ 'token': user4 }, json={
        'userId' : 4
    })

    # Add comments to test data
    user_tokens = [user1, user2, user3, user4, user5]
    comments = [
        "I recommended this recipe to my grandkids and they loved it. In fact I recommended this recipe to my whole village and they applauded in tears",
        "This recipe is superb, my grandkids love it.",
        "Are these recipes suitable for Rats?", 
        "Wow If I could give it a 10 I would",
        "Meh I could make better",
        "My condiments to the chef",
        "Goto www.kitchencrypto and invest in kitchencoin, it's going to the moon",
        "Fantastic recipe Barbara.",
        "The gals loved this recipe",
        "Tastes just like how I remember it",
        "Wow great recommendation",
        "Amazing",
        "@josh please make this tonight for dinner",
        "Highly commended",
        "hello",
        "Please keep making more of these, my chickens love it",
        "Thank you for this recipe, will be sure to share.",
        "How many toppings do you recommend with this?"
        "How long should I take for preparing this recipe?",
        "The servings for this recipe aren't accurate for big families like ours.",
        "Truly iconic",
        "Instructions were spot on, great job",
        "Gladys myself and the rest of the ladies absolutely loved this recipe, it's a hit at our PTA meetings",
        "Lorelai and Luke recommended this recipe to us and we love it."
        "This is my favourite meal",
        "***** you this dish is brilliant",
        "Is this as easy to make as Macha Latte?",
        "Where is the sauce",
        "Just saw this on My Kitchen rules and had to see the recipe for myself."
    ]

    # Add ratings to the recipes
    ratings = [1,2,3,4,5]
    for recipe in recipes:
        requests.post(f'http://localhost:5001/api/{recipe}/comment', headers = {}, json={
            'token': random.choice(user_tokens),
            'comment': random.choice(comments),
        })

        requests.post(f'http://localhost:5001/api/{recipe}/comment', headers = {}, json={
            'token': random.choice(user_tokens),
            'comment': random.choice(comments),
            'rating': random.choice(ratings)
        })

        requests.post(f'http://localhost:5001/api/{recipe}/comment', headers = {}, json={
            'token': random.choice(user_tokens),
            'comment': random.choice(comments)
        })

        requests.post(f'http://localhost:5001/api/{recipe}/comment', headers = {}, json={
            'token': random.choice(user_tokens),
            'comment': random.choice(comments),
            'rating': random.choice(ratings)
        })

###############################################################################
def test_register():
    # Pytest being run for tests and not to generate data
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    if len(recipes) != 30:
        return

    user = requests.post(f"http://localhost:5001/api/register", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
        "username" : "LambSauce",
        "name" : "Rordam Gamsay"
    }).json()
    assert user['token'] != None

###############################################################################
def test_logout():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_make_recipe():
    # Pytest being run for tests and not to generate data
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    if len(recipes) != 30:
        return

    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Make a recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Mango lassi",
        "description": "Who's a good boy?", 
        "utensils": ["Cutting board", "Knife", "Blender"],
        "ingredients": 
        [
            {"ingredient": "Mangoes", "units": "", "quantity": 4, "extraInstructions": ""},
            {"ingredient": "Coconut milk", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Yogurt", "units": "g", "quantity": 300, "extraInstructions": ""},
            {"ingredient": "Honey", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Water", "units": "ml", "quantity": 200, "extraInstructions": ""}, 
            {"ingredient": "Ice", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 2,
        "method": 
        [
            "Peel and cut mangoes into cubes.",
            "Add mangoes, ice cubes, cold water, honey, and yogurt to blender.",
            "Blend on high until smooth, approx. 2 – 3 min.",
            "Add coconut milk and blend to combine, approx. 1 – 2 min. Enjoy immediately."
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["Indian"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['mango_lassi'],
        "prepTime": "0 hours 10 mins",
        "cookTime": "0 hours 0 mins"
    }).json()
    assert recipe['id'] != None

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_recipe_save():
    # Pytest being run for tests and not to generate data
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    if len(recipes) != 31:
        return

    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Make a recipe with the wrong title
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Iced chocolate latte",
        "description": "Quite cold indeed", 
        "utensils": ["Cutting board", "Knife", "2 bowls", "Fork", "Hand mixer", "Straw"],
        "ingredients": 
        [
            {"ingredient": "Strawberries", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Milk", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Espresso", "units": "ml", "quantity": 50, "extraInstructions": ""},
            {"ingredient": "Cream", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Vanilla sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Ice", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Brew two shots of espresso and let them cool down. Meanwhile, remove the stem of the strawberries and halve them. Add them to a bowl with the sugar and mash them with a fork until you have a smooth puree that is not too thick.",
            "Add cream to a bowl and slowly whip it using a hand mixer with a whisk attachment. While whipping, add the vanilla sugar, then increase the speed and beat until stiff. Set aside.",
            "Add the strawberry purée to a highball glass and fill halfway with mini ice cubes.",
            "Fill with milk. Slowly pour the espresso shots into the glass. Avoid stirring to keep the layering.",
            "Top with cream using a spoon or a piping bag. Garnish with a fresh strawberry. Cheers!"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['strawberry_latte'],
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()
    assert recipe['id'] != None

    # Edit the recipe with the correct title
    recipe_edit = requests.post(f"http://localhost:5001/api/recipe/save", json={
        'id' : recipe['id'],
        'token' : user['token'],
        "title" : "Iced strawberry latte",
        "description": "Quite cold indeed", 
        "utensils": ["Cutting board", "Knife", "2 bowls", "Fork", "Hand mixer", "Straw"],
        "ingredients": 
        [
            {"ingredient": "Strawberries", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Milk", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Espresso", "units": "ml", "quantity": 50, "extraInstructions": ""},
            {"ingredient": "Cream", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Vanilla sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Ice", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Brew two shots of espresso and let them cool down. Meanwhile, remove the stem of the strawberries and halve them. Add them to a bowl with the sugar and mash them with a fork until you have a smooth puree that is not too thick.",
            "Add cream to a bowl and slowly whip it using a hand mixer with a whisk attachment. While whipping, add the vanilla sugar, then increase the speed and beat until stiff. Set aside.",
            "Add the strawberry purée to a highball glass and fill halfway with mini ice cubes.",
            "Fill with milk. Slowly pour the espresso shots into the glass. Avoid stirring to keep the layering.",
            "Top with cream using a spoon or a piping bag. Garnish with a fresh strawberry. Cheers!"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['strawberry_latte'],
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    })
    assert recipe_edit.status_code == 200

    # Check title is correct now
    recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={}).json()
    assert recipe_info['title'] == "Iced strawberry latte"

    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_explore_recipes():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Check if theres 32 recipes (size of test data)
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    assert len(recipes) == 32

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_delete_recipe():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Create a test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Iced chocolate latte",
        "description": "Quite cold indeed", 
        "utensils": ["Cutting board", "Knife", "2 bowls", "Fork", "Hand mixer", "Straw"],
        "ingredients": 
        [
            {"ingredient": "Strawberries", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Milk", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Espresso", "units": "ml", "quantity": 50, "extraInstructions": ""},
            {"ingredient": "Cream", "units": "ml", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Vanilla sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""}, 
            {"ingredient": "Sugar", "units": "tbsp", "quantity": 1, "extraInstructions": ""},
            {"ingredient": "Ice", "units": "", "quantity": "", "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Brew two shots of espresso and let them cool down. Meanwhile, remove the stem of the strawberries and halve them. Add them to a bowl with the sugar and mash them with a fork until you have a smooth puree that is not too thick.",
            "Add cream to a bowl and slowly whip it using a hand mixer with a whisk attachment. While whipping, add the vanilla sugar, then increase the speed and beat until stiff. Set aside.",
            "Add the strawberry purée to a highball glass and fill halfway with mini ice cubes.",
            "Fill with milk. Slowly pour the espresso shots into the glass. Avoid stirring to keep the layering.",
            "Top with cream using a spoon or a piping bag. Garnish with a fresh strawberry. Cheers!"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": recipe_pic['strawberry_latte'],
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()
    assert recipe['id'] != None

    # Check its been added to list of recipes
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    assert len(recipes) == 33

    # Delete the recipe
    recipe_delete = requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })
    assert recipe_delete.status_code == 200

    # Check number of recipes decreased
    recipes = requests.get(f"http://localhost:5001/api/recipes").json()
    assert len(recipes) == 32

    # Check if the deleted recipe gives an error
    recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={})
    assert recipe_info.status_code == 404

    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_like_recipe():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Create recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Test",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Strawberries", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Test"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Like the recipe
    recipe_like = requests.post(f"http://localhost:5001/api/like", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # There should be 1 like on the recipe now
    recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={}).json()
    assert recipe_info['likes'] == 1

    # Cleanup and delete the recipe
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_unlike_recipe():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Test",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Strawberries", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Test"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Like the recipe
    recipe_like = requests.post(f"http://localhost:5001/api/like", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Recipe should have 1 like
    recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={}).json()
    assert recipe_info['likes'] == 1

    # Unlike the recipe
    recipe_unlike = requests.post(f"http://localhost:5001/api/unlike", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Recipe should have 0 likes now
    recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={}).json()
    assert recipe_info['likes'] == 0

    # Cleanup and delete recipe
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_user_info_recipe():
    user_followers = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()
    assert user_followers['email'] == "user1@gmail.com"
    assert user_followers['username'] == "charlxtte"
    assert user_followers['name'] == "Shallot Shan"
    assert user_followers['title'] == "Food Connoisseur"
    assert user_followers['bio'] == "I love creating and eating food :)"

###############################################################################
def test_subscribe_recipe():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Get number of current followers
    user_followers = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()['followers']

    # Subscribe
    subscribe = requests.post(f"http://localhost:5001/api/subscribe", headers={'token': user['token']}, json={
        'userId' : 1
    })
    assert subscribe.status_code == 200

    # Check number of followers has increased by 1
    user_info = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()
    assert user_info['followers'] == (user_followers + 1)

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_unsubscribe_recipe():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # Get number of current followers
    user_followers = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()['followers']

    # Already subscribed from last test so it should error
    subscribe = requests.post(f"http://localhost:5001/api/subscribe", headers={'token': user['token']}, json={
        'userId' : 1
    })
    assert subscribe.status_code == 400

    # Number of followers should stay the same
    user_info = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()
    assert user_info['followers'] == user_followers

    # unsubscribe
    unsubscribe = requests.post(f"http://localhost:5001/api/unsubscribe", headers={'token': user['token']}, json={
        'userId' : 1
    })
    assert unsubscribe.status_code == 200

    # Check number of followers has decreased
    user_info = requests.get(f"http://localhost:5001/api/userInfo?userId=1", json={}).json()
    assert user_info['followers'] == user_followers - 1

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_personalised_feed():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    assert user['token'] != None

    # subscribe to user 1 and 2
    requests.post(f"http://localhost:5001/api/subscribe", headers={'token': user['token']}, json={
        'userId' : 1
    })
    requests.post(f"http://localhost:5001/api/subscribe", headers={'token': user['token']}, json={
        'userId' : 2
    })

    subscribed_users = [1,2]
    # Check personal feed only has recipes from those two users
    recipes = requests.get(f"http://localhost:5001/api/personalised_recipes", headers={'token': user['token']}).json()
    for recipe in recipes:
        recipe_info = requests.get(f"http://localhost:5001/api/recipe?recipeId={recipe['id']}", headers={}, json={}).json()
        assert recipe_info['authorId'] in subscribed_users

    # Cleanup by unsubscribing
    requests.post(f"http://localhost:5001/api/unsubscribe", headers={'token': user['token']}, json={
        'userId' : 1
    })
    requests.post(f"http://localhost:5001/api/unsubscribe", headers={'token': user['token']}, json={
        'userId' : 2
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200


###############################################################################
def test_change_user_info():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
    # Update user info
    requests.post(f"http://localhost:5001/api/profile/6/update", json={
        'token' : user['token'],
        'title' : "Idiot sandwich",
        'bio' : "Guess how many Michelin stars I have"
    })

    # Check user info has been updated
    user_info = requests.get(f"http://localhost:5001/api/userInfo?userId=6", json={}).json()
    assert user_info['title'] == "Idiot sandwich"
    assert user_info['bio'] == "Guess how many Michelin stars I have"

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_change_user_credentials():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Change credentials
    requests.post(f"http://localhost:5001/api/credentials/manage", json={
        'token' : user['token'],
        'username' : "Lamb Sause",
    })

    # Check credentials have changed
    user_info = requests.get(f"http://localhost:5001/api/userInfo?userId=6", json={}).json()
    assert user_info['username'] == "Lamb Sause"

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200


###############################################################################
def test_adding_to_pantry():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Add ingredient to pantry
    requests.post(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={
        'add' : ['Poppy'],
        'delete' : []
    })
    
    # Check ingredient has been added to pantry
    pantry = requests.get(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={}).json()
    assert pantry['pantry'] == ['Poppy']

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_deleting_from_pantry():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Remove ingredient from pantry
    requests.post(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={
        'add' : [],
        'delete' : ['Poppy']
    })
    
    # Check pantry is empty
    pantry = requests.get(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={}).json()
    assert pantry['pantry'] == []
    
    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_is_makeable():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Add ingredient to pantry
    requests.post(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={
        'add' : ['Poppy'],
        'delete' : []
    })

    # Create a test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "Test",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Test"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Check if its been added to makeable recipes
    recipes = requests.get(f"http://localhost:5001/api/makeable_recipes", headers={'token' : user['token']}, json={}).json()
    assert len(recipes['recipes']) == 1

    # Delete ingredient from pantry
    requests.post(f"http://localhost:5001/api/pantry", headers={'token': user['token']}, json={
        'add' : [],
        'delete' : ['Poppy']
    })

    # Delete the recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

###############################################################################
def test_search_by_title():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Make test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "Test"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Search by title to find the single recipe
    recipes = requests.get(f"http://localhost:5001/api/search?title=asdfghj").json()
    assert len(recipes) == 1

    # Search by wrong title for 0 recipes
    recipes = requests.get(f"http://localhost:5001/api/search?title=asdfghjk").json()
    assert len(recipes) == 0

    # Delete recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })


###############################################################################
def test_search_by_method():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "qwerty"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Search by method, should be single recipe
    recipes = requests.get(f"http://localhost:5001/api/search?method=qwerty").json()
    assert len(recipes) == 1

    # Search by wrong method, should be 0 recipes
    recipes = requests.get(f"http://localhost:5001/api/search?method=qwertyu").json()
    assert len(recipes) == 0

    # Delete recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })

###############################################################################
def test_search_by_ingredients():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Garlic", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "qwerty"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Search by ingredient added, should be 1 recipe
    recipes = requests.get(f"http://localhost:5001/api/search?include=Poppy").json()
    assert len(recipes) == 1

    # Search by ingredient added but ingredient excluded, should be 0 recipes
    recipes = requests.get(f"http://localhost:5001/api/search?include=Poppy&exclude=Garlic").json()
    assert len(recipes) == 0

    # Delete recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })

###############################################################################
def test_search_by_mealtype():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Garlic", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "qwerty"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Search by mealtype
    recipes = requests.get(f"http://localhost:5001/api/search?mealtypes=Beverage").json()
    assert len(recipes) == 3

    # Delete recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })


###############################################################################
def test_add_comment():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()

    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Garlic", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "qwerty"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Should be 0 comments on new recipe
    comments = requests.get(f"http://localhost:5001/api/{recipe['id']}/comments").json()
    assert len(comments) == 0

    # Add comment to recipe
    comment = requests.post(f"http://localhost:5001/api/{recipe['id']}/comment", json={
        'token' : user['token'],
        'comment' : "Test comment"
    })
    assert comment.status_code == 200

    # Should be 1 comment on recipe now
    recipes = requests.get(f"http://localhost:5001/api/{recipe['id']}/comments").json()
    assert len(recipes) == 1

    # Delete recipe for cleanup
    delete = requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })
    assert delete.status_code == 200

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })


###############################################################################
def test_delete_comment():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Create test recipe
    recipe = requests.post(f"http://localhost:5001/api/recipe/create", json={
        'token' : user['token'],
        "title" : "asdfghj",
        "description": "Test", 
        "utensils": ["Cutting board"],
        "ingredients": 
        [
            {"ingredient": "Poppy", "units": "g", "quantity": 100, "extraInstructions": ""},
            {"ingredient": "Garlic", "units": "g", "quantity": 100, "extraInstructions": ""}
        ],
        "servings": 1,
        "method": 
        [
            "qwerty"
        ],
        "difficulty": "Easy",
        "mealType": "Beverage",
        "cuisine": ["American"],
        "dietaries": ["Vegetarian"],
        "photo": None,
        "prepTime": "0 hours 15 mins",
        "cookTime": "0 hours 0 mins"
    }).json()

    # Add comment
    comment = requests.post(f"http://localhost:5001/api/{recipe['id']}/comment", json={
        'token' : user['token'],
        'comment' : "Test comment"
    })
    assert comment.status_code == 200

    # Check comment exists
    recipes = requests.get(f"http://localhost:5001/api/{recipe['id']}/comments").json()
    assert len(recipes) == 1

    # Delete comment
    new_comment = requests.delete(f"http://localhost:5001/api/{recipe['id']}/comment", json={
        'token' : user['token'],
        'commentId' : recipes[0]['id'],
        'comment' : ""
    })
    assert new_comment.status_code == 200

    # Check number of comments decreased by 1
    recipes = requests.get(f"http://localhost:5001/api/{recipe['id']}/comments").json()
    assert len(recipes) == 0

    # Delete recipe for cleanup
    requests.delete(f"http://localhost:5001/api/recipe", headers={'token': user['token']}, json={
        'recipeId' : recipe['id']
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })


###############################################################################
def test_change_password():
    # Login
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    }).json()
   
    # Change password
    requests.post(f"http://localhost:5001/api/credentials/manage", json={
        'token' : user['token'],
        'current_password' : "Password1!",
        'new_password' : "Password2!",
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user['token']
    })
    assert logout.status_code == 200

    # Try login from old password, should cause error
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password1!",
    })
    assert user.status_code != 200

    # Login with correct password
    user = requests.post(f"http://localhost:5001/api/login", json={
        'email' : "user6@gmail.com",
        "password" : "Password2!",
    })
    assert user.status_code == 200

    # Cleanup by changing back to initial password
    requests.post(f"http://localhost:5001/api/credentials/manage", json={
        'token' : user.json()['token'],
        'current_password' : "Password2!",
        'new_password' : "Password1!",
    })

    # Logout
    logout = requests.post(f"http://localhost:5001/api/logout", json={
        'token' : user.json()['token']
    })
    assert logout.status_code == 200
