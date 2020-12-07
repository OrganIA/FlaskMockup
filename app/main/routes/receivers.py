from flask import flash, redirect, render_template, url_for
from sqlalchemy import inspect

from .. import bp
from ..models import Receiver, ReceiverForm
from ... import dummy
from app import db
from app.model import table_rows

@bp.route('/receivers')
def receivers():
    results = table_rows(Receiver.query.all(), excludes=Receiver.table_excludes)
    return render_template(
        'receivers.html',
        title='Receveurs',
        data=results,
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
    form.method = 'post'
    if not form.validate():
        return render_template(
            'form.html',
            title='Ajouter un receveur',
            form=form,
        )
    # Form is valid, we process it
    receiver = Receiver()
    form.populate_obj(receiver)
    db.session.add(receiver)
    db.session.commit()
    flash('Receveur {0.first_name} {0.last_name} ajouté'.format(receiver))
    return redirect(url_for('.receivers'))

