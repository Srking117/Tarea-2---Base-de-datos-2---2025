from typing import Sequence
from datetime import date

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.dtos.review import ReviewReadDTO, ReviewCreateDTO, ReviewUpdateDTO
from app.models import Review
from app.repositories.review import ReviewRepository, provide_review_repo
from app.controllers import duplicate_error_handler, not_found_error_handler


class ReviewController(Controller):
    path = "/reviews"
    tags = ["reviews"]
    return_dto = ReviewReadDTO

    dependencies = {
        "review_repo": Provide(provide_review_repo),
    }

    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_reviews(self, review_repo: ReviewRepository) -> Sequence[Review]:
        return review_repo.list()

    @get("/{id:int}")
    async def get_review(self, id: int, review_repo: ReviewRepository) -> Review:
        return review_repo.get(id)

    @post("/", dto=ReviewCreateDTO)
    async def create_review(
        self,
        data: DTOData[Review],
        review_repo: ReviewRepository,
    ) -> Review:

        builtins = data.as_builtins()

        rating = builtins["rating"]
        user_id = builtins["user_id"]
        book_id = builtins["book_id"]

        
        if rating < 1 or rating > 5:
            raise HTTPException(
                status_code=400,
                detail="El rating debe estar entre 1 y 5.",
            )

        
        existing_reviews = review_repo.list(
            Review.user_id == user_id,
            Review.book_id == book_id,
        )

        if len(existing_reviews) >= 3:
            raise HTTPException(
                status_code=400,
                detail="El usuario ya tiene 3 reseñas para este libro.",
            )

        
        builtins["review_date"] = date.today()

        return review_repo.add(Review(**builtins))

    @patch("/{id:int}", dto=ReviewUpdateDTO)
    async def update_review(
        self,
        id: int,
        data: DTOData[Review],
        review_repo: ReviewRepository,
    ) -> Review:
        review, _ = review_repo.get_and_update(
            match_fields="id",
            id=id,
            **data.as_builtins()
        )
        return review

    @delete("/{id:int}")
    async def delete_review(self, id: int, review_repo: ReviewRepository) -> None:
        review_repo.delete(id)
