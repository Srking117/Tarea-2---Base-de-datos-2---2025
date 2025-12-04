"""Data Transfer Objects for Book endpoints."""

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Book


class BookReadDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(
        exclude={"loans", "reviews"},
    )


class BookCreateDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews"},
    )


class BookUpdateDTO(SQLAlchemyDTO[Book]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at", "loans", "reviews"},
        partial=True,
    )
