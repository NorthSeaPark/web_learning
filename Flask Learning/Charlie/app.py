from flask import Flask

__author__ = 'Charlie Hou'

app = Flask(__name__)
app.config.from_object('config')

# 根目录下添加了charlie页面
# 注意重定向的过程
@app.route('/charlie')
def hello():
    return "Hello, Charlie"

# 另一种注册路由的方式
#app.add_url_rule('/charlie', view_func=hello)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81 ) # 调试模式不用重启

