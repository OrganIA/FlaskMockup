from flask import render_template
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
    return render_template(
        'form.html',
        title='Ajouter un receveur',
        form=form,
    )
