from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from app.models import Book, Publisher, Category, Author
from wtforms_sqlalchemy.fields import QuerySelectField

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
    publisher = SelectField('Publisher', coerce=int)
    #publisher = QuerySelectField(query_factory=choice_publisher, allow_blank=True,get_label='Name')
    category = SelectField('Category', coerce=int)
    #category = QuerySelectField(query_factory=choice_category, allow_blank=True,get_label='Name')
    author = SelectField('Author', coerce=int)
    #author = QuerySelectField(query_factory=choice_author, allow_blank=True,get_label='full_name')
    submit = SubmitField('Add')
    


class Add_book_to_readinglit(FlaskForm):
    lists = SelectField('Reading Lists', coerce=int)
    submit = SubmitField('Add')