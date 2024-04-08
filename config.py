import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/flask_db"
    
    if os.environ.get('RENDER'):
        connection_string = os.environ.get('DATABASE_URL', 'postgresql://david_sexton:xvzBRkawcGGQAdFiiqxjqVoHJpigL33U@dpg-coa5stsf7o1s73dku450-a/flask_db_9euf')
    
    else:
        connection_string = os.environ.get('DATABASE_URL', "postgresql://postgres:password@localhost:5432/flask_db" )