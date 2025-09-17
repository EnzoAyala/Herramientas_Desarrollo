#config.py

DB_URI = 'mysql+mysqlconnector://root:root@localhost/largophone'


class Config:
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False