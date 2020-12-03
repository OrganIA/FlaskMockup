from flask import render_template

from .. import bp
from ..models import Receiver, ReceiverForm
from ... import dummy
from app import db

@bp.route('/receivers')
def receivers():
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
