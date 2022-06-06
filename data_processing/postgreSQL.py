#!/usr/bin/python

from pprint import pprint
import psycopg2

class PostgreSQL_CRUD():
    def __init__(self, host, port, dbname, user, password):
        self.connect = psycopg2.connect(host=host, port=port, dbname = dbname, user=user, password=password)
        self.cursor  = self.connect.cursor()
    
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
                    tag_weight real[]);'''
        self.execute(query)
        self.commit()
        
    def insert(self, schema, table, title, link, img, tags):
        if len(tags) == 4:
            query = f"""insert into {schema}.{table} (title, link, img, tag, tag_weight)
                        values('{title}', '{link}', '{img}', 
                        ARRAY['{tags[0][0]}', '{tags[1][0]}', '{tags[2][0]}', '{tags[3][0]}'],
                        ARRAY[ {tags[0][1]} ,  {tags[1][1]} ,  {tags[2][1]} ,  {tags[3][1]} ])
                        on conflict(link)
                        do nothing"""
            try:
                self.execute(query)
                self.commit()
            except psycopg2.DatabaseError as error:
                print(error)
            
    def read(self, table):
        query = f"""select * from {table}"""
        self.execute(query)
        return self.cursor.fetchall()
