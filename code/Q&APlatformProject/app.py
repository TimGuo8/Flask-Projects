from flask import Flask
from config import Config
from flask_mail import Message
from exts import db, mail, cache
from qa_celery import make_celery
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from models.UserModel import UserModel
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()
# 绑定配置文件
app.config.from_object(Config)
# 将db和app连接
db.init_app(app)
migrate = Migrate(app, db)
# 初始化mail
mail.init_app(app)
# 初始化cache
cache.init_app(app)
# init celery
celery = make_celery(app)

# 将blueprint和app连接
# blueprint作用是讲视图函数模块化
with app.app_context():
    app.register_blueprint(qa_bp)
    app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
