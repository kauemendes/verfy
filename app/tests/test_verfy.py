# app/server/tests/test_user.py


import datetime
import unittest

from flask_login import current_user

from app.server import bcrypt
from app.server.user.forms import LoginForm
from app.server.user.models import User
from base import BaseTestCase


class TestVerfyBlueprint(BaseTestCase):

    def test_se_campo_url_aceita_url(self):


