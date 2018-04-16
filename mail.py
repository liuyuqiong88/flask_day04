#coding:utf8

from flask import Flask,render_template
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['SECRET_KEY'] = "qiong"

app.config['MAIL_SERVER'] = "smtp.163.com"
app.config['MAIL_PORT'] = 25
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "13798076559@163.com"
app.config['MAIL_PASSWORD'] = "yuqiong114"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<13798076559@163.com>'

# EMAIL_HOST = 'smtp.163.com'                 # 发邮件主机
# EMAIL_PORT = 25                             # 发邮件端口
# EMAIL_HOST_USER = 'islet1010@163.com'       # 发件人邮件
# EMAIL_HOST_PASSWORD = 'python123'           # 邮箱授权时获得授权码，非注册登录密码
# EMAIL_FROM = '天天生鲜<islet1010@163.com>'   # 邮件中的显示的发件人, 邮箱需要与发件人邮箱一致
mail = Mail(app)




@app.route('/')
def index():


    return render_template('mail.html')

@app.route('/send')
def send_mail():



    message = Message()

    message.subject = "saddfsadfas"

    message.recipients = ["13798076559@163.com"]

    message.body = "sdftgsdfssdg"


    mail.send(message)

    return u"发送中．．．．．"
if __name__ == '__main__':

    app.run(debug=True)