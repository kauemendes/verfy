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
    user_ext = db.relationship('UsersExt', backref='users_ext',
                                lazy='joined', uselist=False)
    urls = db.relationship('Urls', backref='urls',
                                lazy='joined', uselist=False)

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
    user_nicename = db.Column(db.String(255), nullable=False)
    user_url = db.Column(db.String(255), nullable=False)
    user_activation_key = db.Column(db.String(255), nullable=False)
    user_status = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, user_id, user_nicename, user_url, user_activation_key, user_status, created_at, updated_at):
        self.user_id = user_id
        self.user_nicename = user_nicename
        self.user_url = user_url
        self.user_activation_key = user_activation_key
        self.user_status = user_status
        self.created_at = created_at
        self.updated_at = updated_at

    def has_activated(self):
        return self.user_activation_key is not None

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<UsersExt {0}>'.format(self.user_id)