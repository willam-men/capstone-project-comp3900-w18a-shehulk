import json
import jwt

from datetime import datetime,timedelta
from werkzeug.security import check_password_hash, generate_password_hash

from project.env import get_flask_app_secret
from project.error import AccessError, InputError
from project.models.orm import TokenOrm, UserOrm
from project.models.schemas import User, UserCredentials, Payload

def create_auth_token(userId: int) -> str:
    """Used to create a basic jwt token 

    Args:
        userId (int): user ID

    Raises:
        InputError: if userId is not an Int 

    Returns:
        str: jwt encoded token
    """
    if not isinstance(userId, int):
        raise InputError("Error: userId invalid")

    token = jwt.encode(
        {
        'iat': datetime.now(),                       # Time at which the JWT was issued; can be used to determine age of the JWT 
        'exp': datetime.now() + timedelta(hours=10000)   # Time after which the JWT expires
        }, 
        get_flask_app_secret(), 
        'HS256'
    )
    TokenOrm.create(
        jsonWebToken=token,
        userId=userId,
    )
    return token   


def destroy_token(token: str) -> bool:
    """Used to destroy tokens

    Args:
        token (str): JWT token

    Raises:
        InputError: if userId is not an Int 

    Returns:
        bool: whether successfully destroyed
    """
    if not token:
        raise InputError("No Token provided")
    if TokenOrm.delete().where(TokenOrm.jsonWebToken==token).execute():
        return True
    else: 
        return False


def is_valid_token(token: str) -> Payload:
    """Used to verify if a jwt web token is valid and current

    Args:
        token (str): JSON Web Token

    Raises:
        InputError:if no token provided 
        AccessError: if token is expired or Invalid

    Returns:
        Payload: JSON payload with the userId and valid set to true upon success, else valid is set to false
    """
    if not token:
        raise InputError('Error: token provided cannot be null') 
    
    # decode token and check expiry date
    try:
        decoded_token = jwt.decode(token, get_flask_app_secret(), algorithms=['HS256']) 
        expiry = datetime.fromtimestamp(decoded_token['exp'])
    
    except Exception as error:
        raise AccessError("Error: Token is Invalid") from error

    # token expired
    if expiry < datetime.now():        
        destroy_token(token)
        return False
    
    # Check if its a valid token
    if TokenOrm.select(TokenOrm.jsonWebToken,TokenOrm.userId).where(TokenOrm.jsonWebToken==token).dicts().first():
        return True

def token_to_id(token: str) -> int:
    """Converts token to user id

    Args:
        token (str): token of the logged in user

    Returns:
        int: user id of user logged in
    """
    token_query = TokenOrm.select(TokenOrm.jsonWebToken,TokenOrm.userId).where(TokenOrm.jsonWebToken==token).dicts().first()
    return token_query['userId']

def get_current_user(token: str) -> User:
    """Get the details of the user that is currently logged in

    Args:
        token (str): token of the logged in user

    Raises:
        AccessError: Token is invalid
        InputError: User does not exist

    Returns:
        User: name, id and profile picture of user logged in
    """
    if not is_valid_token(token):
        raise AccessError("token is invalid")
    user_id = token_to_id(token)
    user_query = UserOrm.select(UserOrm.name, UserOrm.profilePic).where(UserOrm.id == user_id).dicts().first()
    if not user_query:
        raise InputError("User does not exist")
    user = User(userId=user_id, name=user_query['name'], pfp=user_query['profilePic'])
    return user

def check_if_username_email_exists(username: str, email: str) -> bool:
    """Check if username and email already exists

    Args:
        username (str): username
        email (str): email

    Raises:
        InputError: Username / email already exists 

    Returns:
        bool: Whether username and email already exist in our database
    """
    # Query the database to check whether the username or email already exists
    sql_query = UserOrm.select().where(
                            (UserOrm.username==username) |
                            (UserOrm.email==email))

    if sql_query.exists():
        raise InputError("This username or email already exists. Please enter another email/username.")
    
    return False

def register_user(username: str, email: str, name: str, password: str) -> json:
    """Register user with given details

    Args:
        username (str): username
        email (str): email
        name (str): name
        password (str): encrypted password

    Returns:
        json: {"token": string of current valid token for the given user}
    """
    sql_query = UserOrm.create(
                                username=username,
                                email=email,
                                name=name,
                                title="",
                                bio="",
                                password=generate_password_hash(
                                    password,
                                    method='sha256'
                                ),
                                followerIds=[],
                                followingIds=[],
                                publishedRecipes=[],
                                savedRecipes=[]
    )
    sql_query = UserOrm.select(UserOrm.id).where(UserOrm.username==username, UserOrm.email==email).dicts().first()
    token = create_auth_token(sql_query['id'])
    dic = {}
    dic['token'] = token
    return dic

def find_user_from_email(email: str) -> UserCredentials:
    """Find user id and password based on email address

    Args:
        email (str): email address

    Raises:
        InputError: username does not exist in database

    Returns:
        UserCredentials: credentials of the user logged in
    """
    try: 
        sql_query_credentials = UserOrm.select(UserOrm.id,UserOrm.password).where((UserOrm.email==email)).get()
    except: 
        raise InputError("Username provided does not exist")
    return sql_query_credentials
    
def check_password_correct(password: str, sql_query_credentials: UserCredentials) -> json:
    """Check whether password is correct

    Args:
        password (str): encrypted password
        sql_query_credentials (UserCredentials): user id and password of the user attempting to login

    Raises:
        InputError: password does not match the password we have on record

    Returns:
        json: with key 'token' and value of the current valid token
    """
    if check_password_hash(sql_query_credentials.password, password):
        user_query = TokenOrm.select().where(TokenOrm.userId == sql_query_credentials.id).dicts().first()
        dic = {}
        if not user_query:
            token = create_auth_token(sql_query_credentials.id)
            dic['token'] = token
        elif is_valid_token(user_query['jsonWebToken']):
            token = user_query['jsonWebToken']
            dic['token'] = token
        else:
            token = create_auth_token(sql_query_credentials.id)
            dic['token'] = token
        return dic
    raise InputError("Bad Request: Incorrect Password")