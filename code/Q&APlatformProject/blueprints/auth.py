import random
from flask import Blueprint, render_template, request
from celery import Celery
from exts import mail,cache
from flask_mail import Message
from utils import restful
from .forms import RegisterForm
# 所有的视图函数都要以url_prefix开头
bp = Blueprint("auth", __name__, url_prefix="/auth")

celery = Celery(
        "task",
        backend="redis://127.0.0.1:6379/0",
        broker="redis://127.0.0.1:6379/0")
@celery.task
def send_mail(recipient, subject, body):
    # from app import app
    # with app.app_context():
    message = Message(subject=subject, recipients=recipient, body=body)
    mail.send(message)
    print("发送成功!")

@bp.route("/login")
def login():
    pass
@bp.route("/logout")
def logout():
    pass

#GET: 从服务器获取数据
#POST: 将客户端数据提交给服务器
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
    # 验证用户提交的邮箱和验证码是否正确
    #表单验证 flask-wtf
        return render_template("regist.html")
    else:
        #进到这里就只有可能是POST
        # 表单验证
        form = RegisterForm(request.form)
        if form.validate():
            return "success"
        else:
            # print(form.errors)
            return "fail"
# 默认get请求
@bp.route("/email/captcha", methods=["GET"])
def get_email_captcha():
    try:
        #两种传参方法, arg and query
        email = request.args.get("email")
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
        # random.sample 返回列表类型
        captcha = "".join(random.sample(digits,4))
        body = f"注册验证码为{captcha}, 请勿告诉别人"
        recipients=[email]
        subject="验证码邮件，请勿回复"
        send_mail.delay(recipients, subject, body)
        # message = Message(subject=subject, recipients=[recipients], body=body)
        # mail.send(message)
        # 使用flask-caching和redis缓存验证码
        cache.set(email, captcha, timeout=1000)
        # 之后用cache.get(email)的方法从缓存中获取用以验证
        # 使用restful显示状态码
        return restful.ok()
    except Exception as e:
        print(e)
        return restful.server_error()

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["2529058249@qq.com"], body= "我是邮箱内容")
    mail.send(message)
    return "success"