from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

#Registration form with validation rules.
class RegisterForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired("Enter your first name.")])
    username = StringField('Username', validators=[DataRequired("User name must be from 2 to 20 charakters long."), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired("Passwords must be at least 8 characters long."),Length(min=3, max=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

# Login from with remember me check box. Browswer will remember user in secure cookie for same time.
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Incorect username"), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired("Incorect Password")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    