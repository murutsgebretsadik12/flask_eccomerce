
# SQLALCHEMY_DATABASE_URI="postgresql://flaskprojecteccomerce_y7i7_user:yEQygoEEAi8M4FwK0uGu6iH9JsfGRG5y@dpg-co2l2rgl6cac73bpoo5g-a.frankfurt-postgres.render.com/flaskprojecteccomerce_y7i7"

# SQLALCHEMY_TRACK_MODIFICATIONS = False

# UPLOAD_FOLDER = 'static/images'  # Folder to store uploaded images

# SECRET_KEY = 'secrete123456'

import os
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "postgresql://username:password@hostname/database")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_FOLDER = 'static/images'
