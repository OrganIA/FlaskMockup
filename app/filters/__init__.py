from app import init_blueprint

bp = init_blueprint(__name__)

@bp.app_template_filter('typify')
def typify(x):
    return x.__class__.__name__

@bp.app_template_filter('datetime')
def datetime(x):
    return x.strftime('%m/%d/%Y')
