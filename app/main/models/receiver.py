from app import db
from app.modelform import ModelForm, f_cls

BLOOD_TYPES = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, info={'label': 'Prénom'}, nullable=False)
    last_name = db.Column(
        db.String, info={'label': 'Nom de famille'}, nullable=False
    )
    birthday = db.Column(
        db.Date, info={'label': 'Date de naissance'}, nullable=False
    )
    gender = db.Column(
        db.String,
        info={
            'label': 'Sexe',
            'choices': [('male', 'Homme'), ('female', 'Femme')]
        },
        nullable=False
    )
    abo = db.Column(
        db.String,
        info={
            'label': 'ABO',
            'choices': [(x, x) for x in BLOOD_TYPES]},
        nullable=False
    )
    needed_organ = db.Column(
        db.String, info={'label': 'Organe'}, nullable=False
    )
    arrival = db.Column(db.Date, info={'label': 'Arrivée'})

    table_excludes = ['id']

    def __str__(self):
        return '<{0.__class__.__name__}: {0.first_name} {0.last_name} needs {0.needed_organ}>'.format(self)

    def __repr__(self):
        return str(self)

class ReceiverForm(ModelForm):
    submit = 'Ajouter'
    class Meta:
        model = Receiver
        field_args = {
            'first_name': f_cls('small'),
            'last_name': f_cls('small'),
            'needed_organ': f_cls('mini'),
            'gender': f_cls('mini'),
            'abo': f_cls('mini'),
        }
