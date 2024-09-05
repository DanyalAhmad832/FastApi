from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "History"},
    {"title": "Title Three", "author": "Author Three", "category": "Math"},
    {"title": "Title Four", "author": "Author Four", "category": "Language"},
    {"title": "Title Five", "author": "Author Five", "category": "Science"},
    {"title": "Title Six", "author": "Author One", "category": "History"},
    {"title": "Title Seven", "author": "Author Seven", "category": "Language"},
    {"title": "Title Eight", "author": "Author Eight", "category": "Math"}
]

########################################################################################################################
                                        #GET OR READ#
########################################################################################################################

@app.get("/books")
async def read_all_books():
    return BOOKS


"""Below method refers to path parameters in FastApi"""
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


"""Below method refers to Query parameters in FastApi"""
@app.get("/books/")
async def read_category_by_query(category: str):
    same_category_books = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            same_category_books.append(book)
    return same_category_books


"""Below method refers to Path Parameter and Query parameters in FastApi"""
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    same_category_books = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get(
                "category").casefold() == category.casefold():
            same_category_books.append(book)
    return same_category_books


########################################################################################################################
                                               #POST OR CREATE#
########################################################################################################################

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully!"}


########################################################################################################################
                                               #PUT OR UPDATE#
########################################################################################################################
@app.put("/books/update_book")
async def update_book(new_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == new_book.get("title").casefold():
            BOOKS[i].update(new_book)


########################################################################################################################
                                               #DELTETE#
########################################################################################################################
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

########################################################################################################################
                                               #ASSIGNMET#
########################################################################################################################
@app.get("/books/byauthor/{book_author}")
async def read_book_by_author(book_author: str):
    same_author_books = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            same_author_books.append(book)
    return same_author_books
