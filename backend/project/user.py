import uuid
from peewee import fn
from uuid import UUID
from project.models.orm import UserOrm
from project.error import InputError, NotFoundError

def add_subscription(subscriber: int, publisher: int) -> list[int]:
    """Subscribe the 'subscriber' to any of the publisher's recipes

    Args:
        subscriber (int): id of subscriber
        publisher (int): id of publisher

    Raises:
        InputError: Publisher/Subsrciber does not exist in database, or the subscriber has already been subscribed

    Returns:
        list[int]: List of ids of the subscribers that the publisher has
    """
    # check if the publisher exists
    publisher_query = UserOrm.select(UserOrm.followerIds).where(UserOrm.id == publisher).dicts().first()
    if not publisher_query:
        raise InputError("This publisher does not exist.")
    subscriber_query = UserOrm.select(UserOrm.followingIds).where(UserOrm.id == subscriber).dicts().first()
    if not subscriber_query:
        raise InputError("This user does not exist.")

    # If already subscribed don't do anything
    following_publisher = publisher_query['followerIds']
    followed_by_subscriber = subscriber_query['followingIds']
    if (subscriber in following_publisher) or (publisher in followed_by_subscriber):
        raise InputError("User is already subscribed")

    # add subscriber to publishers followerIds in the database
    following_publisher.append(subscriber)
    userORM = UserOrm.update(followerIds = following_publisher).where(UserOrm.id == publisher)
    userORM.execute()

    # add subscriber to publishers followerIds in the database
    followed_by_subscriber.append(publisher)
    userORM = UserOrm.update(followingIds = followed_by_subscriber).where(UserOrm.id == subscriber)
    userORM.execute()
    return following_publisher

def remove_subscription(subscriber: int, publisher: int) -> None:
    """Remove the subscriber's subscription from a publisher

    Args:
        subscriber (int): id of subscriber
        publisher (int): id of publisher

    Raises:
        InputError: Publisher/Subsrciber does not exist in database, or the subscriber was not previously subscribed
    """
    # check if the publisher exists
    publisher_query = UserOrm.select(UserOrm.followerIds).where(UserOrm.id == publisher).dicts().first()
    if not publisher_query:
        raise InputError("This publisher does not exist.")
    subscriber_query = UserOrm.select(UserOrm.followingIds).where(UserOrm.id == subscriber).dicts().first()
    if not subscriber_query:
        raise InputError("This user does not exist.")

    # If already unsubscribed don't do anything
    following_publisher = publisher_query['followerIds']
    followed_by_subscriber = subscriber_query['followingIds']
    if (subscriber not in following_publisher) or (publisher not in followed_by_subscriber):
        raise InputError("User is not subscribed")
    # remove subscriber to publishers followerIds in the database
    following_publisher.remove(subscriber)
    userORM = UserOrm.update(followerIds = following_publisher).where(UserOrm.id == publisher)
    userORM.execute()

    # remove subscriber to publishers followerIds in the database
    followed_by_subscriber.remove(publisher)
    userORM = UserOrm.update(followingIds = followed_by_subscriber).where(UserOrm.id == subscriber)
    userORM.execute()
    return

def get_user_info(user: int) -> dict:
    """Gets the information of a user 

    Args:
        user (int): id of user

    Returns:
        dict: Information about a user
    """
    user_query = UserOrm.select().where(UserOrm.id == user).dicts().first()
    if not user_query:
        raise NotFoundError("User does not exist")
    user_query['followers'] = len(user_query['followerIds'])
    user_query.pop('password')
    user_query.pop('savedRecipes')
    user_query.pop('id')
    user_query.pop('followingIds')
    user_query.pop('publishedRecipes')
    return user_query

def get_user_info_by_id(user: int) -> dict:
    """Gets the name, username, email and profile picture of a user

    Args:
        user (int): id of user that we are finidng the information of

    Raises:
        InputError: user does not exist

    Returns:
        dict: name, username, email and profile picture of the user
    """
    user_query = UserOrm.select(UserOrm.name, UserOrm.username, UserOrm.email, UserOrm.profilePic, UserOrm.id).where(UserOrm.id == user).dicts().first()
    if not user_query:
        raise InputError("User does not exist")
    return user_query

def get_all_user_info() -> list[dict]:
    """Get information of all users

    Returns:
        list[dict]: list of all information of users (bio, email, )
    """
    user_info = list(UserOrm.select().order_by(-fn.cardinality(UserOrm.followerIds), UserOrm.id).dicts())
    for user in user_info:
        user.pop('password')
        user.pop('savedRecipes')
        user.pop('followingIds')
        user['followers'] = len(user['followerIds'])
    return user_info

def remove_recipe_from_user(user_id: int, recipe_id: UUID):
    """Removes recipe from userOrm
    
    Returns:
        Nothing
    """
    user_query = UserOrm.select(UserOrm.publishedRecipes).where(UserOrm.id == user_id).dicts().first()
    if not user_query:
        raise InputError("User does not exist.")
    recipes = user_query['publishedRecipes']
    print(f"recipes are {recipes}")
    print(f"recipe id is {recipe_id}")
    recipes.remove(UUID(recipe_id))
    userORM = UserOrm.update(publishedRecipes = recipes).where(UserOrm.id == user_id)
    userORM.execute()
    return