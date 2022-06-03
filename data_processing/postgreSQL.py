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
    
    def create_table(self, table):
        query = f'''create table {table} (
            title varchar(255),
            link varchar(255) unique,
            img varchar(255),
            tag varchar(16)[]
        );'''
        self.execute(query)
        self.commit()
        return table

    def insert(self, table, title, link, img, tag):
        query = f"""insert into {table} (title, link, img, tag)
            values('{title}', '{link}', '{img}', ARRAY['{tag[0]}','{tag[1]}','{tag[2]}'])
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

        

db = PostgreSQL_CRUD(host="255.255.255.255", port="00000",dbname="dbname", user="user",password="password")
# db.create_table(table="date1")
db.insert("date1", '제목2', '링크2','이미지2',['태그21', '태그22','태그23'])

pprint(db.read("date1"))
