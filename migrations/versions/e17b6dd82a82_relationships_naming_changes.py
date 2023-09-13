"""relationships naming changes

Revision ID: e17b6dd82a82
Revises: d669081548e2
Create Date: 2023-09-13 22:45:06.514652

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e17b6dd82a82'
down_revision: Union[str, None] = 'd669081548e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
