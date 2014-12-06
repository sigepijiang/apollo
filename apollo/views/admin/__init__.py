#-*- coding: utf-8 -*-

from share.framework.bottle.app import Blueprint

from .market import MarketListView


blueprint_admin = Blueprint('admin', subdomain='www', url_prefix='/admin')

blueprint_admin.add_url_rule(
    '/market/', view_func=MarketListView.as_view(), methods=['GET'],
    endpoint='main'
)
