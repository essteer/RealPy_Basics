import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    time_tag = page.soup.select("#time")[0]
    roll_time = time_tag.text
    print(f"The result of your die roll is: {result}")
    print(f"The die was cast at: {roll_time}")

    if i < 3:
        time.sleep(5)
