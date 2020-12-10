from hashlib import md5
from flask_login import UserMixin
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField

from app import db, login_manager
from app.models import Person
from app.modelform import ModelForm, lbl

class User(UserMixin, db.Model, Person):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return '<{user.__class__.__name__}#{user.id} {user.username}>'.format(user=self)

    @property
    def avatar_url(self, size=None):
        if not self.email:
            return ''
        return 'https://www.gravatar.com/avatar/{hash}?d=mp&r=pg{params}'.format(
            hash=md5(self.email.encode('utf-8')).hexdigest(),
            params='&s={}'.format(size) if size else ''
        )

class UserForm(ModelForm):
    class Meta:
        model = User
    password = PasswordField('Mot de passe')
    email = EmailField('Email')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
