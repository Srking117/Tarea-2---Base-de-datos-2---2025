from typing import Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData

from app.dtos.category import (
    CategoryReadDTO,
    CategoryCreateDTO,
    CategoryUpdateDTO,
)
from app.models import Category
from app.repositories.category import CategoryRepository, provide_category_repo
from app.controllers import duplicate_error_handler, not_found_error_handler


class CategoryController(Controller):
    path = "/categories"
    tags = ["categories"]
    return_dto = CategoryReadDTO

    dependencies = {"category_repo": Provide(provide_category_repo)}

    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_categories(self, category_repo: CategoryRepository) -> Sequence[Category]:
        return category_repo.list()

    @get("/{id:int}")
    async def get_category(self, id: int, category_repo: CategoryRepository) -> Category:
        return category_repo.get(id)

    @post("/", dto=CategoryCreateDTO)
    async def create_category(
        self,
        data: DTOData[Category],
        category_repo: CategoryRepository,
    ) -> Category:
        return category_repo.add(data.create_instance())

    @patch("/{id:int}", dto=CategoryUpdateDTO)
    async def update_category(
        self,
        id: int,
        data: DTOData[Category],
        category_repo: CategoryRepository,
    ) -> Category:
        category, _ = category_repo.get_and_update(
            match_fields="id",
            id=id,
            **data.as_builtins()
        )
        return category

    @delete("/{id:int}")
    async def delete_category(self, id: int, category_repo: CategoryRepository) -> None:
        category_repo.delete(id)
