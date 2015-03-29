#-*- coding: utf-8 -*-

from share.framework.bottle import APIBlueprint

from .user import UserAPI
from .market import MarketFloorAPI, MarketFloorBGIAPI
from .shop import MarketShopAPI
from .facility import MarketFacilityAPI

bp_apis = APIBlueprint('apis')
UserAPI.attach_to(bp_apis)
MarketFloorAPI.attach_to(bp_apis)
MarketFloorBGIAPI.attach_to(bp_apis)
MarketShopAPI.attach_to(bp_apis)
MarketFacilityAPI.attach_to(bp_apis)
