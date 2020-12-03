from flask import render_template

from .. import app
from .. import dummy

@app.route('/receivers')
def receivers():
    return render_template('receivers.html', data=[dummy.get_random_entry() for _ in range(20)])
