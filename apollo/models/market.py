#-*- coding: utf-8 -*-

from datetime import datetime

import sqlalchemy as sa

from share.framework.bottle.engines import db
from share.utils.base62 import to_url
from share.sa.types import JSONType


__all__ = ['MarketModel', 'MarketFloorModel', 'MarketShopModel']


class MarketModel(db.Model, db.TableOpt):
    __tablename__ = 'market'

    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Unicode(32), nullable=False)
    title = sa.Column(sa.Unicode(32))
    description = sa.Column(sa.Unicode())
    address = sa.Column(sa.Unicode(128))
    phone = sa.Column(JSONType())
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )


class MarketFloorModel(db.Model, db.TableOpt):
    __tablename__ = 'floor'

    id = sa.Column(sa.Integer(), primary_key=True)
    market_id = sa.Column(sa.Integer())
    category = sa.Column(sa.Unicode(128))
    floor = sa.Column(sa.Integer())
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )


class MarketShopModel(db.Model, db.TableOpt):
    __tablename__ = 'shop'

    id = sa.Column(sa.Integer(), primary_key=True)
    floor_id = sa.Column(sa.Integer())
    name = sa.Column(sa.Unicode(32), nullable=False)
    logo = sa.Column(sa.String())
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )


class MarketFloorLayoutModel(db.Model, db.TableOpt):
    __tablename__ = 'market_floor_layout'

    id = sa.Column(sa.Integer(), primary_key=True)
    floor_id = sa.Column(sa.Integer())
    data = sa.Column(JSONType())
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )
