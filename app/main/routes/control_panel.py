from datetime import datetime, timedelta
import names
import random
from flask import flash, redirect, render_template, url_for

from app import db
from .. import bp
from ..models import Donor, Receiver, data

@bp.route('/cpanel')
def cpanel():
    return render_template('cpanel.html', title='Panneau de contrôle')

def fill_random(person):
    person.first_name = names.get_first_name()
    person.last_name = names.get_last_name()
    person.birthday = datetime.today() - timedelta(
        days=random.random() * 365 * 80
    )
    #TODO use key instad of value for datas
    person.gender = random.choice(data.GENDERS)[1]
    person.abo = random.choice(data.BLOOD_TYPES)
    if person.gender != 'Femme':
        organs = [x for x in data.ORGANS if x[1] != 'Utérus']
    else:
        organs = data.ORGANS
    person.organ = random.choice(organs)[1]

def add_random_persons(type=None, number=10):
    for _ in range(10):
        person = type()
        fill_random(person)
        db.session.add(person)
        flash('{} a été ajouté aux receveurs'.format(str(person)))
    db.session.commit()
    return redirect(url_for('.cpanel'))

@bp.route('/receivers/add/random')
def add_random_receivers():
    return add_random_persons(Receiver)

@bp.route('/donors/add/random')
def add_random_donors():
    return add_random_persons(Donor)

@bp.route('/cpanel/delete_all')
def delete_all_persons():
    for r in Receiver.query.all():
        db.session.delete(r)
    for r in Donor.query.all():
        db.session.delete(r)
    db.session.commit()
    return redirect(url_for('.cpanel'))
