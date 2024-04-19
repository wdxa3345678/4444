
from fastapi import FastAPI, Body
from pydantic import BaseModel


app=FastAPI()
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id : int
    title : str
    author : str
    description : str
    rating : int


BOOKS=[
    Book(1,"Computer secience","code with bill","very nice book",5),
    Book(2,"history","history with bill","very good book",4),
    Book(3,"Computer math","math with bill","very bad book",3),
    Book(4,"Computer music","music with bill","very boring book",2),
    Book(5,"Computer health","code with bill","very heealth book",4),
]

@app.get("/books/")
async def read_books():
    return BOOKS




@app.post("/create_book")
async def create_book(book_request:BookRequest):
    print(type(book_request))
    new_book=Book(**book_request.dict())
    BOOKS.append(new_book)