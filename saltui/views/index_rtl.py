# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/index-rtl')
def index_rtl():
    return render_template('index-rtl.html')