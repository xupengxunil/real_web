#/usr/bin/env python
#coding: uTF-8

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:jiajia@192.168.2.111:3306/flask"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:jiajia@172.25.18.170:3306/flask"
    SQLALCHEMY_ECHO = True