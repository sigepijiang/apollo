#-*- coding: utf-8 -*-

from share.framework.bottle.engines import db
from share.framework.bottle import MethodView, render_template

from apollo.models import MarketFloorModel, MarketFloorLayoutModel
from .base import AdminListView, AdminEditView, AdminOperationView
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


class FloorOperationAdmin(AdminOperationView):
    model_class = MarketFloorModel
    model_keys = ['id']
    actions = ['kill']


class FloorLayoutEditAdmin(MethodView):
    def get(self, floor_id):
        layout = MarketFloorLayoutModel.query.filter(
            MarketFloorLayoutModel.floor_id == floor_id
        ).first()
        if not layout:
            layout = MarketFloorLayoutModel(floor_id=floor_id)
            db.session.add(layout)
            db.session.commit()
        return render_template(
            'admin/floor_layout.html', layout=layout)
