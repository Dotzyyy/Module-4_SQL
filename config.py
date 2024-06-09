import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/flask_db"

    
    