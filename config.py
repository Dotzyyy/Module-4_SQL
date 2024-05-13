import os

class Config:

    if 'RENDER' in os.environ:
        # Running on Render
        db_uri = os.environ['DATABASE_URL']
    else:
    # Local development
        db_uri = 'postgresql://postgres:password@localhost:5432/flask_db'



    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    