#!/bin/bash

# システムパッケージをアップデート
yum -y update
# IUSリポジトリをインストール
yum install -y https://repo.ius.io/ius-release-el7.rpm
# IUSリポジトリ設定をエイリアス無効でコピー(無効にしないとどうしてもy/n聞かれる)
\cp -f /home/amtapp/.devcontainer/flask/ius.repo /etc/yum.repos.d/ius.repo

# システムパッケージをアップデート
yum -y update
# 依存パッケージのインストール：https://github.com/pyenv/pyenv/wiki#suggested-build-environment
# openssl,gitは古いので別途インストール
yum install -y gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel tk-devel libffi-devel xz-devel # git openssl-devel

# git2.36インストール
yum install -y --enablerepo=ius git236
git --version

# opensslインストール
cd /usr/local/src
yum install -y perl-core
curl -OL https://www.openssl.org/source/openssl-1.1.1.tar.gz -o /usr/local/src/openssl-1.1.1.tar.gz
tar xzvf openssl-1.1.1.tar.gz
cd openssl-1.1.1
./config
make && make test || true && make install
# opensslを使えるように設定
ldd /usr/local/bin/openssl
sh -c 'echo /usr/local/lib64 > /etc/ld.so.conf.d/local.conf'
ldconfig
ldconfig -p | grep libssl.so.1.1
ldd /usr/local/bin/openssl
/usr/local/bin/openssl version

cd /home/amtapp
# pyenvインストール
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
# pyenvを使えるように設定
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv --version

# python3.11.1インストール
pyenv install -v 3.11.1
# pythonバージョン切り替え
pyenv global 3.11.1
pyenv rehash
python --version

cd /home/amtapp
# venv環境構築
python -m venv venv
source venv/bin/activate
# pipアップグレード
python -m pip install --upgrade pip
pip -V
# 開発に必要パッケージをインストール
pip install flask flask-sqlalchemy gunicorn --use-pep517
# deactivate