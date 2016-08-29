#/usr/bin/env python
#coding: uTF-8
from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func

from saltui.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from views import api,index,charts,tables,forms,bootstrap_elements,bootstrap_grid,index_rtl,blank_page