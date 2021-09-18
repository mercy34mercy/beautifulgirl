import requests
from bs4 import BeautifulSoup
import re
import random

def get_key(top_key):
    # 100ランク取得
    load_url = "https://www.google.co.jp/search?hl=ja&source=hp&q=" + \
        top_key+"&ie=utf-8&oe=utf-8&num=101"

    # HTML取得
    html = requests.get(load_url)
    web_data = BeautifulSoup(html.content, "html.parser")
    list = web_data.findAll(True, {'class': 'BNeawe vvjwJb AP7Wnd'})

    for i in range(1):
        # 10ランク取得
        pagenum = random.randint(1,30)
        load_url = "https://search.yahoo.co.jp/search?p="+top_key + "&ei=utf-8&b=" + \
                str(pagenum)

        # HTML取得
        html = requests.get(load_url)
        web_data = BeautifulSoup(html.content, "html.parser")
        list = web_data.findAll('a')

        # 獲得したテキストから、indexを作成
        result_title = []
 

        pattern = "(.*)clear.gif(.*)"
        # ランキング表示
        for ls in list:
            if str(ls).find('clear.gif') != -1:
                d = re.search(pattern, str(ls))
                a = d.group(2)
                a = a.replace("<b>", "")
                a = a.replace("</b>", "")
                a = a.replace(""""""">", "")
                a = a.replace("</a", "")

                result_title.append(a.strip('|'))

    if(len(result_title) <=  5):
        return "EOF"

    
    return result_title[random.randint(0,len(result_title)-1)]
