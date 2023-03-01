from datetime import datetime

from flask_login import UserMixin

from webapp.db import db
from webapp.user.enums import UserRole

from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=True)
    phone_number = db.Column(db.String(12), unique=True)
    nick_name = first_name = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(UserRole), index=True)
    registration_datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User name {self.id}, {self.full_name}>'
