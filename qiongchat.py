# -*- coding: utf-8 -*-
import hashlib

import time
from flask import Flask
from flask import request
import xmltodict

app = Flask(__name__)

WECHAT_TOKEN = 'yuqiong'

@app.route('/wechat8017',methods=["POST","GET"])
def index():
    # 获取参数

    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    #将token,timetamp,nonce 三个参数进行字典排序

    tmp_list = [WECHAT_TOKEN,timestamp,nonce]
    tmp_list.sort()

    # 将三个参数字符串进行字典排序
    tmp_list_str = ''.join(tmp_list)

    sig = hashlib.sha1(tmp_list_str).hexdigest()

    if sig == signature :

        if request.method == "GET":
            return echostr
        elif request.method == "POST":
            request_xml_str = request.data

            request_xml_dict = xmltodict.parse(request_xml_str).get('xml')

            msgtype = request_xml_dict.get('MsgType')

            content = "hahhahaaaa"
            if msgtype == "Text":
                response_xml = {
                    "xml" :{
                        "ToUserName":request_xml_dict.get('FromUserName'),
                        "FromUserName":request_xml_dict.get('ToUserName'),
                        "CreateTime" : time.time(),
                        "MsgType" : "Text",
                        "Content" : content,
                    }

                }





if __name__ == '__main__':
    app.run(debug=True,port=8017)
