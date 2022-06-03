#!/usr/bin/python

import spacy

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

def filter(str):
    
    word = []
    nlp = spacy.load("ko_core_news_sm")
    p_entry = hfilter(str)
    doc = nlp(str)
    p_entry2 = list(doc)
    for i in p_entry2:
        if i.pos_=="NOUN":
            word.append(i)
    
    return word
