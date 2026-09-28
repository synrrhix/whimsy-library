from models import Book

def find_book(books, title):
    for book in books:
        if book.title == title:
            return book
    return None

def add_book(books):
    parts = input('Enter title, author, genre, rating, year, pages separated by commas, in that order: ').split(',')

    if len(parts) != 6:
        print('Enter exactly 6 values.')
        return

    try:
        book = Book(parts[0].strip().title(), parts[1].strip().title(), parts[2].strip().title(), int(parts[3]), int(parts[4]), int(parts[5]))
        books.append(book)
    except ValueError:
        print('Rating, year and pages must be numbers.')
        return

    books.append(book)
    print("Book added successfully!")

def remove_book(books, title):
    book = find_book(books, title)
    if book is None:
        print('Book not found. ')
        return
    books.remove(book)

def show_books(books):
    if not books:
        print('No books.')
        return

    print('===== YOUR LIBRARY =====')

    for book in books:
        book_details = [book.title, book.author, book.genre, str(book.rating), str(book.year), str(book.pages)]
        joined_book = " | ".join(book_details)
        print(f'{joined_book}\n')

def sort_books(books):
    sort_options = {
        'title': lambda b:b.title,
        'author': lambda b: b.author,
        'genre': lambda b: b.genre,
        'rating': lambda b: b.rating,
        'year': lambda b: b.year,
        'pages': lambda b: b.pages,
    }
    choice = input("Sort by: ").strip().lower()

    if choice not in sort_options:
        print(f'{choice} is an invalid option.')
        return None

    sorted_books = sorted(books,key=sort_options[choice])
    return sorted_books

def get_highest_rated_books(books):
    highest = [book for book in books if book.rating >= 8]
    return highest

def find_books_by_author(books):
    choice = [author.strip() for author in input('Enter author(s) to find books by: ').split(',')]
    by_author = [book.title for book in books if book.author in choice]

    if not by_author:
        return None

    return ', '.join(by_author)

def get_top_books(books, n):
    sorted_top = sorted(books, key=lambda book: book.rating, reverse=True)
    return sorted_top[:n]