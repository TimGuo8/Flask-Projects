#render_template 底层就是jinja2模板 只是封装了
from datetime import datetime

from flask import Flask, render_template
app = Flask(__name__)

@app.template_filter("dformat")
def datetime_format(value, format="%Y-%d-%m%H:%M"):
    return value.strftime(format)
@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    user = {"username": "Tim", "id": blog_id}
    #使用**语法可以将字典变为关键字参数
    # return render_template("blog_detail.html", **user)
    return render_template("blog_detail.html", user=user)
@app.route("/filter")
def filter():
    user = {"username": "Tim", "id": 2}
    mytime = datetime.now()
    return render_template("filter_demo.html", user = user, mytime = mytime)
@app.route("/control")
def control_statement():
    age = 17
    books = [
        {
            "name": "三国演义",
            "author": "罗贯中"
        },
        {
            "name": "红楼梦",
            "author": "曹雪芹"
        }]
    return render_template("control.html", age=age, books = books)
@app.route("/child1")
def child1():
    return render_template("child1.html")
@app.route("/child2")
def child2():
    return render_template("child2.html")
if __name__ == '__main__':
    app.run()
