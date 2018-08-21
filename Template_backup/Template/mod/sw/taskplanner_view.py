"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, g
 
from flask import Blueprint, render_template, abort
from flask import request

mod_sw_taskplanner= Blueprint('mod.sw.tp', __name__) 

VERSION = "0.1"
counter = 0;

@mod_sw_taskplanner.route('/', methods=["GET", "POST"])
@mod_sw_taskplanner.route('/home', methods=["GET", "POST"])
@mod_sw_taskplanner.route('/task', methods=["GET", "POST"])
def home():
    """Renders the home page."""
    if request.method == 'POST':
        global counter
        data = request.get_json()
        print data
        counter += 1
        print(counter)
        print("")
        return "200"
    else:
        return render_template(
            'contact.html',
            title='Contact',
            year=datetime.now().year,
            message='Your contact page.'
        )

@mod_sw_taskplanner.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@mod_sw_taskplanner.route('/version')
def version():
    return "version " + VERSION

@mod_sw_taskplanner.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@mod_sw_taskplanner.before_app_first_request
def bla():
    print "blabla"
    peter =  getattr(g, '_peter', None)
    if peter is not None:
        print peter