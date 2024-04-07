from flask import render_template
from flaskapp import app, db

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error404.html'), 404