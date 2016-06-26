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
