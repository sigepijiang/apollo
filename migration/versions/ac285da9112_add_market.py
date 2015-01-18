"""add market

Revision ID: ac285da9112
Revises: 35d79ddcc228
Create Date: 2014-12-06 15:14:14.153153

"""

# revision identifiers, used by Alembic.
revision = 'ac285da9112'
down_revision = '35d79ddcc228'

from datetime import datetime

from alembic import op
import sqlalchemy as sa
from share.sa.types import JSONType

from sqlalchemy.dialects.postgresql import ENUM


def upgrade():
    op.create_table(
        'market',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.Unicode(32)),
        sa.Column('title', sa.Unicode(32)),
        sa.Column('description', sa.Unicode()),
        sa.Column('address', sa.Unicode(128)),
        sa.Column('phone', JSONType()),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )

    op.create_table(
        'floor',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('market_id', sa.Integer()),
        sa.Column('category', sa.Unicode(128)),
        sa.Column('floor', sa.Integer()),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )

    op.create_table(
        'shop',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('floor_id', sa.Integer()),
        sa.Column('name', sa.Unicode(32)),
        sa.Column('logo', sa.CHAR(32)),
        sa.Column('phone', sa.String(16)),
        sa.Column(
            'area_type',
            sa.Enum(
                'shop', 'escalator', 'lift', 'exit', 'hydrant', 'counter',
                'garbage', 'phone', 'restaurant', 'wc', 'stair',
                name='shop_area_type_enum',
            )
        ),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )

    op.create_table(
        'market_floor_layout',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('floor_id', sa.Integer()),
        sa.Column('data', JSONType()),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )


def downgrade():
    op.drop_table('market_floor_layout')
    op.drop_table('shop')
    op.drop_table('floor')
    op.drop_table('market')
    ENUM(name='shop_area_type_enum').drop(
        op.get_bind(), checkfirst=False)
