#!/usr/bin/python

from data_processing.tf_idf import best_tags
from data_processing import postgreSQL

def get_tag(schema, table):

    db = postgreSQL.PostgreSQL_CRUD(host="255.255.255.255", port="0000",dbname="dbname", user="user",password="password")
    
    keywords = []
    for i in range(1,5):
        db.execute(f"select tag[{i}], tag_weight[{i}] from {schema}.{table} where tag_weight[{i}]>0.3")
        keywords.extend(db.cursor.fetchall())

    dic = {}
    for i in keywords:
        if i[0] in dic:
            dic[i[0]] = dic.get(i[0]) + i[1]
        else:
            dic[i[0]] = i[1]

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
    

    return best