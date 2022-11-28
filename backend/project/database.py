from peewee import Database
from playhouse.postgres_ext import PostgresqlExtDatabase
from threading import Lock

from project.env import get_db_host, get_pg_user, get_pg_user_password

_lock = Lock()
_db = None 

def db() -> Database:
    with _lock:
        global _db 
        if _db is None:
            _db = _create_db_connection()
    return _db

def _create_db_connection() -> Database:
    return PostgresqlExtDatabase(database=get_pg_user(), host=get_db_host(), user=get_pg_user(), password=get_pg_user_password(), port = 5432)
