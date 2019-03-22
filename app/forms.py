from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import *
#from wtforms_sqlalchemy.fields import QuerySelectField

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
    
    # checking the username alredy exist in the database and return error message to the form
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The user with this username exists. Please choos a different username.')
                
class Add_Author(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    """
    def validate_full_name(self, full_name):
        author = Author.query.filter_by(full_name=full_name.data)
        if author:
            raise ValidationError('The author with this name alredy exists.')
        """    
class Add_Category(FlaskForm):
    Name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    
    """
    def validate_Name(self, Name):
        category = Category.query.filter_by(Name=Name.data)
        if category:
            raise ValidationError('The category alredy exists.')
            """
class Add_Publisher(FlaskForm):
    Name = StringField('Publisher Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    
    def validate_Name(self, Name):
        publisher = Publisher.query.filter_by(Name=Name.data)
        if publisher:
            raise ValidationError('The Publisher alredy exists.')
         
class Add_Readinglist(FlaskForm):
    ListName = StringField('Reading List Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    """
    def validate_ListName(self, ListName):
        readinglist = Lists.query.filter_by(ListName=ListName.data)
        if readinglist:
            raise ValidationError(' %s alredy have this list created.'%(current_user.name))
       """     

def publisher_query():
    return Publisher.query

def category_query():
    return Category.query

class Add_Book(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    year = StringField('Year Published', validators=[DataRequired()])
    book_cover = StringField('URL link for book cover picture', validators=[DataRequired()])
    description = TextAreaField('Book description ', validators=[DataRequired()])
    publisher = SelectField('Publisher',  choices=[])
    category = SelectField('Category', choices=[])
    submit = SubmitField('Add')
    """
    def validate_Name(self, Name):
        publisher = Publisher.query.filter_by(Name=Name.data)
        if publisher:
            raise ValidationError('The Publisher alredy exists.')
     """   