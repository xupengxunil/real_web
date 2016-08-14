#/usr/bin/env python
#coding: uTF-8

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True