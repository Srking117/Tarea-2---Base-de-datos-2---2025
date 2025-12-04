"""Repository for Book database operations (REQ 6)."""

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from advanced_alchemy.repository import SQLAlchemySyncRepository

from app.models import Book, Category, Review, book_categories


class BookRepository(SQLAlchemySyncRepository[Book]):
    model_type = Book

    
    def get_available_books(self):
        return self.session.scalars(
            select(Book).where(Book.stock > 0)
        ).all()

    
    def find_by_category(self, category_id: int):
        return self.session.scalars(
            select(Book)
            .join(book_categories, Book.id == book_categories.c.book_id)
            .where(book_categories.c.category_id == category_id)
        ).all()

    
    def get_most_reviewed_books(self, limit: int = 10):
        return self.session.scalars(
            select(Book)
            .join(Review, Review.book_id == Book.id)
            .group_by(Book.id)
            .order_by(func.count(Review.id).desc())
            .limit(limit)
        ).all()

    
    def update_stock(self, book_id: int, quantity: int) -> Book:
        book = self.session.get(Book, book_id)
        if not book:
            raise ValueError("Libro no encontrado.")

        new_stock = book.stock + quantity
        if new_stock < 0:
            raise ValueError("La operación dejaría el stock negativo.")

        book.stock = new_stock

        self.session.add(book)
        self.session.commit()

        return book

    
    def search_by_author(self, author_name: str):
        return self.session.scalars(
            select(Book).where(Book.author.ilike(f"%{author_name}%"))
        ).all()


async def provide_book_repo(db_session: Session) -> BookRepository:
    return BookRepository(session=db_session, auto_commit=True)
