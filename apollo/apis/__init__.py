#-*- coding: utf-8 -*-

from share.framework.bottle import APIBlueprint

from .user import UserAPI
from .market import MarketFloorAPI
from .shop import MarketShopAPI

bp_apis = APIBlueprint('apis')
UserAPI.attach_to(bp_apis)
MarketFloorAPI.attach_to(bp_apis)
MarketShopAPI.attach_to(bp_apis)
