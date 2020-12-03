from flask import render_template

from .. import bp
from ..models import Receiver
from ... import dummy
from app import db

@bp.route('/receivers')
def receivers():
    return render_template('receivers.html', data=[dummy.get_random_entry() for _ in range(20)])
