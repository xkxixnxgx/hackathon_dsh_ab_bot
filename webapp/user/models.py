from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, index=True, primary_key=True)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), index=True, nullable=False)
    date_reg = db.Column(db.String(12), nullable=False)
    picture = db.Column(db.String(70), nullable=False, default='default.jpg')
    username = db.Column(db.String(50), index=True, nullable=True)

    def set_password(self, user_password):
        self.user_password = generate_password_hash(user_password)

    def check_password(self, user_password):
        return check_password_hash(self.user_password, user_password)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)

    @property
    def is_admin(self):
        return self.role == 'admin'


class Requests(db.Model, UserMixin):
    id = db.Column(db.Integer, index=True, primary_key=True)
    product = db.Column(db.String(100), unique=False, nullable=False)
    date_add = db.Column(db.String(20), nullable=False)
    status_request = db.Column(db.String(20), unique=False, nullable=False)
    first_name_client = db.Column(db.String(20), unique=False, nullable=False)
    last_name_client = db.Column(db.String(20), unique=False, nullable=False)
    passport_series = db.Column(db.String(20), unique=False, nullable=False)
    passport_number = db.Column(db.String(20), unique=False, nullable=False)
    phone_client = db.Column(db.String(20), index=True, unique=True, nullable=False)


    def __repr__(self):
        return '<Product {}>'.format(self.product)

    @property
    def is_admin(self):
        return self.role == 'admin'