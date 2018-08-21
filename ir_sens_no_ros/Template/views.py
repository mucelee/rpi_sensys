"""
Routes and views for the flask application.
"""
import json

from datetime import datetime
from flask import render_template,Response
from Template import app

#from version import Version
from jsonConvert import JsonConvert 

from Fiware.entity import Entity
from mod.sw.taskMonitoring import TaskMonitoring

entity = Entity()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


#@app.route('/version')
#def version():
#    version = Version()

#    entity.convertObjectToEntity(version) 

#    asJson = JsonConvert.ToJSON(entity)
#    print asJson
#    response = app.response_class(
#        response= asJson,
#        status=200,
#        mimetype='application/json'
#    )
#    return response


@app.route('/taskMonitoring')
def taskMonitoring():
    taskMon = TaskMonitoring()

    entity.convertObjectToEntity(taskMon) 

    asJson = JsonConvert.ToJSON(entity)
    print asJson
    response = app.response_class(
        response= asJson,
        status=200,
        mimetype='application/json'
    )
    return response