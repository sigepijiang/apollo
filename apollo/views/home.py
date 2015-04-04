#-*- coding: utf-8 -*-

from share.framework.bottle import MethodView, view

from apollo.models import MarketModel


class HomeView(MethodView):
    @view('index.html')
    def get(self):
        market = MarketModel.query.first()
        return {
            'floor_data': [i.layout.data for i in market.floors.all()]}


class AboutView(MethodView):
    @view('about.html')
    def get(self):
        return {}
