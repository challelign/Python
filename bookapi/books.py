from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


BOOKS = [
    {"title": "Alexd", "author": "Alex Mackalister", "category": "Footballer"},
    {"title": "The Silent", "author": "Alex Michaelides", "category": "Thriller"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help"},
    {"title": "Educated", "author": "Tara Westover", "category": "Memoir"},
    {"title": "The Midnight Library", "author": "Matt Haig", "category": "Fiction"},
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "category": "History",
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Philosophical Fiction",
    },
    {"title": "Becoming", "author": "Michelle Obama", "category": "Biography"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "category": "Self-Help",
    },
    {"title": "To Kill a Mockingbird", "author": "Lee", "category": "Classic"},
]


@app.get("/")
async def get_root():
    print("Root endpoint called")
    return {"message": "Hello World"}


@app.get("/books")
async def get_books():
    return {"BOOKS": BOOKS}


# @app.get("/books/mybook")
# async def get_mybook():
#   return  {"book_title": "My Book"}


# http://127.0.0.1:8000/books/Alex


@app.get("/books/{book_title}")
async def get_single_book(book_title: str):
    for book in BOOKS:
        if book["title"] == book_title:
            # if book.get("title").casefold() == book_title.casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# Query Parameters

# http://127.0.0.1:8000/books/?category=Footballer


@app.get("/books/")
async def get_mybook_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# query and path parameter (book_author)
# http://127.0.0.1:8000/books/Lee/?category=Classic


@app.get("/books/{book_author}/")
async def get_mybook_by_author(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            # Used book.get("author", "") to avoid NoneType errors if keys are missing.optional you can remove
            book.get("author", "").casefold() == book_author.casefold()
            and book.get("category", "").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"new_book": new_book, "ALL_BOOKS": BOOKS}


class Book(BaseModel):
    title: str
    author: str
    category: str


@app.put("/books/update_book")
async def update_book(updated_book: Book = Body(...)):
    for index, book in enumerate(BOOKS):
        if (
            book["title"].casefold() == updated_book.title.casefold()
            or book["category"].casefold() == updated_book.category.casefold()
            or book["author"].casefold() == updated_book.author.casefold()
        ):
            BOOKS[index] = updated_book.dict()
            return {"updated_book": BOOKS[index], "ALL_BOOKS": BOOKS}

    raise HTTPException(status_code=404, detail="Book not found")


# Not Working
# @app.put("/books/update_book2")
# async def update_book(updated_book=Body()):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
#             BOOKS[i] = updated_book


@app.put("/books/update_book/{book_title}")
async def update_book(book_title: str, updated_book=Body()):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book.update(updated_book)
            return {"updated_book": book, "ALL_BOOKS": BOOKS}
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
