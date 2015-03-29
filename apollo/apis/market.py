# -*- coding: utf-8 -*-

from bottle import request

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.restful.validator import resful_validator
from share.framework.bottle.engines import db
from share.framework.bottle.errors import APIBadRequest

from apollo.models import MarketFloorModel, MarketFloorLayoutModel
from . import forms


class MarketFloorBGIAPI(RESTfulOpenAPI):
    path = '/market/floor/background_image'
    methods = ['POST']

    @resful_validator(forms.floor_id, forms.background_image)
    def create(self, floor_id, background_image):
        floor = MarketFloorModel.query.get(floor_id)

        if not floor:
            raise APIBadRequest('Floor<%s> is not found' % floor_id)

        floor.background_image = background_image
        db.session.commit()


class MarketFloorAPI(RESTfulOpenAPI):
    path = '/market/floor'
    methods = ['POST']

    def create(self):
        if request.json is None:
            raise APIBadRequest(
                'Content type should be "application/json"')
        data = request.json
        floor_id = data.pop('floor_id', None)
        if floor_id is None:
            raise APIBadRequest(
                '"floor_id" is missing')

        floor = MarketFloorModel.query.get(floor_id)
        if not floor:
            raise APIBadRequest(
                'Floor<%s> is not found' % floor_id)

        layout = floor.layout
        if not layout:
            layout = MarketFloorLayoutModel(floor_id=floor_id)
            db.session.add(layout)

        layout.data = data
        db.session.commit()
        return {}
