# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/forms')
def forms():
    return render_template('forms.html')