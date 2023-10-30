from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request 
import requests


# create app
app = Flask(__name__)

# set up data base and connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# class of data being stored
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)

    # repr displayed on get request
    def __repr__(self):
        return f"{self.name} by {self.author} published under {self.publisher}"


# web home
@app.route('/')
def index():
    return 'Hello!'

# home/books
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        drink_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher, 'isbn-13': book.id}
        output.append(drink_data)
    
    return {"books": output}

# post books
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['id'], book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}
 
# home/books/id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

# delete 
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Yeetus Deletus"}

# update book name
@app.route('/books/<id>', methods=['PUT'])
def update_title(id):
    book = Book.query.get(id)
    book_name = request.json['book_name']
    book.book_name = book_name
    db.session.commit()
    return {"book_name": book.book_name}
