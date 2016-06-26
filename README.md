# nile web service

## 環境構築

### ライブラリのインストール

```
$ pip install -r requirements.txt
```

### dbの作成

```
$ python manage.py makemigrations ec2 # ec2/models.pyの中身からmigrationファイルを作成
$ python manage.py migrate # dbに反映
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