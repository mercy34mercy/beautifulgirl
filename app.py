# -*- coding: utf-8 -*-

from flask import Flask, render_template
from key_api import get_key
from image_api import get_image
from mecab_api import me
from topkey import select_topkey
from test import great_img
from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/hello')
def indexs():
    return 'hello'


@app.route('/url', methods=['POST','GET'])
def hello():
    top_key = "美女"
    try:
        if request.method == 'POST':
            top_key = request.json['quali']
            num = request.json["num"]
        elif request.method == 'GET': 
            top_key = "美女"
    except:
        return jsonify({"top_key":"EOF","get_key":"EOF"})
    hello = get_key(top_key)
    if(hello == "EOF"):
        return jsonify({"top_key":"EOF","get_key":"EOF"})
    # hello2 = me(hello)
    return jsonify({"top_key":top_key,"get_key":hello})