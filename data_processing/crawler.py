import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import lxml

url = "https://www.youtube.com/feed/trending"
session = HTMLSession()
page = session.get(url)
page.html.render()
soup = BeautifulSoup(page.html.html, 'lxml')
data = page.html.find('a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer')
data2 = page.html.find('yt-formatted-string#description-text.style-scope.ytd-video-renderer')

all_data = []
for i in data:
    test = list()
    test.append(i.attrs["title"])
    test.append(i.attrs["href"])
    all_data.append(test)

j = 0
for i in data2 :
    all_data[j].append(i.text)
    j += 1

for i in all_data:
    print(i)
