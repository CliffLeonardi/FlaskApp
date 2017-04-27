import os
basedir = os.path.abspath(os.path.dirname(_file_))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = "Secret_Key"

OPENID_PROVIDERS = [
{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
{'name': 'MyOpenID', 'url': 'http://www.myopenid.com'}
]
