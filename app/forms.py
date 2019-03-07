from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired("Enter your first name.")])
    username = StringField('Username', validators=[DataRequired("User name must be from 2 to 20 charakters long."), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')
    