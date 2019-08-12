from flask_testing import TestCase
from app.main import db
from manage import app
from app.main.service.user_service import save_new_user
import uuid
import datetime


data = {"public_id": "1",
        "email": "test123@gmail.com",
        "username": "test123",
        "password": "test",
        "registered_on": "August 18 2014 - 21:11:35"}


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()
        save_new_user(data)

    def tearDown(self):
        db.session.remove()
        db.drop_all()