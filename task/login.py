# -*- coding: utf-8 -*-

from flask import request,Flask,jsonify

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username,password]):
        return jsonify({'code':'-1',"error":u"参数不能为空"})

    if username != 'yuqiong' or password != 'qiong':
        return jsonify({'code': "-2", "error": u"用户名或密码不正确"})

    return jsonify({'code': "0", "error": u"登录成功"})


if __name__ == '__main__':
    app.run(debug=True)
