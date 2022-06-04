# -*- coding: utf-8 -*-

from math import log
import collections
from pprint import pprint

def analysis_content(docs):
    doc_info = {}
    for doc in docs:
        counts = collections.Counter(doc)
        
        for word, freq in zip(counts.keys(), counts.values()):
            doc_info[word] = freq
    return doc_info

def extract_word(docs):
    return  list(set(word for doc in docs for word in doc))

def tf(t, d):
    return d.count(t)

def idf(t, docs):
    df = 0
    for doc in docs:
        df += t in doc
    N = len(docs)
    return log(N/(df+1))

def tfidf(t, d, docs):
    return tf(t,d)* idf(t, docs)

def best_tags(docs):

    N = len(docs)
    word_frequency = analysis_content(docs)

    word_list = extract_word(docs)

    result = []
    for i in range(N):
        result.append([])
        d = docs[i]
        for j in range(len(word_list)):
            t = word_list[j]
            result[-1].append(tfidf(t,d, docs))

    best_tags = []
    
    for i in range(N):
        best_tags.append([])
        temp = {}
        for j in range(len(word_list)):
            if result[i][j]>0 and len(word_list[j])>1:
                temp[word_list[j]]=result[i][j]
        sorted_temp = sorted(temp.items(), key = lambda item: item[1], reverse = True)
        try: 
            for word in sorted_temp[:4]:
                temp = []
                temp.append(word[0])
                temp.append(word[1])
                best_tags[-1].append(temp)
        except : print("e")

    for tags in best_tags:
        for tag in tags:
            tag[1] = round(tag[1],2)
    return best_tags
