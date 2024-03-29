import importlib
import os
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from .config import Config


db = SQLAlchemy(metadata=MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}))
login_manager = LoginManager()
migrate = Migrate()

def init_blueprint(module, prefix=False, **kwargs):
    name = module[len(__name__) + 1:]
    if prefix:
        kwargs['url_prefix'] = '/' + module.split('.')[-1]
    return Blueprint(name, module,
        static_folder='static',
        template_folder='templates',
        **kwargs
    )

def create_app(config_path='../organia.cfg'):
    app = Flask(__name__)
    os.environ['ORGANIA_CONFIG'] = os.environ.get('ORGANIA_CONFIG', '../organia.cfg')
    app.config.from_object(Config)
    app.config.from_envvar('ORGANIA_CONFIG', True)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.view = 'main.login'

    for module in ['dummy', 'filters', 'main']:
        module = importlib.import_module('{}.{}'.format(__name__, module))
        app.register_blueprint(module.bp)

    return app
