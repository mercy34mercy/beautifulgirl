import MeCab
import random
 
def me(sent):
    mecab = MeCab.Tagger("-Ochasen")
    res = mecab.parseToNode(sent)
    meisi=[]

    while res:
        arr = res.feature.split(",")
        if (arr[0] == "名詞"):
            #名詞を取り出す
            meisi.append(arr[6])

        res = res.next

    index = random.randint(0,len(meisi)-1)
    return meisi[index]