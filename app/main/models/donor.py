from app import db
from app.modelform import ModelForm
from .organmixin import OrganMixin, FIELD_ARGS

class Donor(db.Model, OrganMixin):
    id = db.Column(db.Integer, primary_key=True)

    table_excludes = ['id']

    def __repr__(self):
        return '<{0.__class__.__name__}: {0.first_name} {0.last_name} gives {0.organ}>'.format(self)

class DonorForm(ModelForm):
    submit = 'Ajouter'
    show_requireds = True
    class Meta:
        model = Donor
        field_args = FIELD_ARGS
