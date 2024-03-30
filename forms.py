from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):

    """Add an option where you can login with email OR account"""
    
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember User')

    submit = SubmitField('Login')