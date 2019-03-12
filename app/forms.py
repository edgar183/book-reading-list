from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

#Registration form with validation rules.
class RegisterForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=8)])
    submit = SubmitField('Sign Up')

# Login from with remember me check box. Browswer will remember user in secure cookie for same time.
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    