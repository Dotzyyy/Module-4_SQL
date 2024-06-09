import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    if os.environ.get('RENDER') == 'local':
        
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://flask_db_d6ml_user:DlJLp9X8q21fl9RBoZP8Y5zkTXDdgVVk@dpg-cpiq6oi1hbls73bl78j0-a/flask_db_d6ml')
        
    
    else:

        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql://postgres:password@localhost:5432/flask_db')

    

    
    