"""Renaming students to scholars

Revision ID: dcca78f70fcc
Revises: 89d1e9cf9963
Create Date: 2024-05-12 20:54:21.301915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcca78f70fcc'
down_revision = '89d1e9cf9963'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')