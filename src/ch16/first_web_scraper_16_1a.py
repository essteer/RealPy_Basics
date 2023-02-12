from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
# page
# <http.client.HTTPResponse object at 0x0000019706BC73D0>
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)
#  ...
title_index = html.find("<title>")
print(title_index)
# 14
start_index = title_index + len("<title>")
# 21
end_index = html.find("</title>")
print(end_index)
# 39
title = html[start_index:end_index]
print(title)
# Profile: Aphrodite
