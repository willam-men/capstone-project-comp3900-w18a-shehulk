from enum import Enum
from typing import Dict, List
from uuid import UUID
from pydantic import BaseModel

class Recipe(BaseModel):
    status: str
    title: str 
    description: str
    authorName: str
    authorId: int
    authorPfp: str = None
    servings: int
    ingredients: List[Dict[str, str]]
    method:List[str]
    difficulty: str
    mealType: str
    photo: str = None
    viewCount: int 
    likedList: List[int]
    savedList: List[int]
    lastUpdated: str
    utensils: List[str]
    cuisine: List[str]
    dietaries: List[str]
    prepTime: str
    cookTime: str

class User(BaseModel):
    userId: int
    name: str 
    pfp: str = None

class UserCredentials(BaseModel):
    id: UUID
    password: str

class Payload(BaseModel):
    token: str
    valid: bool
    id: int

class RecipeStatus(str, Enum):
    PUBLISHED = 'Published'
    DRAFT = 'Draft'

recipe = {
    "title": "Garlic Broccolini", 
    "description": "This is a recipe that …", 
    "utensils": ["Garlic Press", "Large skillet"],
    "ingredients": [
        {"quantity": "2", 
        "units":"Bunches", 
        "ingredient": "Broccolini", 
        "extraInstructions": ""}, 
        {"quantity": "1", 
        "units":"tablespoon", 
        "ingredient": "olive oil"}, 
        {"quantity": "2", 
        "units":"cloves", 
        "ingredient": "garlic"}, 
        {"quantity": "1", 
        "units":"teaspoon", 
        "ingredient": "salt"},
        {"quantity": "1/2", 
        "units":"cup", 
        "ingredient": "water"}],
    "servings": 2,
    "method": ["Rinse the Broccolini under cold water and shake off the excess water. Trim about 2cm off the bottom off the Broccolini stems.",
        "Heat the oil in a large straight skillet over medium-high heat until shimmering. Add the Broccolini and saute until the Broccolini is bright green and some of the stems and tips of the florets are lightly charred, 5 to 7 minutes.",
        "Press the garlic in a garlic press, and add the salt. Continue to saute for about 30 seconds. Add the water, cover and cook until the Broccolini is a vibrant green (1-2 minutes). Serve immediately."],
    "difficulty": "Easy",
    "mealType": "Side",
    "cuisine": ["cuisine 1", "cuisine 2"],
    "dietaries": ["Gluten free", "Very cool", "Haraam ovo lactoseitarian"],
    "photo": None,
    "prepTime": "30 mins",
    "cookTime": "20 mins",
    "status": "Published",
    "authorName": 'Test User',
    "authorId": 1,
    "authorPfp": None
}
