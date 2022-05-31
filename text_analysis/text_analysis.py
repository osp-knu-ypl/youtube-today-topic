#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':
 
    posTagger = Twitter()
    
    word = []
    data = []
    data.append('[아이유의 팔레트] 세븐틴이에유는 일촌이에유 (With 세븐틴) Ep.12')
    data.append("IU's Palette] SEVENTEENIU are friends now (With SEVENTEEN) Ep.12 [아이유의 팔레트] 세븐틴이에유는 일촌이에유 (With 세븐틴) Ep.12#아이유 #세븐틴 #팔레트")
    data.append("이지금 [IU Official]")
    
    for my_data in data:
        hsent = hfilter(my_data)
        print(hsent)
        wlist = posTagger.pos(hsent)
        print(wlist)
        print()
        for w in wlist:
            if w[1]=="Noun":  
                word.append(w[0])

    print(word)
        

