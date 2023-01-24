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
  return render_template('amt/index.html', amt_flucs=amt_flucs)

@bp.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    f_date = request.form['f_date']
    f_amount = request.form['f_amount']
    f_purpose = request.form['f_purpose']
    f_note = request.form['f_note']
    error = None
    if not f_date:
      error = '「日付」を入力してください'
    if not f_amount:
      error = '「金額(円)」を入力してください'
    if not f_purpose:
      error = '「用途」を入力してください'
    if error is not None:
      flash(error)
    else:
      fluc = Amt_fluctuations(f_date, f_purpose, f_amount, f_note)
      db.session.add(fluc)
      db.session.commit()
      return redirect(url_for('amt.index'))
  return render_template('amt/create.html')
