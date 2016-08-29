# -*- coding: utf-8 -*-
from saltui import app
from flask import render_template

@app.route('/blank-page')
def blank_page():
    return render_template('blank-page.html')