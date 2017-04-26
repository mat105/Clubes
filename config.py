import os

__where = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbdata.db'.format(__where)