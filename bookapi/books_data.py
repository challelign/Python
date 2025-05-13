class Book:
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(
        1,
        "To Kill a Mockingbird",
        "Harper Lee",
        "A novel about the injustices of the American South.",
        5,
    ),
    Book(
        2,
        "1984",
        "George Orwell",
        "A dystopian novel about totalitarianism and surveillance.",
        5,
    ),
    Book(
        3,
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "A story about the decline of the American Dream.",
        4,
    ),
    Book(
        4,
        "Pride and Prejudice",
        "Jane Austen",
        "A romantic novel about social class and manners.",
        4,
    ),
    Book(
        5,
        "The Catcher in the Rye",
        "J.D. Salinger",
        "A novel about teenage rebellion and angst.",
        3,
    ),
]
