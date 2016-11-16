# app/server/user/models.py


import datetime

from app.server import app, db, bcrypt


class Urls(db.Model):

    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    ipv4_origin = db.Column(db.String(255), nullable=True)
    ipv6_origin = db.Column(db.String(255), nullable=True)
    protocol = db.Column(db.String(255), nullable=True)
    searched_on = db.Column(db.DateTime, nullable=True)

    # def __init__(self, email, password, admin=False):
    #     self.email = email
    #     self.password = bcrypt.generate_password_hash(
    #         password, app.config.get('BCRYPT_LOG_ROUNDS')
    #     )
    #     self.registered_on = datetime.datetime.now()
    #     self.admin = admin
    #
    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Urls {0}>'.format(self.url)
