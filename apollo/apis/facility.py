# -*- coding: utf-8 -*-

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.restful.validator import resful_validator
from share.framework.bottle.engines import db

from apollo.models import MarketFacilityModel
from apollo.models import MarketFloorModel
from . import forms


class MarketFacilityAPI(RESTfulOpenAPI):
    path = '/market/facility'
    methods = ['POST', 'GET', 'PUT']

    @resful_validator(forms.id, forms.facility_type, forms.floor_id,
                      forms.index)
    def update(self, id, facility_type, floor_id, index):
        floor = MarketFloorModel.query.get(floor_id)
        facility = MarketFacilityModel.qurey.get(id)
        if not facility or not floor:
            return

        facility.facility_type = facility_type
        db.session.commit()
        facility_data = floor.layout.data.get('facility_data', {})
        facility_data[index] = facility.as_dict()
        floor.layout.data['facility_data'] = facility_data
        db.session.commit()
        return facility.as_dict()

    @resful_validator(forms.id)
    def get(self, id):
        facility = MarketFacilityModel.qurey.get(id)
        if not facility:
            return
        return facility.as_dict()

    @resful_validator(forms.floor_id, forms.facility_type,
                      forms.index)
    def create(self, facility_type, floor_id, index):
        facility = MarketFacilityModel(
            facility_type=facility_type, floor_id=floor_id)
        db.session.add(facility)
        db.session.commit()

        floor = MarketFloorModel.query.get(floor_id)
        facility_data = floor.layout.data.get('facility_data', {})
        facility_data[index] = facility.as_dict()
        floor.layout.data['facility_data'] = facility_data
        db.session.commit()
        return facility.as_dict()
