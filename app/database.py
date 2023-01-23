from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import click

db = SQLAlchemy()

@click.command('init-db')
def init_db_command():
  db.drop_all()
  click.echo('初期化')

def init_db(app):
  db.init_app(app)
  Migrate(app, db, 'instance/migrations')
  app.cli.add_command(init_db_command)