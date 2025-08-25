"""Initial migration

Revision ID: 685369b66a66
Revises: 0fe71b8b5115
Create Date: 2025-08-24 19:43:15.203765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '685369b66a66'
down_revision: Union[str, Sequence[str], None] = '0fe71b8b5115'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
