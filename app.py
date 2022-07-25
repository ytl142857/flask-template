from flask import Flask, request, render_template
from myMethods import count
import json

app = Flask(__name__)


# 直接渲染页面
@app.route('/index/', methods=['GET', 'POST'])
def index():
  content = {}
  content['hello_message'] = 'hello 小明'
  if request.method == 'POST':
    if request.form['username'] and request.form['password']:
      content['message'] = '登录成功'
    else:
      content['error'] = '未发送用户名和密码'
  return render_template("index.html", context=content)


# 返回 JSON, 可用做简易的 API 编写
@app.route('/api/hello/', methods=['GET'])
def api_hello():
  content = { "data": "hello world", "message": "success", "code": 200 }
  return content


@app.route('/api/count/', methods=['POST'])
def api_count():
  data = json.loads(request.data)
  return { "result": count(data['data']), "message": "success", "code": 200 }


if __name__ == '__main__':
  app.debug = True
  app.run(port=4001)