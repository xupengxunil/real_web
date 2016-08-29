# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/bootstrap-elements')
def bootstrap_elements():
    return render_template('bootstrap-elements.html')