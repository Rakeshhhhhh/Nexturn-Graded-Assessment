from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.models import Book
from app.extensions import db  # Import db here

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@main_routes.route('/about')
def about():
    return render_template('about.html')

@main_routes.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    published_year = request.form.get('published_year')
    genre = request.form.get('genre')

    if not title or not author or not published_year or not genre:
        return jsonify({'error': 'All fields are required!'})

    book = Book(title=title, author=author, published_year=int(published_year), genre=genre)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('main_routes.home'))

@main_routes.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main_routes.home'))
