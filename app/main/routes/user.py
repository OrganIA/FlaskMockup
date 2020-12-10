from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app import db, login_manager
from .. import bp
from ..models import User, UserForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    def exit():
        return render_template(
            'login.html',
            form=form,
            form_title='Se connecter',
        )
    form = UserForm()
    form.submit = 'Se connecter'
    form.sort_by(['email', 'password'])
    if not form.is_submitted():
        return exit()
    try:
        user = User.query.filter_by(username=form.username.data).one()
    except (NoResultFound, MultipleResultsFound) as e:
        flash("L'utilisateur est introuvable")
        return exit()
    form._obj = user
    if not form.validate():
        flash("Erreur")
        return exit()
    login_user(user, remember=True)
    flash("Vous voilà connecté {}".format(user))
    return redirect(url_for('.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    form.submit = 'S\'inscrire'
    form.sort_last(['password'])
    if not form.validate_on_submit():
        return render_template(
            'register.html',
            form_title='S\'inscrire',
            form=form,
        )
    user = User()
    form.populate_obj(user)
    user.password = generate_password_hash(user.password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('Bienvenue {}'.format(user))
    return redirect(url_for('.receivers'))

@bp.route('/logout')
def logout():
    logout_user()
    flash('Vous avez été déconnecté')
    return redirect(url_for('.login'))
