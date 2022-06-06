import postgreSQL
from pprint import pprint

def get_tag(schema, table):
    db = postgreSQL.PostgreSQL_CRUD(host="", port="",dbname="", user="",password="")
    tag_info=[]
    test = []
    for i in range(1,5):
        db.execute(f"select tag[{i}], count(*) from {schema}.{table} group by tag")
        test.extend(db.cursor.fetchall())

    dic = {}
    for i in test:
        if i[0] in dic:
            dic[i[0]] = dic.get(i[0]) + 1
        else:
            dic[i[0]] = 1

    one_table = []
    for i in range(0, 5):
        maxkey = max(dic, key=dic.get)
        key = maxkey
        value = str(dic.get(maxkey))
        data_1 = []
        data_1.append(key)
        data_1.extend(value)
        del(dic[maxkey])
        one_table.append(data_1)
    
    print(one_table)
    return one_table
