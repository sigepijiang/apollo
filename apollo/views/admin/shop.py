#-*- coding: utf-8 -*-

from .base import AdminListView, AdminEditView

from apollo.models import MarketShopModel
from . import forms


class ShopListAdmin(AdminListView):
    template = 'admin/shop_list.html'
    order_by = 'id'
    obj_name = 'shop_list'
    title = u'商店列表'
    model = MarketShopModel


class ShopEditAdmin(AdminEditView):
    template = 'admin/shop_edit.html'
    obj_name = 'shop'
    title = u'商店编辑'
    model = MarketShopModel
    redirect_page = 'apollo:admin.shop_list'
    form = forms.ShopEditForm
    query_args = ['shop_id']
