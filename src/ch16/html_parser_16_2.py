from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
soup.find_all("img")
image1, image2 = soup.find_all("img")
# image1.name
# 'img'
# image1["src"]
# '/static/dionysus.jpg'
# soup.title
# <title>Profile: Dionysus</title>
# soup.title.string
# 'Profile: Dionysus'

soup.find_all("img", src="/static/dionysus.jpg")
# [<img src="/static/dionysus.jpg"/>]
