"""Renaming email column

Revision ID: eddd4fbab9b0
Revises: dcca78f70fcc
Create Date: 2024-05-12 21:03:09.894114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eddd4fbab9b0'
down_revision = 'dcca78f70fcc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name='email_address')


def downgrade() -> None:
    op.alter_column('scholars', 'email_address', new_column_name='email')