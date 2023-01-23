import os
from flask import Flask
from app.database import init_db
import app.models

import secrets

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True, static_folder='resources/static')
  app.config.from_mapping( # TODO デプロイ：設定ファイルを外部に分離
    SECRET_KEY='256133',
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'suzukiti',
      'password': '256133',
      'host': 'mysql',
      'db_name': 'dev_amtapp'
    }),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
  )

  if test_config is None:
    # テスト設定ないとき、インスタンスの設定があれば、読み込む
    app.config.from_pyfile('config.py', silent=True)
  else:
    # テスト設定あれば、それを読み込む
    app.config.from_mapping(test_config)

  # インスタンスフォルダを作成、すでにあったらスルー
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  init_db(app)

  from .controller import amt
  app.register_blueprint(amt.bp)

  return app
