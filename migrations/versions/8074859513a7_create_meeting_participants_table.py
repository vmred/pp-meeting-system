"""create meeting_participants table

Revision ID: 8074859513a7
Revises: 38b4cdb77716
Create Date: 2023-09-13 21:52:09.346357

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8074859513a7'
down_revision: Union[str, None] = '38b4cdb77716'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'meeting_participants',
        sa.Column('user_id', sa.UUID, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('meeting_id', sa.Integer, sa.ForeignKey('meetings.id', ondelete='CASCADE'), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'meeting_id'),
    )


def downgrade() -> None:
    op.drop_table('meeting_participants')
