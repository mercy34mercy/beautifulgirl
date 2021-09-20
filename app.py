# -*- coding: utf-8 -*-

from flask import Flask, render_template
from key_api import get_key
from image_api import get_image
from ginza_jp_api import ginza
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


@app.route('/url')
def hello():
    top_key = "美女"
    hello = get_key(top_key)
    if(hello == "EOF"):
        return render_template("mainpage.html", name="https://sports-pctr.c.yimg.jp/r/iwiz-amd/20210918-00403683-usoccer-000-1-view.jpg?cx=0&cy=0&cw=1200&ch=750")
    hello2 = ginza(hello)
    # hello3 = get_image(top_key,hello2)
    #hello4 = great_img(top_key,hello2)
    return jsonify({"top_key":top_key,"get_key":hello2})