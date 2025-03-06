"""Renaming students to scholars

Revision ID: 374fee6dddb8
Revises: 791279dd0760
Create Date: 2025-03-06 11:46:29.861525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '374fee6dddb8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')

    pass
