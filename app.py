from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *

if __name__ == '__main__':
        app.run(debug=True)

posts = [
    
    {
        'author': 'David Sexton',
        'title': 'Board Game 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ornare nibh finibus sapien vehicula, eget pulvinar turpis porttitor.',
        'date': '10/01/24',
    },

    {
        'author': 'David Sexton',
        'title': 'Board Game 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ornare nibh finibus sapien vehicula, eget pulvinar turpis porttitor.',
        'date': '12/01/24',
    },
]



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David' }
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)