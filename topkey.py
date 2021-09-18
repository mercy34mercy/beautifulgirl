import random

def select_topkey():
    key = ["美女","JK","美人","アイドル"]
    select_int = random.randrange(3)
    a = key[select_int]
    print (a)
    return a