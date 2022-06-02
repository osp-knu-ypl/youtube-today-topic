from math import log
import collections
from pprint import pprint

import pandas as pd


youtubes = [['apple', 'apple', 'apple', 'banana', 'banana', 'cherry', 'banana', 'cherry', 'cherry'],
         ['a', 'banana', 'c'],
         ['b', 'fadf', 'banana', 'asdfgasd']]

def analysis_content(docs):
    doc_info = {}
    for doc in docs:
        counts = collections.Counter(doc)
        
        for word, freq in zip(counts.keys(), counts.values()):
            doc_info[word] = freq
    return doc_info

def extract_word(docs):
    return  list(set(word for doc in docs for word in doc))

N = len(youtubes)

def tf(t, d):
    return d.count(t)

def idf(t, docs):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df+1))

def tfidf(t, d, docs):
    return tf(t,d)* idf(t, docs)

word_frequency = analysis_content(youtubes)
print(word_frequency)

word_list = extract_word(youtubes)
print(word_list)

result = []
for i in range(N):
    result.append([])
    d = youtubes[i]
    for j in range(len(word_list)):
        t = word_list[j]
        result[-1].append(tfidf(t,d, youtubes))
tfidf_ = pd.DataFrame(result, columns=word_list)
print(tfidf_)
print(word_list)
pprint(result)

