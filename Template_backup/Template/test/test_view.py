"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, g
 
from flask import Blueprint, render_template, abort
from flask import request
from Template import app
from Template.jsonConvert import JsonConvert

from version import Version
from Template.Fiware.entity import Entity

mod_test = Blueprint('test', __name__) 
 

@mod_test.route('/', methods=["GET", "POST"]) 
def home():
    entity = Entity()
    version = Version()

    entity.convertObjectToEntity(version) 

    asJson = JsonConvert.ToJSON(entity)
    print asJson
    response = app.response_class(
        response= asJson,
        status=200,
        mimetype='application/json'
    )
    return response

 