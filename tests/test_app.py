from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Author, Book
from datetime import date, timedelta

class TestBase(TestCase):
    def create_app(self): # Sets test configuration
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "test secret key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app
    
    def setUp(self): # Run before each test
        db.create_all()
        sample_author = Author(author_name = "Sample Author")
        sample_book = Book(title = "Sample Book", price = 10.00, publish_date = date.today(), author_id = 1)
        db.session.add(sample_author)
        db.session.add(sample_book)
        db.session.commit()
    
    def tearDown(self): # Run after each test
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample Book', response.data)

class TestAddBook(TestBase):
    def test_add_get(self):
        response = self.client.get(url_for('add_book'))
        self.assert200(response)
        self.assertIn(b'Book title', response.data)
    
    def test_add_post(self):
        response = self.client.post(
            url_for('add_book'),
            data = dict(title="Sample book 2", price = 12.00, publish_date = date.today(), author_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample book 2', response.data)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assert200(response)
        self.assertIn(b'Book title', response.data)

class TestDelete(TestBase):
    def test_delete_book(self):
        response = self.client.get(url_for("delete_book", i=1), follow_redirects=True)
        self.assertNotIn(b"Run unit test", response.data)

class TestAddAuthor(TestBase):
    def test_add_author_get(self):
        response = self.client.get(url_for('add_author'))
        self.assert200(response)
        self.assertIn(b'name', response.data)
    def test_add_author_post(self):
        response = self.client.post(
            url_for('add_author'),
            data = dict(author_name="Sample Author"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample Author', response.data)
    
    def test_update_post(self):
        response = self.client.post(
            url_for('update', id = 1),
            data = dict(title="Sample book 3", price = 12.00, publish_date = date.today(), author_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample book 3', response.data)
