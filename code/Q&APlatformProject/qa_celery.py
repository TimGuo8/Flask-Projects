# from flask_mail import Message
# from exts import mail
from celery import Celery
# 定义任务函数
# from module_with_my_app_and_mail import app, mail
# 创建Celery对象
# @celery.task
# def send_mail(recipient, subject, body):
#     # from app import app
#     # with app.app_context():
#     message = Message(subject=subject, recipients=[recipient], body=body)
#     mail.send(message)
#     print("发送成功!")
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'])

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery
