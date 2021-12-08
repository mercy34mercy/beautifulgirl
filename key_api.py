import requests
from bs4 import BeautifulSoup
import re
import random

from mecab_api import me

def get_key(top_key):

    
    jsons = requests.get("http://api.bing.com/osjson.aspx?market=ja-JP&query=%s" %(top_key)).text
    jsondatas =  re.findall('"([^"]*)"', jsons)
    
    
    for jsonda in jsondatas:
        print(jsonda)
        
        
    
    index = random.randint(0,len(jsondatas)-1)
    
    return jsondatas[index]
        