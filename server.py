from fastapi import FastAPI, HTTPException, Body, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime
import LinkedList as ll
import HashTable as ht
import BinarySearchTree as bst
import random as rand
import Queue as q
import Stack as s
from sqlalchemy import create_engine, event, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

app = FastAPI()

DATABASE_URL = "sqlite:///author_book.file"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(50))
    lname = Column(String(50))
    country = Column(String(50))
    book = relationship("Book", cascade="all, delete")

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    total_pages = Column(Integer)
    rating = Column(Float)
    isbn = Column(String(20))
    published_date = Column(Date)
    preface = Column(String(200))
    date_created = Column(Date)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

class AuthorCreate(BaseModel):
    fname: str
    lname: str
    country: str

class BookCreate(BaseModel):
    title: str
    total_pages: int
    rating: float
    isbn: str
    published_date: datetime
    preface: str

@app.post("/author")
def create_new_author(author: AuthorCreate, db: Session = Depends(SessionLocal)):
    new_author = Author(
        fname=author.fname,
        lname=author.lname,
        country=author.country,
    )
    db.add(new_author)
    db.commit()
    return {"message": "New Author Added to the Database"}

@app.post("/book/{input_author_id}")
def add_new_book(input_author_id: int, book: BookCreate, db: Session = Depends(SessionLocal)):
    check_author = db.query(Author).filter_by(id=input_author_id).first()
    if not check_author:
        raise HTTPException(status_code=400, detail="Author does not exist")
    
    new_book = Book(
        title=book.title,
        total_pages=book.total_pages,
        rating=book.rating,
        isbn=book.isbn,
        published_date=book.published_date,
        preface=book.preface,
        date_created=datetime.now(),
        author_id=input_author_id
    )
    db.add(new_book)
    db.commit()
    return {"message": "New Book Added to the Database"}

@app.get("/author/author_descending_order")
def get_author_descending_order(db: Session = Depends(SessionLocal)):
    all_authors = db.query(Author).all()
    ll_all_authors = ll.LinkedList()
    for eachAuthor in all_authors:
        ll_all_authors.beginning_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    return ll_all_authors.convert_ll_to_list()

@app.get("/author/authors_ascending_order")
def get_all_authors_ascending(db: Session = Depends(SessionLocal)):
    all_authors = db.query(Author).all()
    ll_all_authors = ll.LinkedList()
    for eachAuthor in all_authors:
        ll_all_authors.end_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    return ll_all_authors.convert_ll_to_list()

@app.get("/author/{input_author_id}")
def get_one_author(input_author_id: int, db: Session = Depends(SessionLocal)):
    all_authors = db.query(Author).all()
    ll_all_authors = ll.LinkedList()
    for eachAuthor in all_authors:
        ll_all_authors.beginning_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    output_details = ll_all_authors.get_author_by_id(input_author_id)
    if not output_details:
        raise HTTPException(status_code=404, detail="Author not found")
    return output_details

@app.delete("/author/{input_author_id}")
def delete_author_id(input_author_id: int, db: Session = Depends(SessionLocal)):
    author = db.query(Author).filter_by(id=input_author_id).first()
    if not author:
        raise HTTPException(status_code=400, detail=f"Author ID {input_author_id} does not exist")
    db.delete(author)
    db.commit()
    return {"message": f"Author ID {input_author_id} with Name {author.fname} {author.lname} deleted successfully"}

@app.get("/book/{book_id}")
def get_one_book(book_id: int, db: Session = Depends(SessionLocal)):
    all_books = db.query(Book).all()
    rand.shuffle(all_books)
    binary_search_tree = bst.BinarySearchTree()
    for eachBook in all_books:
        binary_search_tree.insert({
            "id": eachBook.id,
            "title": eachBook.title,
            "total_pages": eachBook.total_pages,
            "rating": eachBook.rating,
            "isbn": eachBook.isbn,
            "published_date": eachBook.published_date,
            "date_created": eachBook.date_created,
            "preface": eachBook.preface,
            "author_id": eachBook.author_id,
        })
    book = binary_search_tree.search(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/book/numeric_preface")
def get_numeric_of_book_preface(db: Session = Depends(SessionLocal)):
    all_books = db.query(Book).all()
    queue = q.Queue()
    for eachBook in all_books:
        queue.enqueue(eachBook)
    output = []
    for _ in range(len(all_books)):
        popped_element = queue.dequeue()
        counter = sum(ord(character) for character in popped_element.data.preface)
        output.append(
            {
                "id": popped_element.data.id,
                "title": popped_element.data.title,
                "preface_ascii": counter,
                "preface": popped_element.data.preface,
            }
        )
    return output

@app.delete("/book/delete_last_5")
def delete_last_5(db: Session = Depends(SessionLocal)):
    all_books = db.query(Book).all()
    stack = s.Stack()
    for eachBook in all_books:
        stack.push(eachBook)
    for _ in range(5):
        popped_element = stack.pop()
        if not popped_element:
            return {"message": "Database is empty. Few elements were removed"}
        db.delete(popped_element.data)
        db.commit()
    return {"message": "Last 5 books deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
