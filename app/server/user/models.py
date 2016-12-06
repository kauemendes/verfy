# app/server/user/models.py


import datetime

from app.server import app, db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    user_ext = db.relationship('UsersExt', backref='users_ext',  lazy='joined', uselist=False)
    urls = db.relationship('Urls', backref='urls', lazy='joined', uselist=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)


class UsersExt(db.Model):

    __tablename__ = "users_ext"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    nicename = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=True)
    activation_key = db.Column(db.String(255), nullable=True)
    status = db.Column(db.Boolean, nullable=True)
    facebook_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=True)

    def __init__(self, user_id, nicename, activation_key, facebook_id, status=False, url=None):
        self.user_id = user_id
        self.nicename = nicename
        self.activation_key = activation_key
        self.status = status
        self.facebook_id = facebook_id
        self.url = url

    def has_activated(self):
        return self.activation_key is not None

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<UsersExt {0}>'.format(self.user_id)