#-*- coding: utf-8 -*-
from share.framework.bottle import MethodView, render_template

from apollo.models import MarketFloorModel
from .base import AdminListView, AdminEditView
from . import forms


class FloorListAdmin(AdminListView):
    template = 'admin/floor_list.html'
    order_by = 'id'
    obj_name = 'floor_list'
    title = u'楼层列表'
    model = MarketFloorModel


class FloorEditAdmin(AdminEditView):
    template = 'admin/floor_edit.html'
    obj_name = 'floor'
    title = u'编辑编辑'
    model = MarketFloorModel
    redirect_page = 'apollo:admin.floor_list'
    form = forms.FloorEditForm
    query_args = ['floor_id']


class FloorLayoutEditAdmin(MethodView):
    def get(self, floor_id):
        return render_template('admin/floor_layout.html')
