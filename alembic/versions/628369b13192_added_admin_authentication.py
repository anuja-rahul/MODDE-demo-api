"""added admin authentication

Revision ID: 628369b13192
Revises: b35eaaa96903
Create Date: 2024-08-19 00:12:41.018496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '628369b13192'
down_revision: Union[str, None] = 'b35eaaa96903'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'admins', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'admins', type_='unique')
    op.drop_column('admins', 'email')
    # ### end Alembic commands ###
