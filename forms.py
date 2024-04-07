from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import sqlalchemy as sa
from flaskapp import db
from models import User

class LoginForm(FlaskForm):

    """Add an option where you can login with email OR account"""
    
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember User')

    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data
        ))
        if user is not None:
            raise ValidationError('Username unavailable')
        

class EditInfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=240)])
    submit = SubmitField('Submit')


class UserPost(FlaskForm):
        post = TextAreaField("What's new?", validators=[DataRequired(), Length(min=1, max=140)])
        submit = SubmitField('Submit')


class FollowerButton(FlaskForm):
    submit = SubmitField('Submit')