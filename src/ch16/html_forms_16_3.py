import mechanicalsoup

# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)
# page
# <Response [200]>
# type(page.soup)
# <class 'bs4.BeautifulSoup'>

#1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)
# http://olympus.realpython.org/profiles

# 4
base_url = "http://olympus.realpython.org"
links = profiles_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")

