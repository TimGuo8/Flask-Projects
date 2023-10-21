from flask import Flask, request

app = Flask(__name__)

# url: http(80)/https(443)://www.qq.com
# url与视图：path与视图
# app.route是个装饰器
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route("/blog")
def blog_list():
    return "this is the blog list"
# 带参数的url：将参数固定到了path中，
# path parameter
@app.route("/blog/<int:blog_id>")
def blog_detail(blog_id):
    return "this is a blog: %s" % blog_id

# /book/list:会给我第一页的数据
# /book/list?page=2: 获取第二页的数据
# query parameter
# http://127.0.0.1:5000/book/list?page=100
@ app.route("/book/list")
def book_list():
    page = request.args.get("page", default = 1, type = int)
    return f"当前获取的时第{page}页"



if __name__ == '__main__':
    app.run()
