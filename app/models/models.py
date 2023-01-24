from datetime import datetime
from app.database import db
from sqlalchemy import text, Text, Date, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.schema import FetchedValue

class Amt_fluctuations(db.Model):
  __tablename__ = 'amt_fluctuations'
  amt_fluctuations_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
  amt_fluctuations_date = db.Column(Date, nullable=False)
  amt_fluctuations_purpose = db.Column(Text, nullable=False)
  amt_fluctuations_amount = db.Column(Integer, nullable=False)
  amt_fluctuations_note = db.Column(Text)
  amt_fluctuations_create_at = db.Column(DateTime, server_default=func.now())
  amt_fluctuations_update_at = db.Column(
    DateTime,
    server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    server_onupdate=FetchedValue()
  )

  def __init__(self, date, purpose, amount, note=None):
    super().__init__()
    self.amt_fluctuations_date = date
    self.amt_fluctuations_purpose = purpose
    self.amt_fluctuations_amount = amount
    self.amt_fluctuations_note = note
