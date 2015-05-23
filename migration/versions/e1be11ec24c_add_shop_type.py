"""add shop type

Revision ID: e1be11ec24c
Revises: ac285da9112
Create Date: 2015-05-17 17:25:35.442572

"""

# revision identifiers, used by Alembic.
revision = 'e1be11ec24c'
down_revision = 'ac285da9112'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('shop', sa.Column('shop_type', sa.Unicode(16)))


def downgrade():
    op.drop_column('shop', 'shop_type')
