from flask import flash, redirect, render_template, url_for
from sqlalchemy import inspect

from .. import bp
from ..models import Receiver, ReceiverForm
from ... import dummy
from app import db
from app.model import table_rows

@bp.route('/receivers', methods=['GET', 'POST'])
def receivers():
    results = table_rows(Receiver.query.all())
    for r in results:
        r['action'] = '<a href="{url}">Supprimer</a>'.format(
            url=url_for('.delete_receiver', id=r['id'])
        )
    return render_template(
        'receivers.html',
        title='Receveurs',
        data=results,
        excludes=Receiver.table_excludes,
    )

@bp.route('/receivers/random')
def random_receivers():
    return render_template(
        'receivers.html',
        title='Receveurs',
        data=[dummy.get_random_entry() for _ in range(20)],
    )

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
    receiver = Receiver()
    form.populate_obj(receiver)
    db.session.add(receiver)
    db.session.commit()
    flash('Receveur {0.first_name} {0.last_name} ajouté'.format(receiver))
    return redirect(url_for('.receivers'))


@bp.route('/receivers/delete/<int:id>')
def delete_receiver(id):
    receiver = Receiver.query.get_or_404(id)
    db.session.delete(receiver)
    db.session.commit()
    flash('Receveur {0.first_name} {0.last_name} supprimé'.format(receiver))
    return redirect(url_for('.receivers'))

@bp.route('/receivers/<int:id>')
def get_receiver(id):
    #TODO
    receiver = Receiver.query.get_or_404(id)
    return 'hey {}'.format(receiver.first_name)
