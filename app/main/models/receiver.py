from app import db
from app.modelform import ModelForm, f_cls

class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, info={'label': 'Prénom'})
    last_name = db.Column(db.String, info={'label': 'Nom de famille'})
    birthday = db.Column(db.Date, info={'label': 'Date de naissance'})
    arrival = db.Column(db.Date, info={'label': 'Arrivée'})
    needed_organ = db.Column(db.String, info={'label': 'Organe'})
    gender = db.Column(db.String, info={'label': 'Sexe'})
    abo = db.Column(db.String, info={'label': 'ABO'})

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
