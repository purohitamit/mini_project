from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, FloatField
from wtforms.validators import DataRequired, ValidationError
from datetime import date
from application.models import Author, Book

# class NameCheck():
#     def __init__(self, message = "Author name already exists"):
#         self.message = message
    
#     def __call__(self, form, field):
#         if field.data in [author.author_name for author in Author.query.all()]:
#             raise(ValidationError(self.message))

# class DateCheck():
#     def __init__(self, message="Publication date can not be in future: Please enter a valid date"):
#         self.message = message
    
#     def __call__(self, form, field):
#         if field.data > date.today():
#             raise ValidationError(self.message)

class AuthorForm(FlaskForm):
    #name = StringField("Author Name: ", validators=[NameCheck()])
    name = StringField("Author Name: ")
    submit = SubmitField("Add Author")

class BookForm(FlaskForm):
    #title = StringField("Book title: ", validators=[DataRequired()])
    title = StringField("Book title: ")
    price = FloatField("Price: ")
    #publish_date = DateField("Published Date", validators = [DateCheck()])
    publish_date = DateField("Published Date")
    author_id = SelectField("Author of the book", choices=[])
    submit = SubmitField("Add Book")

