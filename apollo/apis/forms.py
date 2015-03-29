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

index = {
    voluptuous.Required('index'): voluptuous.Coerce(int),
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

facility_type = {
    voluptuous.Required('facility_type'): voluptuous.Any(
        'escalator', 'lift', 'exit', 'hydrant', 'counter',
        'garbage', 'phone', 'restaurant', 'wc', 'stair'
    )
}

background_image = {
    voluptuous.Required('background_image'): voluptuous.Coerce(str),
}


gender = {}
title = {}
summary = {}
