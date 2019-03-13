from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User

#Registration form with validation rules.
class RegisterForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=8)])
    submit = SubmitField('Sign Up')
    
    # checking the username alredy exist in the database and returning error message to the form
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The user with this username exists. Please choos a different username.')
            
# Login from with remember me check box. Browswer will remember user in secure cookie for same time.
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#Update account details form with validation rules.
class UpdateAccountForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update')
    
    # checking the username alredy exist in the database and returning error message to the form
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The user with this username exists. Please choos a different username.')