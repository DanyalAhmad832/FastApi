from fastapi import FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "Computer Science 1", "codingwithdanyal",'A very nice book!', 1 ),
    Book(2, "Computer Science 2", "codingwithdanyal",'A very nice book!', 2 ),
    Book(3, "Computer Science 3", "codingwithdanyal",'A very nice book!', 3 ),
    Book(4, "Computer Science 4", "codingwithdanyal",'A very nice book!', 4 ),
    Book(5, "Computer Science 5", "codingwithdanyal",'A very nice book!', 5 ),
    Book(6, "Computer Science 6", "codingwithdanyal",'A very nice book!', 5 )

]

@app.get("/books")
async def read_books():
    return BOOKS

