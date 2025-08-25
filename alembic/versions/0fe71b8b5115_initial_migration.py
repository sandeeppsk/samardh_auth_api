"""Initial migration

Revision ID: 0fe71b8b5115
Revises: 5eae6b16c84f
Create Date: 2025-08-24 19:36:18.821954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fe71b8b5115'
down_revision: Union[str, Sequence[str], None] = '5eae6b16c84f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
