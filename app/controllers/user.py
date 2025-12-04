"""Controller for User endpoints."""

from typing import Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException
import re

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.user import UserCreateDTO, UserReadDTO, UserUpdateDTO
from app.dtos.password_update import PasswordUpdateDTO
from app.models import User
from app.repositories.user import UserRepository, provide_user_repo, password_hasher


class UserController(Controller):
    """Controller for user management operations."""

    path = "/users"
    tags = ["users"]
    return_dto = UserReadDTO
    dependencies = {"users_repo": Provide(provide_user_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    

    @get("/")
    async def list_users(self, users_repo: UserRepository) -> Sequence[User]:
        return users_repo.list()

    

    @get("/{id:int}")
    async def get_user(self, id: int, users_repo: UserRepository) -> User:
        return users_repo.get(id)

    

    @post("/", dto=UserCreateDTO)
    async def create_user(
        self,
        data: DTOData[User],
        users_repo: UserRepository,
    ) -> User:
        """Create a new user with hashed password."""
        builtins = data.as_builtins()

        
        email = builtins.get("email")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=400, detail="Email inválido")

        return users_repo.add_with_hashed_password(data)

    

    @patch("/{id:int}", dto=UserUpdateDTO)
    async def update_user(
        self,
        id: int,
        data: DTOData[User],
        users_repo: UserRepository,
    ) -> User:
        """Update user fields (password excluded)."""
        builtins = data.as_builtins()

        
        email = builtins.get("email")
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=400, detail="Email inválido")

        user, _ = users_repo.get_and_update(
            match_fields="id",
            id=id,
            **builtins,
        )
        return user

    

    @post("/{id:int}/update-password", status_code=204)
    async def update_password(
        self,
        id: int,
        data: PasswordUpdateDTO,
        users_repo: UserRepository,
    ) -> None:
        """
        Update a user's password securely:
        - Verify current password (hashed)
        - Hash the new password
        - Save to database
        """
        user = users_repo.get(id)

        
        if not password_hasher.verify(data.current_password, user.password):
            raise HTTPException(
                detail="Contraseña incorrecta",
                status_code=401,
            )

       
        hashed = password_hasher.hash(data.new_password)
        user.password = hashed

        users_repo.update(user)

    

    @delete("/{id:int}")
    async def delete_user(self, id: int, users_repo: UserRepository) -> None:
        users_repo.delete(id)
