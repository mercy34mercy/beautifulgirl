import requests
from bs4 import BeautifulSoup
import re
import random

from mecab_api import me

def get_key(top_key):
    # # 100ランク取得
    # load_url = "https://www.google.co.jp/search?hl=ja&source=hp&q=" + \
    #     top_key+"&ie=utf-8&oe=utf-8&num=101"

    # # HTML取得
    # html = requests.get(load_url)
    # web_data = BeautifulSoup(html.content, "html.parser")
    # list = web_data.findAll(True, {'class': 'BNeawe vvjwJb AP7Wnd'})
    '''
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

    if(len(result_title) <=  4):
        return "関連画像"
    '''
    
    #index = random.randint(0,len(result_title)-1)
    
    while(1):
        try:
            #return_key = me(result_title[index])
            return_key = me("私の名前は小林雅史です、サッカー")
            break
        except:
            i = 0

    
    return return_key
