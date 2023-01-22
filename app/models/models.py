from datetime import datetime
from app.database import db

class Sample(db.Model):
  __tablename__ = 'sample'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
