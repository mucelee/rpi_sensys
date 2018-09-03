"""
The flask application package.
"""

from flask import Flask


app = Flask(__name__)

import Template.views

from Template.mod.sw.taskplanner_view import mod_sw_taskplanner
from Template.test.test_view import mod_test

print "register blueprints"
app.register_blueprint(mod_sw_taskplanner, url_prefix='/mod.sw.tp')
app.register_blueprint(mod_test , url_prefix='/test')
print "register done"