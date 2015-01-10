#-*- coding: utf-8 -*-

from .base import AdminListView, AdminEditView

from share.framework.bottle import render_template, MethodView
from share.framework.bottle.engines import db

from apollo.models import MarketShopModel, MarketFloorModel
from apollo.models import MarketFloorLayoutModel
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


class FloorShopListAdmin(MethodView):
    def get(self, floor_id):
        floor = MarketFloorModel.query.get(floor_id)
        layout = MarketFloorLayoutModel.query.filter(
            MarketFloorLayoutModel.floor_id == floor_id
        ).first()
        if not layout:
            layout = MarketFloorLayoutModel(floor_id=floor_id)
            db.session.add(layout)
            db.session.commit()
        return render_template(
            'admin/floor_shops.html', floor=floor, layout=layout)
