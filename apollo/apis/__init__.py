#-*- coding: utf-8 -*-

from share.framework.bottle import APIBlueprint

from .user import UserAPI
from .market import MarketFloorAPI

bp_apis = APIBlueprint('apis')
UserAPI.attach_to(bp_apis)
MarketFloorAPI.attach_to(bp_apis)
