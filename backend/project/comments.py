import string
import uuid
from project.models.orm import UserOrm, CommentOrm, RecipesOrm
from project.error import InputError,InternalServerError,AccessError

def create_comment(userId:uuid, recipeId:uuid, comment:string, photo:string="", rating:float=0) -> None:
	"""Given user inputs this function will create a comment on a recipe

	Args:
		userId (uuid): id of the user creating the comment
		recipeId (uuid): id of the recipe under which the comment is created
		comment (string): the comment itself
		photo (string, optional): Optional photo attachment to comment. Defaults to "".
		rating (float, optional): rating associated with the comment. Defaults to 0.

	Raises:
		InputError: The user does not exist 
		InternalServerError: Comment creation failed.

	Returns:
		_type_: _description_
	"""
	query_username = UserOrm.select(UserOrm.username).where(UserOrm.id==userId).dicts().first()
	
	if not query_username:
		raise InputError("The user specified does not exist")

	is_valid_recipe(recipeId)
	"""
	query_existing_comment = CommentOrm.select(CommentOrm.userId).where(CommentOrm.userId==userId,CommentOrm.recipeId==recipeId).dicts()
	if query_existing_comment:
		raise InputError("User has already added a review comment")
	"""
	
	query_pfp = UserOrm.select(UserOrm.profilePic).where(UserOrm.id==userId).first()
	
	if not query_pfp:
		query_pfp = None 
	if rating == 0:
		rating = None
	queried_comment = CommentOrm.create(
										recipeId=recipeId,
										userId=userId,
										username=query_username['username'],
										comment=comment,
										photo=photo,
										rating=rating
										)
	if not queried_comment:
		raise InternalServerError("Failed to create new comment")
	
	return None


def edit_comment(userId:int, commentId:uuid, comment:string, photo:string, rating:float) -> None:
	"""Update a comment and associated photo

	Args:
		userId (int): id of the user who owns the comment
		commentId (uuid): id of the comment
		comment (string): message of the comment to update to 
		photo (string): Update the associated photo of the comment 

	Raises:
		AccessError: Attempt to modify a non-existent comment

	Returns:
		None: returns None upon success
	"""
	param_updates = {}

	if photo is not None: 
		param_updates[CommentOrm.photo] = photo
	
	if comment is not None:
		param_updates[CommentOrm.comment] = comment

	if rating is not None:
		param_updates[CommentOrm.rating] = rating
	
	if rating == 0:
		param_updates[CommentOrm.rating] = None

	query_comment = CommentOrm.update(param_updates).where(CommentOrm.id==commentId,CommentOrm.userId==userId).execute()

	if not query_comment:
		raise AccessError("Attempted to modify a comment which does not exist")	

	return None  


def delete_comment(userId:int,commentId:uuid) -> None:	
	""" Deletes a comment by commentId

	Args:
		userId (int): user id of the user requesting deletion
		commentId (uuid): id of the comment which is being deleted

	Raises:
		AccessError: Raised if the comment specified does not exist

	Returns:
		None: returns None
	"""
	query_comment = CommentOrm.select().where(CommentOrm.id==commentId,CommentOrm.userId==userId).dicts().first()
	if query_comment is None: 
		raise AccessError("Attempted to delete a comment which does not exist")

	query_deletion = CommentOrm.delete().where(CommentOrm.id==commentId).execute()
	if not query_deletion:
		raise AccessError("Comment specified does not exist")
	
	return None 

def delete_comments_from_recipe(recipeId: uuid) -> None:
    query_comment = CommentOrm.select().where(CommentOrm.recipeId ==recipeId).dicts().first()
    if query_comment is not None: 
        CommentOrm.delete().where(CommentOrm.recipeId==recipeId).execute()
    return None


def rate_comment(userId:int, commentId:uuid, rating:int) -> None:
	"""_summary_

	Args:
		userId (int): _description_
		commentId (uuid): _description_
		rating (int): _description_

	Raises:
		InputError: _description_
		AccessError: _description_
	"""
	if commentId not in range(1,5):
		raise InputError("Rating must be within 1 to 5")

	query_comment = CommentOrm.update({CommentOrm.rating:rating}).where(CommentOrm.id==commentId,CommentOrm.userId==userId).execute()

	if not query_comment:
		raise AccessError("Attempted to modify a comment which does not exist")	
	
	return None


def get_comments(recipeId:string) -> list:
	"""Returns a list of comments 

	Args:
		recipeId (string): The uuid associated with a recipe, represented as a string

	Returns:
		list: a list of dictionaries of comments
	"""
	query_recipe_comments = []

	if is_valid_recipe(recipeId):
		query_recipe_comments = list(CommentOrm.select().where(CommentOrm.recipeId==recipeId).dicts())
	for obj in query_recipe_comments:
		if obj["profilePic"] == None:
			queryPic = UserOrm.select(UserOrm.profilePic).where(UserOrm.profilePic!=None, UserOrm.id==obj["userId"]).dicts()
			obj["profilePic"] = queryPic[0]['profilePic'] if queryPic else None
	return query_recipe_comments

def get_average_rating(recipeId:string)	-> float | None:
	"""Returns the average user rating for a given recipe

	Args:
		recipeId (string): the recipeId for which we want the average rating for  
	
	Raises:
		InputError: If the recipe does not have any ratings associated with it.
	

	Returns:
		float: the average user rating for the given recipe 
	"""
	is_valid_recipe(recipeId)
	query_rating = list(CommentOrm.select(CommentOrm.rating).where(CommentOrm.recipeId==recipeId).dicts())
	accumulator = 0
	count = len(query_rating)
	if count == 0:
		return None
	for item in query_rating:
		rating = item["rating"]
		if rating is not None:
			accumulator += float(item["rating"])
		else:
			count -= 1
	if count == 0:
		return None
	return accumulator/count


def is_valid_recipe(recipeId:string) -> True:
	"""Return true if recipeId is valid

	Args:
		recipeId (string): The uuid associated with a recipe, represented as a string

	Raises:
		InputError: If recipeId does not exist

	Returns:
		True: returns True if recipe is found
	"""
	try: 
		recipeUuid = uuid.UUID(recipeId)
	except:
		raise InputError("Error: Not a valid uuid")

	try: 
		RecipesOrm.select().where(RecipesOrm.id==recipeUuid).get()
	except:
		raise InputError("Could not verify recipeId")

	return True 

def delete_comments(recipeId:string) -> True:
	"""
	Deletes all comments associated with a recipe

    Args:recipeId (string): The uuid associated with a recipe, represented as
	
	Raises:
        InputError: If recipeId does not exist 
		InternalServerError: If the reviews associated with the recipeId cannot be deleted
	
	Returns:
        True: returns True if successful
	"""
	if is_valid_recipe(recipeId):
		try:
			CommentOrm.delete().where(CommentOrm.id==recipeId).execute()
		except:
			raise InternalServerError("Failed to delete reviews associated with recipeId")
		return True 

