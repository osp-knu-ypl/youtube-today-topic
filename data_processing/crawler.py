#!/usr/bin/python

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import lxml
import analysis
import tf_idf
from postgreSQL import PostgreSQL_CRUD

# video URL + Country code
trendurl     = "https://www.youtube.com/feed/trending"
youtube_url  = "https://www.youtube.com"
country_code = "?gl=KR"
url = trendurl + country_code

# page download
session = HTMLSession()
page_data = session.get(url)
page_data.html.render(sleep=1, keep_page=True)

# extract information
soup = BeautifulSoup(page_data.html.html, 'lxml')
titles   = page_data.html.find('a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer'    )
contents = page_data.html.find('yt-formatted-string#description-text.style-scope.ytd-video-renderer')

# crawling once
# tf_idf_tags = analysis list
table = []
tf_idf_tags = []
j = 0
for i in titles:
    # each video
    video  = list()
    title  = i.attrs["title"]
    link   = i.attrs["href" ]
    i_link = link[9:]
    link   = youtube_url + link
    img    = f'https://img.youtube.com/vi/{i_link}/0.jpg'
    tag    = analysis.filter(title)

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

# contents anlysis
j = 0
for i in contents:
    content = analysis.filter(i.text)
    tf_idf_tags[j].extend(content)

    if j > 48:
        break
    j += 1

# tf-idf execution
j = 0
tf_idf_tags = tf_idf.best_tags(tf_idf_tags)
for i in tf_idf_tags:
    table[j].append(i)
    j += 1

print(table)
# db = PostgreSQL_CRUD(host="20.124.236.237", port="5432", dbname="youtube_trend", user="administrator", password="qwer1234")

# db.create_table(schema="KR", table="220604")
# for i in table:
#     db.insert("KR", "220604", i[0], i[1], i[2], i[3])
