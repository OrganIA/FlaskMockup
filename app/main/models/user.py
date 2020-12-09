from hashlib import md5
from flask_login import UserMixin
from wtforms import PasswordField

from app import db, login_manager
from app.modelform import ModelForm, lbl

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, **lbl('Prénom'))
    last_name = db.Column(db.String, **lbl('Nom de famille'))
    username = db.Column(db.String, unique=True, **lbl('Nom d\'utilisateur'))
    password = db.Column(db.String)

    def __repr__(self):
        return '<{user.__class__.__name__}#{user.id} {user.username}>'.format(user=self)

    def __str__(self):
        return '{user.first_name} {user.last_name}'.format(user=self)

    @property
    def avatar_url(self, size=None):
        if not self.email:
            return ''
        return 'https://www.gravatar.com/avatar/{hash}?d=mp&r=pg{params}'.format(
            hash=md5(self.email().encode('utf-8')).hexdigest(),
            params='&s={}'.format(size) if size else ''
        )

class UserForm(ModelForm):
    class Meta:
        model = User
    password = PasswordField('Mot de passe')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
