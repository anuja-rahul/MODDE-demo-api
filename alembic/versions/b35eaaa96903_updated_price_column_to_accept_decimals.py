"""updated price column to accept decimals

Revision ID: b35eaaa96903
Revises: 9583c0f23d96
Create Date: 2024-08-18 22:46:47.613576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b35eaaa96903'
down_revision: Union[str, None] = '9583c0f23d96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###
