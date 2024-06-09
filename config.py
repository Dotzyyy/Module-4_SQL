import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    if os.environ.get('ENV') == 'local':

        SQLALCHEMY_DATABASE_URI = os.environ.get('LOCAL_DATABASE_URL')
    
    else:

        SQLALCHEMY_DATABASE_URI = os.environ.get('RENDER_DATABASE_URL')

    

    
    