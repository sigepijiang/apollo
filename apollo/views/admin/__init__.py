#-*- coding: utf-8 -*-

from share.framework.bottle.app import Blueprint
from .market import MarketListAdmin, MarketEditAdmin, MarketOperationAdmin
from .floor import FloorListAdmin, FloorEditAdmin, FloorLayoutEditAdmin
from .floor import FloorOperationAdmin
from .shop import ShopListAdmin, ShopEditAdmin, ShopOperationAdmin

bp_admin = Blueprint('admin', subdomain='www', url_prefix='/admin')

bp_admin.add_url_rule(
    '/market/',
    view_func=MarketListAdmin.as_view(),
    methods=['GET'],
    endpoint='market_list'
)
bp_admin.add_url_rule(
    '/market/<market_id:int>/edit/',
    view_func=MarketEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='market_edit'
)
bp_admin.add_url_rule(
    '/market/create/',
    view_func=MarketEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='market_create',
    defaults={'market_id': None}
)
bp_admin.add_url_rule(
    '/market/operation/<id:int>/<action:re:kill>/',
    view_func=MarketOperationAdmin.as_view(),
    methods=['POST'],
    endpoint='market_operation',
)

bp_admin.add_url_rule(
    '/floor/',
    view_func=FloorListAdmin.as_view(),
    methods=['GET'],
    endpoint='floor_list'
)
bp_admin.add_url_rule(
    '/floor/<floor_id:int>/edit/',
    view_func=FloorEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='floor_edit'
)
bp_admin.add_url_rule(
    '/floor/create/',
    view_func=FloorEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='floor_create',
    defaults={'floor_id': None}
)
bp_admin.add_url_rule(
    '/floor/<floor_id:int>/layout/',
    view_func=FloorLayoutEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='floor_layout',
)
bp_admin.add_url_rule(
    '/floor/operation/<id:int>/<action:re:kill>/',
    view_func=FloorOperationAdmin.as_view(),
    methods=['POST'],
    endpoint='floor_operation',
)

bp_admin.add_url_rule(
    '/shop/',
    view_func=ShopListAdmin.as_view(),
    methods=['GET'],
    endpoint='shop_list'
)
bp_admin.add_url_rule(
    '/shop/<shop_id:int>/edit/',
    view_func=ShopEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='shop_edit'
)
bp_admin.add_url_rule(
    '/shop/create/',
    view_func=ShopEditAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='shop_create',
    defaults={'shop_id': None}
)
bp_admin.add_url_rule(
    '/shop/operation/<id:int>/<action:re:kill>/',
    view_func=ShopOperationAdmin.as_view(),
    methods=['POST'],
    endpoint='shop_operation',
)


from .shop import FloorShopListAdmin
bp_admin.add_url_rule(
    '/floor/<floor_id:int>/shops/',
    view_func=FloorShopListAdmin.as_view(),
    methods=['GET', 'POST'],
    endpoint='floor_shops',
)
