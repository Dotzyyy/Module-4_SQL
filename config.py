import os
from sqlalchemy import *

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    
    if os.environ.get('RENDER'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        # Use the local database URL if RENDER environment variable is not set
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/flask_db"