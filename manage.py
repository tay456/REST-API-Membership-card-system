import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main.model import user
from app import blueprint


from app.main import create_app, db

"""use factory function to create a instance of application"""
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

"""
registering blueprint with the flask application instance
"""
app.register_blueprint(blueprint)


"""push an application context"""
app.app_context().push()

""" instantiate the manager and migrate classes."""
manager = Manager(app)

migrate = Migrate(app, db)

# pass the db and MigrateCommand instances to the add_command interface
# of the manager. This is to expose all the database migration commands through Flask-Script
manager.add_command('db', MigrateCommand)

"""marks the function as executable from the command line"""
@manager.command
def run():
    app.run()


"""marks the function as executable from the command line"""
@manager.command
def test():
    """Allows you to runs any unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()