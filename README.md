# Whimsy

A personal book library manager for the terminal, with a built-in analysis section that uses pandas and matplotlib.

## Features

Library:
- Show, add, remove and find books
- Sort by title, author, genre, rating, year or pages
- Find books by one or more authors
- Show highest-rated books, or the top N
- Save to and load from `books.json`

Analysis:
- Average rating, counts by any column, average rating and pages by genre
- Top-rated books and book age
- Filter with your own column, operator and value (for example `rating >= 9`)
- Charts: books by genre, books by rating, average rating by genre, books published by year

## Run it

Needs Python 3.8 or newer.

```
pip install -r requirements.txt
python main.py
```

`books.json` is included as sample data. Choose "Load books" in the menu to use it.

## Project layout

| File | What it does |
| --- | --- |
| `main.py` | Menus and program loop |
| `models.py` | The `Book` dataclass |
| `books.py` | Starting list of books |
| `functions.py` | Library actions (add, remove, sort, search) |
| `storage.py` | Saving and loading JSON |
| `analysis.py` | pandas summaries and matplotlib charts |

## What I practised

- Splitting a program across several modules
- Dataclasses
- pandas: `groupby`, `value_counts`, boolean filtering
- matplotlib bar and line charts
- JSON persistence with `pathlib`
