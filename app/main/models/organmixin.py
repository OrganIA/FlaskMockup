from app import db
from app.models import Person
from app.modelform import f_cls, lbl
from . import data

class OrganMixin(Person):
    birthday = db.Column(
        db.Date, **lbl('Date de naissance'), nullable=False
    )
    gender = db.Column(
        db.String,
        info={
            'label': 'Sexe',
            'choices': data.GENDERS,
        },
        nullable=False
    )
    abo = db.Column(
        db.String,
        info={
            'label': 'ABO',
            'choices': [(x, x) for x in data.BLOOD_TYPES]},
        nullable=False
    )
    organ = db.Column(
        db.String, nullable=False, info={
            'label': 'Organe',
            'choices': data.ORGANS,
        }
    )
    arrival = db.Column(db.Date, **lbl('Arrivée'))

FIELD_ARGS = {
    'first_name': f_cls('small'),
    'last_name': f_cls('small'),
    'organ': f_cls('mini'),
    'gender': f_cls('mini'),
    'abo': f_cls('mini'),
}
