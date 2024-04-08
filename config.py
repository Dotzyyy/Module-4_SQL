import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    
    default_connection_string = "postgresql://postgres:password@localhost:5432/flask_db"
    
    if os.environ.get('RENDER'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://david_sexton:xvzBRkawcGGQAdFiiqxjqVoHJpigL33U@dpg-coa5stsf7o1s73dku450-a.frankfurt-postgres.render.com/flask_db_9euf')

    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_connection_string )

        
