from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_login import current_user
from app.models import Lists

class Add_Readinglist(FlaskForm):
    ListName = StringField('Reading List Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_ListName(self, ListName):
        readinglist = Lists.query.filter_by(ListName=ListName.data).first()
        if readinglist:
            raise ValidationError(' %s alredy have this list created.'%(current_user.name))

