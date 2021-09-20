# -*- coding: utf-8 -*-

from flask import Flask, render_template
from key_api import get_key
from image_api import get_image
from mecab_api import me
from topkey import select_topkey
from test import great_img
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/hello')
def indexs():
    return 'hello'


@app.route('/url', methods=['POST'])
def hello():
    top_key = "美女"
    try:
        if request.method == 'GET':
            top_key = request.json['quali']
            num = request.json["num"]
    except:
        return "EOF"
    hello = get_key(top_key)
    if(hello == "EOF"):
        return render_template("mainpage.html", name="https://sports-pctr.c.yimg.jp/r/iwiz-amd/20210918-00403683-usoccer-000-1-view.jpg?cx=0&cy=0&cw=1200&ch=750")
    hello2 = me(hello)
    return jsonify({"top_key":top_key,"get_key":hello2})