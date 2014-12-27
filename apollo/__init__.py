#-*- coding: utf-8 -*-

from share.framework.bottle import Avalon

# push the app into the stack FIRST!
app = Avalon(__name__)

from .views import blueprint_www
from .views import bp_admin
app.register_blueprint(blueprint_www)
app.register_blueprint(bp_admin)


from .backends import bp_backends
app.register_blueprint(bp_backends)

from .apis import bp_apis
app.register_blueprint(bp_apis)
