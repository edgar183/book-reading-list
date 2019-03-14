"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import SQLALCHEMY_DATABASE_URI
from app import app, db

# Migrate is used to initialize the extension, while Manager gives you access to command line options.
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    """