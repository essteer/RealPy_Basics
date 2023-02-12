from bs4 import BeautifulSoup
from urllib.request import urlopen

# 1
url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

# 2
soup = BeautifulSoup(html, "html.parser")
anchors = soup.find_all("a")
for anchor in anchors:
    print(anchor["href"])

# 3
paths = [url + anchor["href"][9:] for anchor in anchors]
for path in paths:
    page = urlopen(path)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text())
