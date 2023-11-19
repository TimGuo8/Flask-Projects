import wtforms
from wtforms.validators import Email, Length, EqualTo
from models.UserModel import UserModel
from exts import cache, db
#Form:主要用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Wrong Email Format！")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Wrong Captcha Format！")])
    userName = wtforms.StringField(validators=[Length(min=3, max=20, message="Wrong User Name Format！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Wrong Password Format！")])
    password_conform = wtforms.StringField(validators=[EqualTo("password", message="They are not the same！")])

    # 自定义验证
    # 1. 邮箱是否已经被注册
    # 2. 验证码是否正确
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")
    # 2. 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        cache_captcha = cache.get(email)
        if not cache_captcha or captcha != cache_captcha:
            raise wtforms.ValidationError(message="验证码错误！")