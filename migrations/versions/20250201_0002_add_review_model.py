"""Add Review model"""

from alembic import op
import sqlalchemy as sa
import advanced_alchemy



revision = "20250201_review"
down_revision = "20250201_category"   
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "reviews",
        sa.Column("id", sa.BigInteger(), primary_key=True),

        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.String(), nullable=False),
        sa.Column("review_date", sa.Date(), nullable=False),

        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("book_id", sa.BigInteger(), sa.ForeignKey("books.id"), nullable=False),

        sa.Column("created_at", advanced_alchemy.types.datetime.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", advanced_alchemy.types.datetime.DateTimeUTC(timezone=True), nullable=False),
    )


def downgrade():
    op.drop_table("reviews")
