from flask import Blueprint, render_template
from app.database import db
from app.models import Amt_fluctuations

bp = Blueprint('amt', __name__, url_prefix='/amt')

@bp.route('/')
def index():
  amt_flucs = Amt_fluctuations.query.all()
  return render_template('amt/index.html', amt_flucs=amt_flucs)
