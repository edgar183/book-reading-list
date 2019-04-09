from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from app.models import Book, Publisher, Category, Author, Lists
from wtforms_alchemy.fields import QuerySelectField

def choice_publisher():
    return Publisher.query.all()
    
def choice_category():
    return Category.query.all()
    
def choice_author():
    return Author.query.all()

class Add_Book(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    year = StringField('Year Published', validators=[DataRequired()])
    book_cover = StringField('URL link for book cover picture', validators=[DataRequired()])
    description = TextAreaField('Book description ', validators=[DataRequired()])
    publisher = QuerySelectField(query_factory=choice_publisher, allow_blank=True,get_label='Name')
    category = QuerySelectField(query_factory=choice_category, allow_blank=True,get_label='Name')
    author = QuerySelectField(query_factory=choice_author, allow_blank=True,get_label='full_name')
    submit = SubmitField('Add')
    
def choice_lists():
    return Lists.query.all()

class Add_book_to_readinglit(FlaskForm):
    lists = QuerySelectField(query_factory=choice_lists, allow_blank=True,get_label='ListName')
    submit = SubmitField('Add')