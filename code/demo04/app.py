from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "dd19991207"
DATABASE = "database_flask"
app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}"
                                         f":{PORT}/{DATABASE}?charset=utf8mb4")
# 在app.config中设置好连接数据库的信息
# 然后使用SQLALchemy创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)

# 上下文原理
# with app.app_context():
#     with db.engine.connect() as conn:
#         # 这里需要用sqlalchemy.text把query变成正确格式
#         rs = conn.execute(text("SELECT 1;"))
#         print(rs.fetchone()) #(1,)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
# user = User(username = "Tim", password = '199912')


with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/user/add")
def add_user():
    # 创建ORM对象
    user1 = User(username="Tim", password='199912')
    user2 = User(username="GTH", password='666666')
    # 讲ORM对象添加到db.session中
    db.session.add(user1)
    db.session.add(user2)
    # 将db.session中的改变同步到数据中
    db.session.commit()
    return "用户创建成功"
@app.route("/user/query")
def query_user():
    # 1.  get查找 根据主键查找
    user = User.query.get(1)
    print(f"{user.id} : {user.username} {user.password}")
    #  2.  filter_by查找
    # 返回一个query对象：类数组
    users = User.query.filter_by(username = "GTH")
    for user in users:
        print(f"{user.username}")
    return "数据查找成功"
@app.route("/user/update")
def update_user():
    # users = User.query.filter_by(username="GTH")[0] 会有索引超出错误
    user = User.query.filter_by(username="GTH").first()
    if user is not None:
        user.password = '222222'
    db.session.commit()
    return "数据更新成功"
@app.route("/user/delete")
def delete_user():
#     先查找
    user = User.query.get(1)
# 从db.session中删除
    db.session.delete(user)
# 同步到数据库
    db.session.commit()
    return "数据删除成功！"
if __name__ == '__main__':
    app.run()
