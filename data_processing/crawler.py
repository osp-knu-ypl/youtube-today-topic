#!/usr/bin/python

import sys
import lxml
import analysis
import tf_idf
from pprint        import pprint
from postgreSQL    import PostgreSQL_CRUD
from requests_html import HTMLSession

# video URL + Country code
trendurl     = "https://www.youtube.com/feed/trending"
youtube_url  = "https://www.youtube.com"
country_code = "?gl=" + sys.argv[1]
url          = trendurl + country_code

print("crawling start")
# page download
session = HTMLSession()
page_data = session.get(url, timeout=5)
page_data.html.render()
print("rendering success")

# extract information
titles   = page_data.html.find('a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer'    )
contents = page_data.html.find('yt-formatted-string#description-text.style-scope.ytd-video-renderer')
views    = page_data.html.find('span.style-scope.ytd-video-meta-block')
print("crawling success")

# crawling once
# tf_idf_tags = analysis list
table = []
tf_idf_tags = []

j = 0
for i in titles:
    # each video
    video     = list()
    title     = analysis.tfilter(i.attrs["title"])
    link      = i.attrs["href"]
    thumbnail = link[9:]
    link      = youtube_url + link
    img       = f'https://img.youtube.com/vi/{thumbnail}/0.jpg'
    tag       = analysis.filter(title, sys.argv[3], sys.argv[1])

    # add element
    video.append(title)
    video.append(link)
    video.append(img)
    tf_idf_tags.append(tag)

    # add one video
    table.append(video)

    if j > 48:
        break
    j += 1
print("title analysis success")

# contents anlysis
j = 0
for i in contents:
    content = analysis.filter(i.text, sys.argv[3], sys.argv[1])
    tf_idf_tags[j].extend(content)

    if j > 48:
        break
    j += 1
print("content analysis success")

viewlist = []
j = 0
for i in views:
    j += 1
    if j % 2 == 0:
        continue

    tview = []
    tview = i.text
    view = tview[4:-2]
    dview = float(view)
    viewlist.append(dview)
print("views success")

# tf-idf execution
j = 0
zero_list = ["0", 0]
tf_idf_tags = tf_idf.best_tags(tf_idf_tags, viewlist)
for i in tf_idf_tags:
    while len(i) < 4:
        i.append(zero_list)
    table[j].append(i)
    j += 1
print("tf-idf success")


# table confirm
for i in table:
    j += 1
    print(i[3])

db = PostgreSQL_CRUD(host="", port="", dbname="", user="", password="")
db.create_table(schema=sys.argv[1], table="T"+sys.argv[2])
for i in table:
    db.insert(sys.argv[1], "T"+sys.argv[2], title=i[0], link=i[1], img=i[2], tags=i[3])