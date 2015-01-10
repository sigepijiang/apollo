# -*- coding: utf-8 -*-

import voluptuous


ukey = {
    voluptuous.Required('ukey'): voluptuous.Match(r'^[0-9a-zA-Z]{8}$'),
}

nickname = {
}

id = {
    voluptuous.Required('id'): voluptuous.Coerce(int),
}

floor_id = {
    voluptuous.Required('floor_id'): voluptuous.Coerce(int),
}

name = {
    voluptuous.Required('name'): voluptuous.Coerce(unicode),
}

phone = {
    voluptuous.Required('phone'): voluptuous.Coerce(unicode),
}

gender = {}
title = {}
summary = {}
