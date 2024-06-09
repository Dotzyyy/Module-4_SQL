from flask import render_template
from app import db

def internal_error(error):
    db.session.rollback()
    return render_template('error500.html'), 500

def not_found_error(error):
    return render_template('error404.html'), 404