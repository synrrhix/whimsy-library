import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def create_dataframe(books):
    book_data = [
        {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "rating": book.rating,
            "year": book.year,
            "pages": book.pages
        }
        for book in books
    ]

    return pd.DataFrame(book_data)

def count_values(df):
    valid_columns = ['title', 'author', 'genre', 'rating', 'year', 'pages']
    choice = input("Count by: ").strip().lower()

    if choice not in valid_columns:
        print(f'{choice} is an invalid option.')
        return None

    return df[choice].value_counts()

def average_rating_by_genre(df):
    return df.groupby('genre')['rating'].mean()

def add_book_age(df):
    df['age'] = datetime.now().year - df['year']
    return df

def average_pages_by_genre(df):
    return df.groupby("genre")["pages"].mean().sort_values(ascending=False)

def top_rated_books(df):
    max_rating = df["rating"].max()
    return df[df["rating"] == max_rating]

def plot_genres(df):
    counts = df["genre"].value_counts().sort_values()

    plt.figure(figsize=(10, 6))
    plt.barh(counts.index, counts.values)
    plt.xlabel("Number of Books")
    plt.ylabel("Genre")
    plt.title("Books by Genre")
    plt.tight_layout()
    plt.show()

def plot_ratings(df):
    counts = df["rating"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Rating")
    plt.ylabel("Number of Books")
    plt.title("Books by Rating")
    plt.xticks(counts.index)
    plt.tight_layout()
    plt.show()

def average_rating_genre(df):
    averages = df.groupby('genre')['rating'].mean().sort_values()

    plt.figure(figsize=(10, 6))
    plt.barh(averages.index, averages.values)
    plt.xlabel("Average Rating")
    plt.ylabel("Genre")
    plt.title("Average Rating by Genre")
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()

def plot_books_by_year(df):
    counts = df['year'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    plt.plot(counts.index, counts.values, marker="o")
    plt.xlabel("Year")
    plt.ylabel("Number of Books")
    plt.title("Books Published by Year")
    plt.tight_layout()
    plt.show()

def filter_by_whatever(df):
    valid_columns = ['title', 'author', 'genre', 'rating', 'year', 'pages']
    choice = input("Filter by: ").strip().lower()

    if choice not in valid_columns:
        print("Invalid column.")
        return None

    valid_operators = ["==", "!=", ">", "<", ">=", "<="]
    operator = input("Operator: ").strip()

    if operator not in valid_operators:
        print("Invalid operator.")
        return None

    value = input("Value: ").strip()

    if choice in ['rating','year','pages']:
        value = float(value)

    operators = {
        "==": lambda column, value: column == value,
        "!=": lambda column, value: column != value,
        ">": lambda column, value: column > value,
        "<": lambda column, value: column < value,
        ">=": lambda column, value: column >= value,
        "<=": lambda column, value: column <= value
    }

    condition = operators[operator](df[choice], value)
    filtered = df[condition]

    if filtered.empty:
        return None
    return filtered