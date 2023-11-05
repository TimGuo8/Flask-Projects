import random

from flask import Blueprint, render_template, request
from exts import mail,cache
from flask_mail import Message
# 所有的视图函数都要以url_prefix开头
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login():
    pass
@bp.route("/logout")
def logout():
    pass
@bp.route("/register")
def register():
    return render_template("regist.html")

@bp.route("/email/captcha")
def get_email_captcha():
#     两种传参方法, arg and query
    email = request.args.get("email")
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    # random.sample 返回列表类型
    captcha = "".join(random.sample(digits,4))
    body = f"注册验证码为{captcha}, 请勿告诉别人"
    message = Message(subject="验证码邮件，请勿回复", recipients=[email], body = body)
    mail.send(message)
    # 使用flask-caching和redis缓存验证码
    cache.set(email, captcha, timeout=100)
    # 之后用cache.get(email)的方法从缓存中获取用以验证
    return "success"
@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["2529058249@qq.com"], body= "我是邮箱内容")
    mail.send(message)
    return "success"