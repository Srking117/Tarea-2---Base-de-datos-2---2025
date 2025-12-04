"""Add Category model and book_categories m2m table"""

from alembic import op
import sqlalchemy as sa


revision = "20250201_category"
down_revision = "acc8ae75f9e8"
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_table(
        "categories",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(length=100), unique=True, nullable=False),
        sa.Column("description", sa.String(), nullable=True),
    )

    
    op.create_table(
        "book_categories",
        sa.Column("book_id", sa.BigInteger(), sa.ForeignKey("books.id"), primary_key=True),
        sa.Column("category_id", sa.BigInteger(), sa.ForeignKey("categories.id"), primary_key=True),
    )


def downgrade():
    op.drop_table("book_categories")
    op.drop_table("categories")
