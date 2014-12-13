#-*- coding: utf-8 -*-

import sqlalchemy as sa
from bottle import redirect, request

from share.framework.bottle import MethodView, cached_property, url_for
from share.framework.bottle import render_template
from share.framework.bottle.engines import db


class AdminListView(MethodView):
    template = 'list.html'
    order_by = ''
    order_by_chinese = False
    obj_name = ''
    title = ''
    model = ''

    def query_factory(self):
        return self.model.query

    @cached_property
    def query(self):
        return self.query_factory()

    @cached_property
    def records(self):
        return self.query.order_by(self._order_by).all()

    @cached_property
    def _order_by(self):
        order_by = self.order_by
        order_by_chinese = self.order_by_chinese
        order_method = 'asc'

        if order_by.startswith('~'):
            order_method = 'desc'

        order_by = order_by.strip('~')

        result = getattr(
            self.model, order_by, self.model.id
        )
        if order_by_chinese:
            result = sa.func.convert_to(result, 'GBK')

        return getattr(result, order_method, None)()

    def context(self):
        return {
            self.obj_name: self.records,
            'title': self.title,
        }

    def get(self):
        return render_template(self.template, **self.context())


class AdminEditView(MethodView):
    template = 'edit.html'
    obj_name = ''
    title = ''
    model = ''
    redirect_page = ''
    form = None
    query_args = ['id']

    @cached_property
    def record(self):
        index = [self.args.get(i) for i in self.query_args]
        if not filter(None, index):
            return None

        return self.model.query.get(index)

    def context(self):
        form = self.form()

        if self.record:
            form = self.form(obj=self.record)

        return {
            'record': self.record,
            'title': self.title,
            'form': form,
        }

    def get(self, **kwargs):
        self.args = kwargs
        return render_template(self.template, **self.context())

    def post(self, **kwargs):
        self.args = kwargs
        form = self.form(request.forms)
        if not form.validate():
            context = self.context()
            context['form'] = form
            return render_template(self.template, **context)

        record = self.record
        if not record:
            record = self.model()
            db.session.add(record)

        form.populate_obj(record)
        db.session.commit()
        return redirect(url_for(self.redirect_page))
