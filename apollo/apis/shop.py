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
                      forms.index, forms.shop_type)
    def update(self, id, name, phone, floor_id, index, shop_type):
        floor = MarketFloorModel.query.get(floor_id)
        shop = MarketShopModel.query.get(id)
        if not shop or not floor:
            shop = MarketShopModel()
            db.session.add(shop)

        shop.name = name
        shop.phone = phone
        shop.floor_id = floor_id
        shop.shop_type = shop_type

        db.session.commit()
        shop_data = floor.layout.data.get('shop_data', {})
        shop_data[index] = shop.as_dict()
        floor.layout.data['shop_data'] = shop_data
        db.session.commit()
        return shop.as_dict()

    @resful_validator(forms.id)
    def get(self, id):
        shop = MarketShopModel.query.get(id)
        if not shop:
            return
        return shop.as_dict()

    @resful_validator(forms.floor_id, forms.name, forms.phone,
                      forms.index, forms.shop_type)
    def create(self, name, phone, floor_id, index, shop_type):
        shop = MarketShopModel(name=name, phone=phone, floor_id=floor_id)
        db.session.add(shop)
        db.session.commit()

        floor = MarketFloorModel.query.get(floor_id)
        shop_data = floor.layout.data.get('shop_data', {})
        shop_data[index] = shop.as_dict()
        floor.layout.data['shop_data'] = shop_data
        db.session.commit()
        return shop.as_dict()
