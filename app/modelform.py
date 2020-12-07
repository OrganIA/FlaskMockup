from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

from app import db

BaseModelForm = model_form_factory(FlaskForm)

def f_cls(l):
    if isinstance(l, str):
        l = [l]
    return {'render_kw': {'data-classes': l }}

class ModelForm(BaseModelForm):
    class Meta:
        locales = ['fr_FR', 'fr']

    @classmethod
    def get_session(self):
        return db.session
