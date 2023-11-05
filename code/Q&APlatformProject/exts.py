# exts.py 为了解决循环应用问题
# flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache
# 在app.py中和应用绑定
db = SQLAlchemy()
# 创建一个mail对象
mail = Mail()
# 创建一个Flask-caching对象
cache = Cache()