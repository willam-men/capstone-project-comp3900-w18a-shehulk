from datetime import datetime
from peewee import Model, IntegerField, CharField, UUIDField, DoubleField, DateTimeField
from playhouse.postgres_ext import ArrayField, JSONField, BinaryJSONField

from project.database import db

class PeeweeBase(Model):
    class Meta:
        database = db()

class TestOrm():
    id = IntegerField()

class UserOrm(PeeweeBase):
    id = IntegerField(primary_key=True)
    username = CharField()
    name = CharField()
    email = CharField()
    password = CharField()
    title = CharField()
    bio = CharField()
    followerIds = ArrayField(IntegerField)
    followingIds = ArrayField(IntegerField)
    profilePic = CharField(null=True)
    publishedRecipes = ArrayField(UUIDField)
    savedRecipes = ArrayField(UUIDField)
    pantry = ArrayField(CharField)
    mealPlans = ArrayField(UUIDField)

    class Meta:
        table_name = "users"

class TokenOrm(PeeweeBase):
    jsonWebToken = CharField(primary_key=True)
    userId = IntegerField() # Foreign Key 
    class Meta:
        table_name = "tokens"

class CommentOrm(PeeweeBase):
    id = UUIDField(primary_key=True)
    recipeId = UUIDField()
    userId = IntegerField()
    username = CharField()
    profilePic = CharField(null=True)
    comment = CharField(null=True)
    photo = CharField(null=True)
    rating = DoubleField(null=True)

    class Meta:
        table_name = "comments"

class RecipesOrm(PeeweeBase):
    id = UUIDField(primary_key=True)
    status = CharField()
    title = CharField()
    description = CharField()
    authorName = CharField()
    authorId = IntegerField()
    authorPfp = CharField()
    servings = IntegerField()
    ingredients = BinaryJSONField(default=[])
    method = ArrayField(CharField)
    mealType = CharField()
    photo = CharField(null=True, default=None)
    viewCount = IntegerField(default=0)
    likedList = ArrayField(IntegerField, default=[])
    savedList = ArrayField(IntegerField, default=[])
    lastUpdated = DateTimeField(default=datetime.now())
    utensils = ArrayField(CharField)
    dietaries = ArrayField(CharField)
    difficulty = CharField(null=True)
    cuisine = ArrayField(CharField)
    prepTime = CharField()
    cookTime = CharField()

    class Meta:
        table_name = "recipes"

class IngredientsOrm(PeeweeBase):
    ingredient = CharField(primary_key=True)
    recipes = ArrayField(UUIDField, default=[])

    class Meta:
        table_name = "ingredients"