from collections import OrderedDict
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

from app import db

BaseModelForm = model_form_factory(FlaskForm)

def f_cls(l):
    if isinstance(l, str):
        l = [l]
    return {'render_kw': {'data-classes': l }}

def lbl(s):
    return {'info': {'label': s}}

class ModelForm(BaseModelForm):
    class Meta:
        locales = ['fr_FR', 'fr']

    def sort_by(self, l):
        self._fields = OrderedDict((k, self._fields[k]) for k in l)

    def sort_last(self, l):
        keys = [k for k in self._fields.keys() if k not in l]
        keys += l
        self.sort_by(keys)

    @classmethod
    def get_session(self):
        return db.session
