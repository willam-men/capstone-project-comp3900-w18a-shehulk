import string
from project.models.orm import UserOrm
from project.error import InputError,InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


def get_profile(userId:int, private:bool=False) -> list:
    """Get the profile of a user given a userId and a private boolean.

    Args:
        userId (int, optional): Id for the user whose profile is to be retrieved.
        private (bool, optional): Optional flag to get private details. Defaults to False.

    Raises:
        InternalServerError: If the user does not exist in the database

    Returns:
        list: of user details
    """
    if private: 
        query_user = list(UserOrm.select(UserOrm.id,UserOrm.username,UserOrm.name, UserOrm.email, UserOrm.title, UserOrm.bio, UserOrm.email, UserOrm.profilePic).where(UserOrm.id==userId).dicts())
    else:
        query_user = query_user = list(UserOrm.select(UserOrm.id, UserOrm.username, UserOrm.title, UserOrm.bio, UserOrm.profilePic).where(UserOrm.id==userId).dicts())
    if not query_user : raise InternalServerError("Error could not find user")
    if private : query_user.pop('email',None) and query_user.pop('')
    return query_user

def update_profile(userId:int, name:string=None, title:string=None, bio:string=None, pfp:string=None) -> None:
    """Takes in multiple non-none parameters and updates the profile for the given userId 

    Args:
        userId (int): unique identifier for the user
        name (string, optional): name which the user wishes to set. Defaults to None.
        title (string, optional): title which the user goes by. Defaults to None.
        bio (string, optional): string with biographical info. Defaults to None.
        pfp (string, optional): image string. Defaults to None.

    Raises:
        InputError: The specified user does not exist
        InternalServerError: Update profile fails
    """
    query_name = UserOrm.select(UserOrm.name).where(UserOrm.id==userId).dicts().first()
    if not query_name:
        raise InputError("The user specified does not exist")
    input_hash= {
        'id':userId,
        'name':name,
        'title':title, 
        'bio':bio, 
        'profilePic':pfp
    }
    inputs_transformed = {k:v for k,v in input_hash.items() if v != None}
    query_update = UserOrm.update(inputs_transformed).where(UserOrm.id==userId).execute()
    if not query_update:
        raise InternalServerError("Failed to update profile")
    return 

def update_user_credentials(userId:int, username:string=None, email:string=None, passwordCurrent:string=None, passwordNew:string=None):
    """_summary_

    Args:
        userId (int): _description_
        username (string, optional): _description_. Defaults to None.
        email (string, optional): _description_. Defaults to None.
        passwordCurrent (string, optional): _description_. Defaults to None.
        passwordNew (string, optional): _description_. Defaults to None.

    Raises:
        InputError: Password entered does not match with current password, New Password cannot be the same as old password, New Password does not follower validation_rules
        InternalServerError: username, password or email cannot be updated

    Returns:
        dict: empty dict on success
    """
    if email is not None : 
        try: 
            UserOrm.update({'email' : email}).where(UserOrm.id==userId).execute()
        except:
            raise InternalServerError("Failed to update email address")
    if username is not None : 
        try: 
            UserOrm.update({'username' : username}).where(UserOrm.id==userId).execute()
        except:
            raise InternalServerError("Failed to update username")

    if passwordCurrent is not None and passwordNew is not None:       
        query_old_password = UserOrm.select(UserOrm.password).where(UserOrm.id==userId).dicts()
        if not check_password_hash(query_old_password.first()['password'], passwordCurrent):
            raise InputError("password entered does not match with current password")
        validation_rules = [
                lambda s: not check_password_hash(query_old_password.first()['password'], s) or 'New Password cannot be the same as the old password'
                ]

        problems = [problem for problem in [rules(passwordNew) for rules in validation_rules] if problem != True]
        if problems:
            raise InputError(problems)


        query_update_password = UserOrm.update({'password' : generate_password_hash(passwordNew, method='sha256')}).where(UserOrm.id==userId).execute()
        if not query_update_password: 
            raise InternalServerError("Failed to update password")
    return {}