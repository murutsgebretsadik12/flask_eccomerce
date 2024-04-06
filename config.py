
import os
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "postgresql://username:password@hostname/database")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
