#!/usr/bin/python

import spacy
import re
from konlpy.tag import Twitter

# korean asterisk remover
def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

# title quotes remover
def titlefilter(s):
        return re.sub(u'[\"\']+','',s)

# not korean asterisk remover
def otherhfilter(s):
    return re.sub('[^ a-zA-Z]','',s).strip()

# not korean word extraction
def otherfilter(string, code):
    word      = []
    nlp       = spacy.load(code)
    p_string1 = otherhfilter(string)
    p_string2 = nlp(p_string1)
    p_string3 = list(p_string2)

    for i in p_string3:
        if i.pos_=="NOUN":
            word.append(i)

    return word

# word extraction
def filter(string, code):
    if(code == "KR"):
        word = []
        posTagger = Twitter()
        p_string1 = hfilter(string)
        p_string2 = posTagger.pos(p_string1)

        for i in p_string2:
            if i[1] == "Noun":
                word.append(i[0])     
        
        return word                                    
    else:
        otherfilter(string, code)
