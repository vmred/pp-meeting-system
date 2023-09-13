"""create expense_participants table

Revision ID: d669081548e2
Revises: 8074859513a7
Create Date: 2023-09-13 21:53:05.500766

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd669081548e2'
down_revision: Union[str, None] = '8074859513a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'expense_participants',
        sa.Column('user_id', sa.UUID, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('expense_id', sa.Integer, sa.ForeignKey('expenses.id', ondelete='CASCADE'), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'expense_id'),
    )


def downgrade() -> None:
    pass
