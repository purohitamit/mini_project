from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Author, Book
from application.forms import AuthorForm, BookForm

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books = books)

@app.route('/search/book=<keyword>')
def search_book(keyword):
    data = db.session.execute(f"SELECT * FROM Book WHERE title LIKE '%{keyword}%'")
    data = list(data)
    num_results = len(data)
    return render_template('search.html', res = [str(res) for res in data], n = num_results)

@app.route('/search/author=<keyword>')
def search_author(keyword):
    data = db.session.execute(f"SELECT * FROM Author WHERE author_name LIKE '%{keyword}%'")
    data = list(data)
    num_results = len(data)
    return render_template('search.html', res = [str(res) for res in data], n = num_results)

@app.route('/add/author', methods=['GET', 'POST'])
def add_author():
    #message = None
    form = AuthorForm()
    if request.method == 'POST':
        # if not form.validate_on_submit():
        #     message = ""
        #     for field in ['name', 'due']:
        #         try:
        #             err = eval(f"form.{field}.errors[-1]")
        #         except IndexError:
        #             err = ""
        #         message += err + ", "
        #     return render_template('add_proj.html', form = form, message = message)
        name = form.name.data
        new_author= Author(author_name = name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('author_form.html', form = form)

@app.route('/add/book', methods=['GET', 'POST'])
def add_book():
    message = None
    authors = Author.query.all()
    form = BookForm()
    form.author_id.choices.extend([(author.id, str(author)) for author in authors])
    if request.method == 'POST':
        title = form.title.data
        price = form.price.data
        publish_date = form.publish_date.data
        author_id = int(form.author_id.data)
        new_book = Book(title = title, price = price, publish_date = publish_date,  author_id = author_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('book_form.html', form = form, ptitle = "Add Book", message = message)



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = Book.query.get(id)
    authors = Author.query.all()
    form = BookForm()
    form.author_id.choices.extend([(author.id, str(author)) for author in authors])
    if request.method == 'POST':
        book.title = form.title.data
        book.price = form.price.data
        book.publish_date = form.publish_date.data
        book.author_id = int(form.author_id.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('book_form.html', form = form, ptitle = "Update Book")

@app.route('/delete/book/<int:i>')
def delete_book(i):
    book = Book.query.get(i)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


