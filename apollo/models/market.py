#-*- coding: utf-8 -*-

from datetime import datetime

import sqlalchemy as sa

from share.framework.bottle.engines import db
from share.sa.types import JSONType
from share.utils.image import image_for
from share.sa.mutable import MutableDict

from share.sa.types import HashkeyType


__all__ = [
    'MarketModel',
    'MarketFloorModel',
    'MarketShopModel',
    'MarketFacilityModel',
    'MarketFloorLayoutModel'
]


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
    background_image = sa.Column(HashkeyType())
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )

    market = db.relationship(
        'MarketModel',
        primaryjoin='MarketFloorModel.market_id == MarketModel.id',
        foreign_keys='[MarketFloorModel.market_id]',
        lazy='joined',
        backref=db.backref(
            'floors', lazy='dynamic', order_by='MarketFloorModel.floor.asc()')
    )
    layout = db.relationship(
        'MarketFloorLayoutModel',
        primaryjoin='MarketFloorLayoutModel.floor_id == MarketFloorModel.id',
        foreign_keys='[MarketFloorLayoutModel.floor_id]',
        lazy='joined', uselist=False,
    )

    def as_dict(self):
        return {
            'id': self.id,
            'market_id': self.market_id,
            'category': self.category,
            'floor': self.floor,
            'background_image': image_for(self.background_image),
            'layout': self.layout.as_dict()
        }


class MarketFacilityModel(db.Model, db.TableOpt):
    __tablename__ = 'facility'

    id = sa.Column(sa.Integer(), primary_key=True)
    floor_id = sa.Column(sa.Integer())
    facility_type = sa.Column(
        sa.Enum(
            'escalator', 'lift', 'exit', 'hydrant', 'counter',
            'garbage', 'phone', 'restaurant', 'wc', 'stair',
            name='shop_facility_type_enum',
        )
    )

    def as_dict(self):
        return {
            'id': self.id,
            'floor_id': self.floor_id,
            'facility_type': self.facility_type,
        }


class MarketShopModel(db.Model, db.TableOpt):
    __tablename__ = 'shop'

    id = sa.Column(sa.Integer(), primary_key=True)
    floor_id = sa.Column(sa.Integer())
    name = sa.Column(sa.Unicode(32), nullable=False)
    logo = sa.Column(sa.String(32))
    phone = sa.Column(sa.String(16))
    shop_type = sa.Column(sa.Unicode(16))
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )

    floor = db.relationship(
        'MarketFloorModel',
        primaryjoin='MarketFloorModel.id == MarketShopModel.floor_id',
        foreign_keys='[MarketShopModel.floor_id]',
        lazy='joined',
        backref=db.backref('shops', lazy='dynamic')
    )

    def as_dict(self):
        return {
            'id': self.id,
            'floor_id': self.floor_id,
            'name': self.name,
            'phone': self.phone,
            'shop_type': self.shop_type or '',
        }


class MarketFloorLayoutModel(db.Model, db.TableOpt):
    __tablename__ = 'market_floor_layout'

    id = sa.Column(sa.Integer(), primary_key=True)
    floor_id = sa.Column(sa.Integer())
    data = sa.Column(MutableDict.as_mutable(JSONType()))
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )

    def as_dict(self):
        return {
            'id': self.id,
            'floor_id': self.floor_id,
            'data': self.data,
            'date_created': self.date_created.isoformat(),
        }
