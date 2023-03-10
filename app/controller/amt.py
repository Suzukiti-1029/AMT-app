from flask import (
  Blueprint, render_template, request,
  flash, redirect, url_for
)
from app.database import db
from app.models import Amt_fluctuations

bp = Blueprint('amt', __name__, url_prefix='/amt')

@bp.route('/')
def index():
  amt_flucs = Amt_fluctuations.query.all()
  total_amount = sum([amt_fluc.amt_fluctuations_amount for amt_fluc in amt_flucs])
  return render_template('amt/index.html', amt_flucs=amt_flucs, total_amount=total_amount)

@bp.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    f_date = request.form['f_date']
    f_amount = request.form['f_amount']
    f_purpose = request.form['f_purpose']
    f_note = request.form['f_note']
    errs = []
    if not f_date:
      errs += ['「日付」を入力してください']
    if not f_amount:
      errs += ['「金額(円)」を入力してください']
    if not f_purpose:
      errs += ['「用途」を入力してください']

    if errs != []:
      [flash(err) for err in errs]
    else:
      fluc = Amt_fluctuations(f_date, f_purpose, f_amount, f_note)
      db.session.add(fluc)
      db.session.commit()
      return redirect(url_for('amt.index'))
  return render_template('amt/create.html')
