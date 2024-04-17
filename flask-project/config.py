import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_NAME', 'database_name')
