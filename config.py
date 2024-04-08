import os
from sqlalchemy import *
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    SQLALCHEMY_DATABASE_URI = "DATABASE_URL"
    
    if os.environ.get('RENDER'):
        connection_string = os.environ.get('DATABASE_URL')
    
    else:
        connection_string = os.environ.get('DATABASE_URL', "postgresql://postgres:password@localhost:5432/flask_db" )