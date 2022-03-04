from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, FloatField
from wtforms.validators import DataRequired, ValidationError
from datetime import date
from application.models import Author, Book

class AuthorForm(FlaskForm):
    name = StringField("Author Name: ", validators=[DataRequired()])
    submit = SubmitField("Add Author", validators=[DataRequired()])

class BookForm(FlaskForm):
    title = StringField("Book title: ", validators=[DataRequired()])
    price = FloatField("Price: ", validators=[DataRequired()])
    publish_date = DateField("Published Date", validators=[DataRequired()])
    author_id = SelectField("Author of the book", validators=[DataRequired()], choices=[])
    submit = SubmitField("Add Book")

