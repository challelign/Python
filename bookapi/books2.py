# from books_data import BOOKS
from typing import Optional

from fastapi import Body, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

from bookapi.books_data import BOOKS, Book

app = FastAPI()


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="The ID of the book is not needed. If not provided, it will be auto-generated.",
    )
    title: str = Field(..., min_length=3, max_length=50)
    author: str = Field(..., min_length=2, max_length=15)
    description: str = Field(
        ...,  # ellipsis (...) when the field is required and doesn't have a default:
        min_length=10,
        max_length=100,
        description="Description of the book",
    )
    rating: int = Field(
        ...,
        gt=0,
        lt=6,
        description="Rating of the book between 1 and 5",
    )
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A story about the decline of the American Dream.",
                "rating": 4,
            }
        }
    }


@app.get("/")
async def get_root():
    print("Root endpoint called")
    return {"message": "Hello World"}


# Path parameters
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(..., gt=0)):
    print("book_id", book_id)
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.post("/create-book", status_code=status.HTTP_200_OK)
async def create_book(book_request=Body()):
    print("book_request", book_request)
    BOOKS.append(book_request)
    return book_request


# Using base model for request body
@app.post("/create-book-modal", status_code=status.HTTP_201_CREATED)
async def create_book_modal(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_by_id(new_book))
    # BOOKS.append(book_request)
    # return book_request
    return {"message": "Book created successfully", "book": new_book}


def find_book_by_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1  # BOOKS[-1]: Gets the last book in the BOOKS list.
    else:
        book.id = 1
    return book


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(..., gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return
