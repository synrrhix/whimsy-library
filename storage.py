from pathlib import Path
import json
from models import Book

SAVE_FILE = Path("books.json")

def save_books(books):
    book_data = [
        {
    'title': book.title,
    'author': book.author,
    'genre': book.genre,
    'rating': book.rating,
    'year': book.year,
    'pages': book.pages
        }
        for book in books
    ]

    with SAVE_FILE.open("w") as file:
        json.dump(book_data, file, indent=4)

def load_books():
    if not SAVE_FILE.exists():
        return None
    with SAVE_FILE.open("r") as file:
        book_data = json.load(file)

        books = [Book(book["title"], book["author"], book["genre"], book["rating"], book["year"], book["pages"]) for book in book_data]
        return books