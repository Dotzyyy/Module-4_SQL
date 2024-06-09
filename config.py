import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    if os.environ.get('RENDER'):
        
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in')
        
    
    else:

        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql://postgres:password@localhost:5432/flask_db')

    

    
    