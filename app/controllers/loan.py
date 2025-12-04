"""Controller for Loan endpoints (REQ 6 COMPLETO)."""

from typing import Sequence
from datetime import date, timedelta

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.loan import LoanCreateDTO, LoanReadDTO, LoanUpdateDTO
from app.models import Loan, Book, User
from app.repositories.loan import LoanRepository, provide_loan_repo
from app.repositories.book import BookRepository, provide_book_repo
from app.repositories.user import UserRepository, provide_user_repo


class LoanController(Controller):
    """Controller for loan management operations."""

    path = "/loans"
    tags = ["loans"]
    return_dto = LoanReadDTO

    dependencies = {
        "loans_repo": Provide(provide_loan_repo),
        "books_repo": Provide(provide_book_repo),
        "users_repo": Provide(provide_user_repo),
    }

    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

  

    @get("/")
    async def list_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        return loans_repo.list()

  

    @get("/{id:int}")
    async def get_loan(self, id: int, loans_repo: LoanRepository) -> Loan:
        return loans_repo.get(id)

   
    @post("/", dto=LoanCreateDTO)
    async def create_loan(
        self,
        data: DTOData[Loan],
        loans_repo: LoanRepository,
        books_repo: BookRepository,
        users_repo: UserRepository,
    ) -> Loan:
        builtins = data.as_builtins()

        user = users_repo.get(builtins["user_id"]) if "user_id" in builtins else None
        if not user:
            raise HTTPException(status_code=400, detail="Usuario no encontrado.")

        book = books_repo.get(builtins["book_id"]) if "book_id" in builtins else None
        if not book:
            raise HTTPException(status_code=400, detail="Libro no encontrado.")

        if book.stock is None or book.stock <= 0:
            raise HTTPException(status_code=400, detail="No hay stock disponible para este libro.")

        
        books_repo.update_stock(book.id, -1)

        loan_dt = builtins.get("loan_dt") or date.today()
        due_date = loan_dt + timedelta(days=14)

        builtins["loan_dt"] = loan_dt
        builtins["due_date"] = due_date

        return loans_repo.add(Loan(**builtins))

   
    @patch("/{id:int}", dto=LoanUpdateDTO)
    async def update_loan_status(self, id: int, data: DTOData[Loan], loans_repo: LoanRepository) -> Loan:
        loan, _ = loans_repo.get_and_update(match_fields="id", id=id, **data.as_builtins())
        return loan

    
    @post("/{id:int}/return")
    async def return_loan(self, id: int, loans_repo: LoanRepository) -> Loan:
        try:
            loan = loans_repo.return_book(id)
            return loan
        except ValueError:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")


    @get("/overdue")
    async def overdue_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        return loans_repo.get_overdue_loans()

    
    @get("/user/{user_id:int}")
    async def user_loan_history(self, user_id: int, loans_repo: LoanRepository) -> Sequence[Loan]:
        return loans_repo.get_user_loan_history(user_id)
