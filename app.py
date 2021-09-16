# -*- coding: utf-8 -*-
from flask import Flask
from key_api import get_key
from image_api import get_image
from ginza_jp_api import ginza

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/hello')
def indexs():
    return 'hello'


@app.route('/url')
def hello():
    top_key = '美女'
    hello = get_key(top_key)
    hello2 = ginza(hello)
    hello3 = get_image(hello2)
    return hello3



