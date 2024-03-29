from app import db
from app.modelform import ModelForm
from .organmixin import OrganMixin, FIELD_ARGS

class Receiver(db.Model, OrganMixin):
    id = db.Column(db.Integer, primary_key=True)

    table_excludes = ['id']

    def __repr__(self):
        return '<{0.__class__.__name__}: {0.first_name} {0.last_name} needs {0.organ}>'.format(self)

class ReceiverForm(ModelForm):
    submit = 'Ajouter'
    show_requireds = True
    class Meta:
        model = Receiver
        field_args = FIELD_ARGS
