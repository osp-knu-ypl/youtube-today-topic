#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

def analysis(data = [])
 
    posTagger = Twitter()
    
    word = []
        
    for my_data in data:
        hsent = hfilter(my_data)
        print(hsent)
        wlist = posTagger.pos(hsent)
        print(wlist)
        print()
        for w in wlist:
            if w[1]=="Noun":  
                word.append(w[0])

    return word
        

