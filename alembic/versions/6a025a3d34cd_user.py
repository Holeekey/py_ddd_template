"""user

Revision ID: 6a025a3d34cd
Revises: 
Create Date: 2024-10-09 19:38:36.077274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a025a3d34cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False),
        sa.Column('first_name', sa.String(20), nullable=False),
        sa.Column('last_name', sa.String(20), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('user')
