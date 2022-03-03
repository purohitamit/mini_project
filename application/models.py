from application import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author_name = db.Column(db.String(30))
    books = db.relationship('Book', backref='author')
    def __str__(self):
        return f"{self.author_name}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30))
    price = db.Column(db.Float)
    publish_date = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable = False)
    def __str__(self):
        return f"{self.title}"

