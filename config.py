#config.py

DB_URI = "mysql+mysqlconnector://root:ozuna1234%40@localhost:3306/largophone"


class Config:
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False