from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from urllib.parse import urlsplit
from datetime import datetime, timezone




import sqlalchemy as sa

from config import Config




app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://david_sexton:xvzBRkawcGGQAdFiiqxjqVoHJpigL33U@dpg-coa5stsf7o1s73dku450-a/flask_db_9euf'
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login.login_view = 'login'

from models import User, Post
from forms import LoginForm, RegistrationForm, EditInfo, UserPost, FollowerButton
from errors import *








@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = UserPost()
    if form.validate_on_submit():
         
         post = Post(body=form.post.data, author=current_user)
         db.session.add(post)
         db.session.commit()
         flash('Post has been submitted')
         return redirect(url_for('index'))
    posts = db.session.scalars(current_user.following_posts()).all()
    return render_template('index.html', title='Home', form=form, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('index')) 

@app.route('/register', methods=['GET', 'POST'])
def register():
     if current_user.is_authenticated:
          return redirect(url_for('index'))
     form = RegistrationForm()
     if form.validate_on_submit():
          user = User(username=form.username.data, email=form.email.data)
          user.set_password(form.password.data)
          db.session.add(user)
          db.session.commit()
          flash('Account creation successful!')
          return redirect(url_for('login'))
     return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
     user = db.first_or_404(sa.select(User).where(User.username == username))
     posts = db.session.scalars(current_user.following_posts()).all()
     form = FollowerButton()
     return render_template('my_profile.html', user=user, posts=posts, form=form) 

@app.route('/edit_info', methods=['GET', 'POST'])
@login_required
def edit_info():
    form = EditInfo()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Changes Saved.')
        return redirect(url_for('edit_info'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_info.html', title='Edit Info',
                           form=form)

@app.route('/tasks')
@login_required
def tasks():
    return render_template('tasks.html', title='Task List')

@app.before_request
def before_request():
     if current_user.is_authenticated:
          current_user.last_seen = datetime.now(timezone.utc)
          db.session.commit()


@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = FollowerButton()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username))
        if user is None:
            flash(f'User {username} not found.')
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(f'Now following {username}!')
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))
    

@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = FollowerButton()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username))
        if user is None:
            flash(f'User {username} not found.')
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(f'You are not following {username}.')
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

@app.route('/find_user')
@login_required
def find_user():
    query = sa.select(Post).order_by(Post.timestamp.desc())
    posts = db.session.scalars(query).all()
    return render_template('index.html', title='Explore', posts=posts)      




if __name__ == '__main__':
        app.run(debug=True)