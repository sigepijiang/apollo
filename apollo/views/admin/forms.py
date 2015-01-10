#-*- coding: utf-8 -*-

from wtforms import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import Required

from wtforms.ext.sqlalchemy import fields as sa_fields

from apollo.models import MarketModel, MarketFloorModel


class MarketEditForm(Form):
    name = StringField(u'商城名称', validators=[Required(u'商城名称必填')])
    title = StringField(
        u'商城标题', validators=[Required(u'商城标题必填')])
    description = TextAreaField(
        u'商城描述', validators=[Required(u'商城描述必填')])
    address = TextAreaField(
        u'商城地址', validators=[Required(u'商城地址必填')])
    phone = StringField(
        u'联系方式', validators=[Required(u'联系方式必填')])


class FloorEditForm(Form):
    market = sa_fields.QuerySelectField(
        u'商城', query_factory=lambda: MarketModel.query.all(),
        get_label='name'
    )
    category = TextAreaField(
        u'分类', validators=[Required(u'分类必填')])
    floor = IntegerField(
        u'楼层', validators=[Required(u'楼层必填')]
    )


class ShopEditForm(Form):
    floor = sa_fields.QuerySelectField(
        u'楼层', query_factory=lambda: MarketFloorModel.query.all(),
        get_label='floor'
    )
    name = StringField(
        u'名称', validators=[Required(u'名称必填')])
