#!/usr/bin/python

import spacy
import re
from konlpy.tag import Twitter

# korean asterisk remover
def hfilter(s):
    return re.sub(u'[^ \u3130-\u318f\uac00-\ud7a3]+','',s)

# title quotes remover
def tfilter(s):
        return re.sub(u'[\"\']+','',s)

# not korean asterisk remover
def otherhfilter(s, nacode):
    if nacode == "US":
        return re.sub('[^ a-zA-Z]','',s).strip()
    elif nacode == "JP":
        return re.sub('u[^ \u3040-\u309F\u30A0-\u30FF]','',s)
    else:
        return re.sub(u'[\@\#\$\%\&\*\(\)\=\+\_\-\.\,\?\]\[\!]','',s)

# not korean word extraction
def otherfilter(string, code, nacode):
    word      = []
    nlp       = spacy.load(code)
    p_string1 = tfilter(otherhfilter(string, nacode).lower())
    p_string2 = nlp(p_string1)
    p_string3 = list(p_string2)

    for i in p_string3:
        if i.pos_=="NOUN" and len(i) < 16:
            word.append(i)

    return word

# word extraction
def filter(string, code, nacode):
    if(code == "KR"):
        word = []
        posTagger = Twitter()
        p_string1 = hfilter(string)
        p_string2 = posTagger.pos(p_string1)

        for i in p_string2:
            if i[1] == "Noun" and len(i[0]) < 16:
                word.append(i[0])     
        
        return word                                    
    else:
        return otherfilter(string, code, nacode)
