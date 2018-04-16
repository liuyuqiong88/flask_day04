#coding:utf-8

from flask import Flask,render_template
from goods import good_blue
from users import user_blue
from order import orderblue
from cart import cart_blue
from chat import chat_blue

app = Flask(__name__)
app.register_blueprint(good_blue)
app.register_blueprint(user_blue)
app.register_blueprint(orderblue)
app.register_blueprint(cart_blue)
app.register_blueprint(chat_blue)

@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)

