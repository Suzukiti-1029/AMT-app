from flask import Blueprint

bp = Blueprint('amt', __name__, url_prefix='/amt')

@bp.route('/')
def index():
  return 'amtのindex'