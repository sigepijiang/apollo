# -*- coding: utf-8 -*-

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.restful.validator import resful_validator
from share.framework.bottle.engines import db

from apollo.models import MarketShopModel
from apollo.models import MarketFloorModel
from . import forms


class MarketShopAPI(RESTfulOpenAPI):
    path = '/market/shop'
    methods = ['POST', 'GET', 'PUT']

    @resful_validator(forms.id, forms.name, forms.phone, forms.floor_id,
                      forms.index)
    def update(self, id, name, phone, floor_id, index):
        floor = MarketFloorModel.query.get(floor_id)
        shop = MarketShopModel.qurey.get(id)
        if not shop or not floor:
            return

        shop.name = name
        shop.phone = phone
        shop.floor_id = floor_id

        db.session.commit()
        floor.layout.data.set_default(
            'shop_data', {})[index] = shop.as_dict()
        db.session.commit()
        return shop.as_dict()

    @resful_validator(forms.id)
    def get(self, id):
        shop = MarketShopModel.qurey.get(id)
        if not shop:
            return
        return shop.as_dict()

    @resful_validator(forms.id, forms.floor_id, forms.name, forms.phone,
                      forms.index, )
    def create(self, name, phone, id, floor_id, index):
        shop = MarketShopModel(name=name, phone=phone, floor_id=floor_id)
        db.session.add(shop)
        db.session.commit()

        floor = MarketFloorModel.query.get(floor_id)
        floor.layout.data.set_default(
            'shop_data', {})[index] = shop.as_dict()
        db.session.commit()
        return shop.as_dict()
