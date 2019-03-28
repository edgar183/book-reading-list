
class Config:
    # set up database location config
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/bookLibrary.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False