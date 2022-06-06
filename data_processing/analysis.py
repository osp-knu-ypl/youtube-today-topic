#!/usr/bin/python

import spacy
import re
from konlpy.tag import Twitter

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

def titlefilter(s):
        return re.sub(u'[\"\']+','',string)

def otherhfilter(s):
    return re.sub('[^ a-zA-Z]','',s).strip()

def filter(str, code):

        if(code == "KR"):
            word = []
            posTagger = Twitter()
            p_entry = hfilter(str)
            p_entry2 = posTagger.pos(p_entry)

            for i in p_entry2:
                if i[1] == "Noun":                                                                  word.append(i[0])     
            return word                                    
        else:
            otherfilter(str,code)

def otherfilter(str, code):

    word = []
    nlp = spacy.load(code)
    p_entry = otherhfilter(str)
    doc = nlp(str)
    p_entry2 = list(doc)
    
    for i in p_entry2:
        if i.pos_=="NOUN":
            word.append(i)

    return word

