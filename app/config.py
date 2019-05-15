import os
class Config:
    # set up database location config
    SECRET_KEY=os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/bookLibrary.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False