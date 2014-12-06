#-*- coding: utf-8 -*-

from share.framework.bottle import MethodView, view


class MarketListView(MethodView):
    @view('admin/index.html')
    def get(self):
        return {}
