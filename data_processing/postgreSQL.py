from pprint import pprint 
from click import password_option
import psycopg2

def write(n, title, price, item, category, link, picturelink):

    table = "schema.table"

    # DB 접속
    try:
        with psycopg2.connect(host="255.255.255.255", port="00000", dbname="dbname", user="user", password="password") as conn:
            with conn.cursor() as cur:
                #title과 link 중 하나라도 같으면 DB에 추가하지 않음
                for i in range(n):
                    cur.execute(f"""INSERT INTO {table} (TITLE, PRICE, ITEM, CATEGORY, LINK, PICTURELINK)
                    VALUES ('{title[i]}', '{price[i]}', '{item[i]}', '{category[i]}', '{link[i]}', '{picturelink[i]}')
                    ON CONFLICT (LINK)
                    DO NOTHING
                    """)
                
                cur.execute(f"select * from {table}" )
                print(f"SELECT * FROM {table}")
                pprint(cur.fetchall())
    except psycopg2.DatabaseError as e:
        print(e)


#write(1,['title5'], [20], ['Galaxy tab S8 Ultra'], ['Tablet'], ['http://...0'], ['https://picture...']) 
