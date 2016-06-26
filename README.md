# nile web service

## 環境構築

### Mac環境
いかに従えば環境構築できます。

#### python環境の構築

pyenvとvirtualenvの環境を構築。
```
$ brew install pyenv
$ brew install pyenv-virtualenv
```

pythonがpyenvの方を向くように設定。
.bashrcなどに以下を記述。
```
export PYENV_ROOT="${HOME}/.pyenv"
export PATH=${PYENV_ROOT}/bin:$PATH
eval "$(pyenv init -)"
```

プロジェクトの環境を構築
```
$ git clone git@github.com:chikyukotei/nile_web_service.git
$ cd nile_web_service

$ pyenv install 3.5.1
$ pyenv versions   # 3.5.1が入っていることを確認
$ pyenv virtualenv 3.5.1 nws   # virtualenvで今回のリポジトリのライブラリ群を置いておく用の環境nws(名前は何でも良い)を作成
$ pyenv local nws   # このディレクトリで、作成したpython環境を使うように設定
```

#### ライブラリのインストール

```
$ pip install -r requirements.txt
```

#### dbの作成

```
$ python manage.py makemigrations ec2 # ec2/models.pyの中身からmigrationファイルを作成
$ python manage.py migrate # dbに反映
```

#### サーバ立ち上げ

```
$ ./rundjango   # python manage.py runserver と同じ
```

## よくある問題

### migrationしたはずなのにテーブル・カラムが無い等
開発環境では全データ消えても困らないと思うので、以下のコマンド

```
rm ec2/migrations/*
rm db.sqlite3 # データ全部消えるので注意
python manage.py makemigrations ec2
python manage.py migrate
```