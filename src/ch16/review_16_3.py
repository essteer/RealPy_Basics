import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 2
post_login_page = browser.submit(form, login_page.url)
print(f"Title: {post_login_page.soup.title.text}")

# 3
login_page = browser.get(url)
login_html = login_page.soup
login_title = login_html.title
print(f"Title: {login_title.text}")

# 4
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "thor"
form.select("input")[1]["value"] = "HammerDude"

post_login_page = browser.submit(form, login_page.url)
post_login_html = post_login_page.soup

if post_login_html.find_all("Wrong username or password!") is not None:
    print("You entered the wrong username and/or password.")
#
# if error_page.soup.text.find("Wrong username or password!") != -1:
#     print("Login Failed.")
# else:
#     print("Login Successful.")
