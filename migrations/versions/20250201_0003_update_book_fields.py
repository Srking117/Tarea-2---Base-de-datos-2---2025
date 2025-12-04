"""Add new fields to Book model (Req 3)"""

from alembic import op
import sqlalchemy as sa

revision = "20250201_book_update"
down_revision = "20250201_review"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("stock", sa.Integer(), nullable=False, server_default="1"))
    op.add_column("books", sa.Column("description", sa.String(), nullable=True))
    op.add_column("books", sa.Column("language", sa.String(length=10), nullable=False, server_default="es"))
    op.add_column("books", sa.Column("publisher", sa.String(), nullable=True))


def downgrade():
    op.drop_column("books", "publisher")
    op.drop_column("books", "language")
    op.drop_column("books", "description")
    op.drop_column("books", "stock")
