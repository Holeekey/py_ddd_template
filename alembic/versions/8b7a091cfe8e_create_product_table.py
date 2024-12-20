"""create product table

Revision ID: 8b7a091cfe8e
Revises: 3142e3ec568c
Create Date: 2024-11-17 00:38:04.243879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b7a091cfe8e'
down_revision: Union[str, None] = '3142e3ec568c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'products',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('name', sa.String(20), nullable=False),
        sa.Column('price', sa.Float(2), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('user')
    op.create_table(
        'users',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False),
        sa.Column('first_name', sa.String(20), nullable=False),
        sa.Column('last_name', sa.String(20), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )
