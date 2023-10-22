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
with app.app_context():
    with db.engine.connect() as conn:
        # 这里需要用sqlalchemy.text把query变成正确格式
        rs = conn.execute(text("SELECT 1;"))
        print(rs.fetchone()) #(1,)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
