from app import db
from app.modelform import lbl

class Person:
    first_name = db.Column(db.String, **lbl('Prénom'), nullable=False)
    last_name = db.Column(
        db.String, **lbl('Nom de famille'), nullable=False
    )

    def __str__(self):
        return '{person.first_name} {person.last_name}'.format(person=self)
