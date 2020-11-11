import json
from selenium import webdriver

def getMyCookie(originHtml):
    browser = webdriver.Chrome()
    browser.get(originHtml)
    # button = driver.find_element_by_xpath(' // *[ @ id = "tipsButton"]')
    time.sleep(20)
    cookies = browser.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)

originHtml = "https://www.xuexi.cn"
getMyCookie(originHtml)