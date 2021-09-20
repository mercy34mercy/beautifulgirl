import requests
from bs4 import BeautifulSoup
from requests.api import get
import random


def get_image(top_key,key):
    current_url = "https://www.google.com/search?q=" + top_key +"+" +key + \
        "&sxsrf=AOaemvI6vp0YKj-fyH9-T3r370jZUHhZgg:1630890428328&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjCjpellOnyAhUGCYgKHUcEA_QQ_AUoAXoECAEQAw"
    html = requests.get(current_url)
    bs = BeautifulSoup(html.text, 'lxml')
    images = bs.find_all('img', limit=10)
    # for image in images:
    #     # print image source
    #     print(image['data-src'])

    url_list = []
    for index in range(len(images)-1):
        
        image = images[index+1]
        try:
            url = image.get("src")
            url_list.append(url)
        except:
            print("EOF")
    
    if(len(url_list)==0):
        return "https://sports-pctr.c.yimg.jp/r/iwiz-amd/20210920-00010013-goal-000-1-view.jpg?h=1200&cx=0&cy=0&cw=1920&ch=1200"
    
    return url_list[random.randint(0,len(url_list)-1)]