#!/usr/bin/python

from data_processing import postgreSQL
from pprint import pprint

def get_tag(schema, table):
    db = postgreSQL.PostgreSQL_CRUD()
    
    keywords = []
    for i in range(1,5):
        db.execute(f"select tag[{i}], tag_weight[{i}] from {schema}.{table} where tag_weight[{i}]>6")
        keywords.extend(db.cursor.fetchall())

    dic = {}
    for i in keywords:
        if i[0] in dic:
            dic[i[0]] = dic.get(i[0]) + 1
        else:
            dic[i[0]] = 1

    best = []
    for i in range(0, 5):
        maxkey = max(dic, key = dic.get)
        key = maxkey
        value = str(dic.get(maxkey))
        
        data_1 = []
        data_1.append(key)
        data_1.extend(value)
        
        del(dic[maxkey])
        best.append(data_1)
    
    print(best)
    return best
