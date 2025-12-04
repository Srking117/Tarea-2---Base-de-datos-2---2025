"""Add email, phone, address, is_active to users

Revision ID: 20251204_user_update
Revises: 20250201_book_update
Create Date: 2025-12-04
"""
from alembic import op
import sqlalchemy as sa



revision = "20251204_user_update"
down_revision = "20250201_book_update"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("email", sa.String(), nullable=False))
    op.create_unique_constraint(op.f('uq_users_email'), 'users', ['email'])
    op.add_column("users", sa.Column("phone", sa.String(), nullable=True))
    op.add_column("users", sa.Column("address", sa.String(), nullable=True))
    op.add_column("users", sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text('true')))


def downgrade():
    op.drop_column("users", "is_active")
    op.drop_column("users", "address")
    op.drop_column("users", "phone")
    op.drop_constraint(op.f('uq_users_email'), 'users', type_='unique')
    op.drop_column("users", "email")
