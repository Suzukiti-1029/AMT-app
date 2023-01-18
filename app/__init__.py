import os
from flask import Flask

import secrets

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY= '256133', #TODO デプロイ時secrets.token_hex()に変更
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
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

  from . import db
  db.init_app(app)

  import functools
  from flask import (
    Blueprint, flash, g, redirect,
    render_template, request, session, url_for
  )
  from app.db import get_db

  @app.route('/')
  def test():
    username = secrets.token_hex()
    password = secrets.token_hex()
    testdb = get_db()

    testdb.execute(
      'INSERT INTO user(username, password) VALUES (?, ?)',
      (username, password)
    )

    testdb.commit()
    users = testdb.execute('SELECT * FROM user').fetchall()

    string = ""
    for user in users:
      string = string + user['username'] + "：" + user['password'] + "<br>"
    return string

  return app
