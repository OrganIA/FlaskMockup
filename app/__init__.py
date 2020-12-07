import importlib
import os
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config


db = SQLAlchemy()
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

    for module in ['dummy', 'filters', 'main']:
        module = importlib.import_module('{}.{}'.format(__name__, module))
        app.register_blueprint(module.bp)

    return app
