from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    genre: str
    rating: int
    year: int
    pages: int

    def __str__(self):
        return f"{self.title} by {self.author}\nGenre: {self.genre}\nRating: {self.rating}/10\nYear: {self.year}\nPages: {self.pages}"