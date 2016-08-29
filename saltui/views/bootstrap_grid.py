# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/bootstrap-grid')
def bootstrap_grid():
    return render_template('index.html')