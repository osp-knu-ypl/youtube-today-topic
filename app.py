from data_processing import getMostTags
from flask import Flask, render_template, request
import json



from data_processing import postgreSQL

db = postgreSQL.PostgreSQL_CRUD(host="255.255.255.255", port="0000",dbname="dbname", user="user",password="password")

def getJsonGraphData(data):
    temp = []
    for l2 in data:
        for l1 in l2:
            temp.append(l1[0])
    category=set(temp)
    rank = {}
    for tag in category:
        rank[tag]=[]
        
    for tag in category:
        for doc in data:
            check = 0
            for i in range(0,5):
                if tag in doc[i]:
                    check = check+1
                    rank[tag].append(5-i)
            if check == 0:
                rank[tag].append(-1)
        
    
    return json.dumps(rank, ensure_ascii=False)

def getTableList(Country_Code):
    # kr/us
    db.execute(f"select table_name from information_schema.tables where table_schema='{Country_Code}' order by table_name DESC limit 12;")
    table_list =[]
    for table in db.cursor.fetchall():
        table_list.append(table[0])
    return table_list


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/method/', methods=['GET', 'POST'])
def method():
    return "method"

@app.route('/Global/Korea/', methods=['GET', 'POST'])
def korea():
    nation = 'kr'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/KR.html', youtube_list=youtube_list,table_list=table_list, rank = rank)


@app.route('/Global/USA/', methods=['GET', 'POST'])
def usa():
    nation = 'us'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/USA.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/Global/Japan/', methods=['GET', 'POST'])
def jp():
    nation = 'jp'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/JP.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/Global/Italy/', methods=['GET', 'POST'])
def it():
    nation = 'it'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/IT.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/Global/Greece/', methods=['GET', 'POST'])
def gr():
    nation = 'gr'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/GR.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/Global/France/', methods=['GET', 'POST'])
def fr():
    nation = 'fr'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/FR.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/Global/Spain/', methods=['GET', 'POST'])
def es():
    nation = 'es'

    tags = []
    table_list =getTableList(nation)

    for table in table_list:
        tags.append(getMostTags.get_tag(nation, table))
    rank = getJsonGraphData(tags)

    youtube_list = []
    for i in range(0,5):
        db.execute(f"select * from {nation}.{table_list[0]} where '{tags[0][i][0]}'=any(tag)")
        youtube_list.append(db.cursor.fetchall())
    return render_template('/Global/ES.html', youtube_list=youtube_list,table_list=table_list, rank = rank)

@app.route('/creators/', methods=['GET', 'POST'])
def creators():
    return render_template('/creators.html')

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요", 404



if __name__ == '__main__':
    app.run(debug=True)