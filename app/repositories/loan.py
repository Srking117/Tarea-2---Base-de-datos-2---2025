"""Repository for Loan database operations."""

from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal
from sqlalchemy import select, update

from app.models import Loan, Book

from app.models import Loan


class LoanRepository(SQLAlchemySyncRepository[Loan]):
    """Repository for loan database operations."""

    model_type = Loan

    def get_active_loans(self):
        return self.session.scalars(select(Loan).where(Loan.status == Loan.LoanStatus.ACTIVE)).all()

    def get_overdue_loans(self):
        
        today = date.today()
        overdue = self.session.scalars(
            select(Loan).where(Loan.due_date < today, Loan.status != Loan.LoanStatus.RETURNED)
        ).all()

        for ln in overdue:
            ln.status = Loan.LoanStatus.OVERDUE
            self.session.add(ln)

        self.session.commit()
        return overdue

    def calculate_fine(self, loan_id: int) -> Decimal:
        loan = self.session.get(Loan, loan_id)
        if not loan:
            raise ValueError("Loan not found")

        today = date.today()
        if loan.due_date is None:
            return Decimal("0.00")

        days_over = (today - loan.due_date).days
        if days_over <= 0:
            return Decimal("0.00")

        fine = Decimal(500) * Decimal(days_over)
        cap = Decimal(50000)
        if fine > cap:
            fine = cap

        return fine.quantize(Decimal("0.01"))

    def return_book(self, loan_id: int):
        loan = self.session.get(Loan, loan_id)
        if not loan:
            raise ValueError("Loan not found")

        if loan.status == Loan.LoanStatus.RETURNED:
            return loan

        loan.return_dt = date.today()
        loan.status = Loan.LoanStatus.RETURNED

        fine = self.calculate_fine(loan_id)
        loan.fine_amount = fine

        
        book = self.session.get(Book, loan.book_id)
        if book:
            book.stock = (book.stock or 0) + 1
            self.session.add(book)

        self.session.add(loan)
        self.session.commit()
        return loan

    def get_user_loan_history(self, user_id: int):
        return self.session.scalars(select(Loan).where(Loan.user_id == user_id)).all()


async def provide_loan_repo(db_session: Session) -> LoanRepository:
    """Provide loan repository instance with auto-commit."""
    return LoanRepository(session=db_session, auto_commit=True)
