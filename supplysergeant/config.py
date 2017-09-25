__author__ = 'baltieri'

import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:P@ssw0rd@localhost:5432/supplysergeant"
    DEBUG = True
    SECRET_KEY = os.environ.get("SUPPLY_SERGEANT_SECRET_KEY", os.urandom(12))
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:P@ssw0rd@localhost:5432/supplysergent-test"
    DEBUG = False
    SECRET_KEY = "Not secret"