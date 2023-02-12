import re
from urllib.request import urlopen

# 1
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

# 2 with .find()
for tag in ["Name: ", "Color: "]:
    start_index = html.find(tag) + len(tag)
    end_index = html[start_index:].find("<")
    print(html[start_index:start_index + end_index].strip())

# name_index = html.find("Name: ")
# end_index = html[name_index:].find("<")
# start_index = name_index + len("Name: ")
# print(html[start_index:end_index])
#
# color_index = html.find("Favorite Color: ")
# end_index = html.find("</center>")
# start_index = color_index + len("Favorite Color: ")
# print(html[start_index:end_index])

# 3 with regex
for tag in ["Name:\s*.*?[\n<]", "Color:\s*.*?[\n<]"]:
    match_results = re.search(tag, html)
    result = re.sub(".*:\s*", "", match_results.group())
    print(result.strip(" \n<"))

name_pattern = "Name:\s*(\w*)\s*<"
match_results = re.search(name_pattern, html, re.IGNORECASE)
name = match_results.group(1)
print(name)
# name = re.sub("<.*?>", "", title)  # Remove HTML tags

color_pattern = "Color:\s*(\w*)\s*<"
match_results = re.search(color_pattern, html, re.IGNORECASE)
color = match_results.group(1)
print(color)
