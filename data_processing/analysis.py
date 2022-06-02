#!/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

def filter(list):
    posTagger = Twitter()
    word = []
    
    p_entry = hfilter(list)
    p_entry2 = posTagger.pos(p_entry)
    for i in p_entry2:
        if i[1]=="Noun":
            word.append(i[0])
    
    return word
