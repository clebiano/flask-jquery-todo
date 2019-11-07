import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite3.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sqlite3.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# SECRET_KEY = 'xx-xxxx-xxx-xxxxx'
