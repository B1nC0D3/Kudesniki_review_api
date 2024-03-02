"""create users table

Revision ID: 4f9154c84b86
Revises: 
Create Date: 2024-02-20 13:22:05.976418

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4f9154c84b86"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("password", sa.LargeBinary(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
