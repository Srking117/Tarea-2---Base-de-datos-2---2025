"""Controller for Book endpoints including REQ 6 features."""

from typing import Sequence

from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.exceptions import HTTPException
from litestar.dto import DTOData
from advanced_alchemy.exceptions import NotFoundError, DuplicateKeyError

from app.repositories.book import BookRepository, provide_book_repo
from app.dtos.book import BookCreateDTO, BookReadDTO, BookUpdateDTO
from app.models import Book


class BookController(Controller):
    path = "/books"
    tags = ["books"]
    return_dto = BookReadDTO

    dependencies = {"books_repo": Provide(provide_book_repo)}

    

    @get("/")
    async def list_books(self, books_repo: BookRepository) -> Sequence[Book]:
        return books_repo.list()

    @get("/{book_id:int}")
    async def get_book(self, book_id: int, books_repo: BookRepository) -> Book:
        try:
            return books_repo.get(book_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail="Libro no encontrado.")

    @post("/", dto=BookCreateDTO)
    async def create_book(self, data: DTOData[Book], books_repo: BookRepository) -> Book:
        try:
            builtins = data.as_builtins()

            
            stock = builtins.get("stock")
            if stock is not None and stock <= 0:
                raise HTTPException(status_code=400, detail="El stock debe ser mayor a 0 al crear.")

            language = builtins.get("language")
            if language and language not in {"es", "en", "fr", "de", "it", "pt"}:
                raise HTTPException(status_code=400, detail="Idioma inválido.")

            return books_repo.add(Book(**builtins))
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail="El ISBN o título ya existe.")

    @patch("/{book_id:int}", dto=BookUpdateDTO)
    async def update_book(self, book_id: int, data: DTOData[Book], books_repo: BookRepository) -> Book:
        try:
            builtins = data.as_builtins()

           
            if "stock" in builtins and builtins["stock"] < 0:
                raise HTTPException(status_code=400, detail="El stock no puede ser negativo al actualizar.")

            if "language" in builtins and builtins["language"] not in {"es", "en", "fr", "de", "it", "pt"}:
                raise HTTPException(status_code=400, detail="Idioma inválido.")

            book, _ = books_repo.get_and_update(
                match_fields="id",
                id=book_id,
                **builtins
            )
            return book
        except NotFoundError:
            raise HTTPException(status_code=404, detail="Libro no encontrado.")

    @delete("/{book_id:int}")
    async def delete_book(self, book_id: int, books_repo: BookRepository) -> None:
        try:
            books_repo.delete(book_id)
        except NotFoundError:
            raise HTTPException(status_code=404, detail="Libro no encontrado.")

    

    @get("/available")
    async def list_available_books(self, books_repo: BookRepository) -> Sequence[Book]:
        return books_repo.get_available_books()

    
    @get("/category/{category_id:int}")
    async def list_by_category(self, category_id: int, books_repo: BookRepository) -> Sequence[Book]:
        return books_repo.find_by_category(category_id)

   
    @get("/top-reviewed")
    async def top_reviewed_books(self, limit: int = 10, books_repo: BookRepository = None) -> Sequence[Book]:
        return books_repo.get_most_reviewed_books(limit=limit)

    
    @patch("/{book_id:int}/stock")
    async def patch_book_stock(self, book_id: int, quantity: int, books_repo: BookRepository) -> Book:
        try:
            return books_repo.update_stock(book_id, quantity)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @get("/search")
    async def search_books_by_author(self, author: str, books_repo: BookRepository) -> Sequence[Book]:
        return books_repo.search_by_author(author)
