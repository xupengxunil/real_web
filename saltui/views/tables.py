# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/tables')
def tables():
    return render_template('index.html')