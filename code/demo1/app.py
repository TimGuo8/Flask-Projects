# 从flask这个包中导入Flask类
from flask import Flask

# 使用Flask类创建一个app对象
# __name__:代表当前app.py的这个模板的名字
#  作用：  1. 以后出现bug，可以帮助我们快速定位
#         2. 对于寻找模板文件，有一个相对路径
app = Flask(__name__)


# 创建一个路由和视图函数的映射
# 根路由
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Tim!'
# 1. debug 模式:
# 默认加载两个工具：重载器和调试器
# 启用重载器之后，Flask会监视项目中所有源码文件，发现变动时重启服务器。
# 这样每次修改并且保存源码文件后，服务器都会自动重启，让改动生效
# 调试器则是一个基于web的工具，浏览器中可以看到出错信息

# 2. 修改host
# 主要作用：让其他电脑能访问我这台电脑的flask项目

# 3. 修改port
# 如果运行多个flask项目，就需要多个port，或者当前port被占用了 需要换port

if __name__ == '__main__':
    app.run()
