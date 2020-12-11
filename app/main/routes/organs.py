from flask import flash, redirect, render_template, url_for
import random
from sqlalchemy import inspect

from .. import bp
from ..models import Donor, DonorForm, Receiver, ReceiverForm
from ... import dummy
from app import db
from app.model import table_rows, table_inject

def get_persons(t):
    results = table_rows(t.query.all())
    table_inject(results, 'action',
        lambda x: '<a href="{url}"><i class="fas fa-trash-alt"></i></a>'.format(
            url=url_for('.delete_{}'.format(t.__tablename__.lower()), id=x['id'])
        )
    )
    return results

title = 'Liste d\'attente'
tabs = [('.receivers', 'Receveurs'), ('.donors', 'Donneurs')]

@bp.route('/receivers')
def receivers():
    return render_template(
        'organs.html',
        add_route='.add_receiver',
        title=title,
        tabs=tabs,
        data=get_persons(Receiver),
        excludes=Receiver.table_excludes,
    )

@bp.route('/donors')
def donors():
    data = get_persons(Donor)
    for r in data:
        r['action'] = ' <a href="{url}"><i class="fa fa-search"></i></a> '.format(
            url=url_for('.match_donor', id=r['id'])
        ) + r['action']
    return render_template(
        'organs.html',
        add_route='.add_donor',
        title=title,
        tabs=tabs,
        data=data,
        excludes=Donor.table_excludes,
    )

@bp.route('/receivers/random')
def random_receivers():
    return render_template(
        'receivers.html',
        title='Receveurs',
        data=[dummy.get_random_entry() for _ in range(20)],
    )


def add_person(t, form):
    person = t()
    form.populate_obj(person)
    db.session.add(person)
    db.session.commit()
    flash('{} ajouté'.format(person))

@bp.route('/receivers/add', methods=['GET', 'POST'])
def add_receiver():
    form = ReceiverForm()
    if not form.validate_on_submit():
        return render_template(
            'form.html',
            form_title='Ajouter un receveur',
            form=form,
        )
    # Form is valid, we process it
    add_person(Receiver, form)
    return redirect(url_for('.receivers'))

@bp.route('/donors/add', methods=['GET', 'POST'])
def add_donor():
    form = DonorForm()
    if not form.validate_on_submit():
        return render_template(
            'form.html',
            form_title='Ajouter un donneur',
            form=form,
        )
    # Form is valid, we process it
    add_person(Donor, form)
    return redirect(url_for('.donors'))

def delete_person(t, id):
    person = t.query.get(id)
    if person is None:
        flash('Cet individu n\'existe pas')
        return
    db.session.delete(person)
    db.session.commit()
    flash('{} supprimé'.format(person))

@bp.route('/receivers/delete/<int:id>')
def delete_receiver(id):
    delete_person(Receiver, id)
    return redirect(url_for('.receivers'))

@bp.route('/donors/delete/<int:id>')
def delete_donor(id):
    delete_person(Donor, id)
    return redirect(url_for('.donors'))

@bp.route('/donors/match/<int:id>')
def match_donor(id):
    donor = Donor.query.get_or_404(id)
    matching_receivers = Receiver.query.filter_by(
        organ=donor.organ
    ).all()
    data=table_rows(matching_receivers)
    for r in data:
        r['Score'] = random.random() * 1000
    data.sort(key=lambda x: x['Score'], reverse=True)
    for r in data:
        r['Score'] = '{:.1f}'.format(r['Score'])
    return render_template(
        'matching.html',
        title='Receveurs correspondants',
        donor=donor,
        data =data,
        table_id='matching-results',
        excludes=Receiver.table_excludes,
    )

@bp.route('/receivers/<int:id>')
def get_receiver(id):
    #TODO
    receiver = Receiver.query.get_or_404(id)
    return 'hey {}'.format(receiver.first_name)
