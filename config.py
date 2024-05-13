import os

class Config:

    if 'RENDER' in os.environ:
        # Running on Render
        db_uri = os.environ['DATABASE_URL']
        SQLALCHEMY_DATABASE_URI = db_uri
    else:
    # Local development
        db_uri = 'postgresql://postgres:password@localhost:5432/flask_db'
        SQLALCHEMY_DATABASE_URI = db_uri


    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    