#-*- coding: utf-8 -*-

from .base import AdminListView, AdminEditView, AdminOperationView

from apollo.models import MarketModel
from . import forms


class MarketListAdmin(AdminListView):
    template = 'admin/market_list.html'
    order_by = 'id'
    obj_name = 'market_list'
    title = u'商城列表'
    model = MarketModel


class MarketEditAdmin(AdminEditView):
    template = 'admin/market_edit.html'
    obj_name = 'market'
    title = u'商城编辑'
    model = MarketModel
    redirect_page = 'apollo:admin.market_list'
    form = forms.MarketEditForm
    query_args = ['market_id']


class MarketOperationAdmin(AdminOperationView):
    model_class = MarketModel
    model_keys = ['id']
    actions = ['kill']
