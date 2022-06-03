from pprint import pprint 
import psycopg2

class PostgreSQL_CRUD():
    def __init__(self, host, port, dbname, user, password):
        self.connect = psycopg2.connect(host=host, port=port, dbname = dbname, user=user, password=password)
        self.cursor = self.connect.cursor()
    
    def __del__(self):
        self.connect.close()
        self.cursor.close()
    
    def execute(self, query):
        self.cursor.execute(query)
    def commit(self):
        self.connect.commit()
    
    def create_table(self, schema, table):
        query = f'''create table {schema}.{table} (
            title varchar(255),
            link varchar(255) unique,
            img varchar(255),
            tag varchar(16)[],
            tag_weight real[]
        );'''
        self.execute(query)
        self.commit()
        return f"{schema}.{table}"

    def insert(self, schema, table, title, link, img, tags):
        query = f"""insert into {schema}.{table} (title, link, img, tag, tag_weight)
            values('{title}', '{link}', '{img}', ARRAY['{tags[0][0]}','{tags[1][0]}','{tags[2][0]}'], ARRAY[{tags[0][1]},{tags[1][1]},{tags[2][1]}])
            on conflict(link)
            do nothing
            """
        try:
            self.execute(query)
            self.commit()
        except psycopg2.DatabaseError as error:
            print(error)
            
    def read(self, table):
        query = f"""select * from {table}"""
        self.execute(query)
        return self.cursor.fetchall()

#example
db = PostgreSQL_CRUD(host="13.72.102.220", port="5432",dbname="youtube_trend", user="admin",password="qwe123")

#schema는 db에 미리 설정
db.create_table(schema= "KR",table="tablename")
db.insert("KR","tablename", '제목2', '링크2','이미지2',[['비행', 7.76], ['시험', 7.76], ['파일럿', 3.88], ['상황', 3.88]])
pprint(db.read("kr.tablename"))
