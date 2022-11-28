from dotenv import load_dotenv
import os 

load_dotenv()

def get_pg_user_password():
    if (os.environ.get('PG_USER_PASSWORD') == None):
        raise Exception('Missing PG_USER_PASSWORD in .env')
    return os.environ.get('PG_USER_PASSWORD')

def get_db_host():
    if (os.environ.get('DB_HOST') == None):
        raise Exception('Missing DB_HOST in .env')
    return os.environ.get('DB_HOST')

def get_pg_user():
    if (os.environ.get('PG_USER') == None):
        raise Exception('Missing PG_USER in .env')
    return os.environ.get('PG_USER')

def get_pg_admin_email():
    if (os.environ.get('PG_ADMIN_EMAIL') == None):
        raise Exception('Missing PG_ADMIN_EMAIL in .env')
    return os.environ.get('PG_ADMIN_EMAIL')

def get_pg_admin_password():
    if (os.environ.get('PG_ADMIN_PASSWORD') == None):
        raise Exception('Missing PG_ADMIN_PASSWORD in .env')
    return os.environ.get('PG_ADMIN_PASSWORD')

def get_flask_app_secret():
    if (os.environ.get('FLASK_SECRET') == None):
        raise Exception('Missing FLASK_SECRET in .env')
    return os.environ.get('FLASK_SECRET')
