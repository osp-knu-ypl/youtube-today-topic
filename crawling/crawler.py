import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import lxml

url = "https://www.youtube.com/feed/trending"
session = HTMLSession()
page = session.get(url)
page.html.render()

data = []
soup = BeautifulSoup(page.html.html, 'lxml')

title = soup.find('yt-formatted-string', class_="style-scope ytd-video-renderer")
data.append(title.text)
contents = soup.find('yt-formatted-string', id="description-text")
data.append(contents.text)
creator = soup.find('a', class_="yt-simple-endpoint style-scope yt-formatted-string")
data.append(creator.text)

link = soup.find('a', id="thumbnail", 
                class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail", rel="null")
plusurl = link.attrs["href"]
data.append(url + plusurl)
