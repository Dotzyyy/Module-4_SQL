import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '961fc2bb17a331c5c14847e730850e4d'
    
    if os.environ.get('RENDER'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://flask2_db_user:fUIr43Xuux1HCZmOGyD7V1GFb2etJpy9@dpg-coa4a5i1hbls73fjajlg-a.frankfurt-postgres.render.com/flask2_db')
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', "postgresql://postgres:password@localhost:5432/flask_db")