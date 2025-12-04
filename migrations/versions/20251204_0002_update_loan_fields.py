"""Add due_date, fine_amount and status to loans

Revision ID: 20251204_loan_update
Revises: 20251204_user_update
Create Date: 2025-12-04
"""
from alembic import op
import sqlalchemy as sa



revision = "20251204_loan_update"
down_revision = "20251204_user_update"
branch_labels = None
depends_on = None


def upgrade():
    
    op.add_column("loans", sa.Column("due_date", sa.Date(), nullable=True))

    
    op.add_column("loans", sa.Column("fine_amount", sa.Numeric(10,2), nullable=False, server_default="0.00"))

    
    loan_status = sa.Enum('ACTIVE', 'RETURNED', 'OVERDUE', name='loanstatus')
    loan_status.create(op.get_bind(), checkfirst=True)
    op.add_column("loans", sa.Column("status", loan_status, nullable=False, server_default='ACTIVE'))

    
    op.execute("UPDATE loans SET due_date = loan_dt + INTERVAL '14 days' WHERE due_date IS NULL")

    
    op.alter_column("loans", "due_date", nullable=False)


def downgrade():
    op.drop_column("loans", "status")
    sa.Enum(name='loanstatus').drop(op.get_bind(), checkfirst=True)
    op.drop_column("loans", "fine_amount")
    op.drop_column("loans", "due_date")
