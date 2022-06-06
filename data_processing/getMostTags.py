import postgreSQL
from pprint import pprint



db = postgreSQL.PostgreSQL_CRUD(host="", port="",dbname="", user="",password="")

tag_info=[]
for i in range(1,4):
    db.execute(f"select tag[{i}], count(*) from kr.tablename group by tag")
    tag_info = tag_info+db.cursor.fetchall()
pprint(tag_info)

# db.create_table(schema= "KR",table="tablename")
# db.insert("KR","tablename", '제목2', '링크6','이미지2',[['aaa', 7.76], ['bbb', 7.76], ['ccc', 3.88], ['dd', 3.88]])
# pprint(db.read("kr.tablename"))