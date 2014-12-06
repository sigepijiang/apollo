#-*- coding: utf-8 -*-

from datetime import datetime

import sqlalchemy as sa

from share.framework.bottle.engines import db
from share.utils.base62 import to_url


__all__ = ['MarketModel', 'MarketFloorModel', 'MarketShopModel']

class MarketModel(db.Model, db.TableOpt):
    __tablename__ = 'market'


class MarketFloorModel(db.Model, db.TableOpt):
    __tablename__ = 'floor'


class MarketShopModel(db.Model, db.TableOpt):
    __tablename__ = 'floor'
