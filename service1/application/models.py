from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password= db.Column(db.String(500), nullable=False)


    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])


    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
