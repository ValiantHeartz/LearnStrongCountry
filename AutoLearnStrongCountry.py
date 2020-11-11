import json
from selenium import webdriver
#import myCookie
import random
import time
if __name__ == '__main__':
    ## 获取cookies
    browser = webdriver.Chrome()
    browser.get('https://pc.xuexi.cn/points/login.html')
    #button = driver.find_element_by_xpath(' // *[ @ id = "tipsButton"]')
    time.sleep(20)
    '''
    while(1):
        if browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div/a[1]/div/div[1]"):
            break
    '''
    cookies = browser.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)



    pictureHtml = "https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#KT6r-MbR7N"
    paperHtml = "https://www.xuexi.cn/261c9a142ef8e6375ed554815a26d585/f2d8ff735982530b7a8c9bb90fa99f68.html"
    #myCookie.getMyCookie(originHtml)
    ## 用cookies登陆
    browser.implicitly_wait(10)
    browser.get(pictureHtml)
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            # cookie.pop('domain')  # 如果报domain无效的错误
            browser.add_cookie(cookie)
    browser.get(pictureHtml)

    ## 视频任务
    x_path = "/html/body/div/div/div/section/div/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div/div\
/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div\
[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/section/div[3]/section/\
div/div/div[1]/div["

    for i in range(3):
        for j in range(2):
            print(x_path + str(i+1) + ']/div[' + str(j+1) + ']')
            browser.find_element_by_xpath(x_path + str(i+1) + ']/div[' + str(j+1) + ']').click()
            time.sleep(random.randint(70,80))
            handles = browser.window_handles
            browser.switch_to.window(handles[1])
            browser.close()
            browser.switch_to.window(handles[0])

    ## 文章任务
    browser.get(paperHtml)
    x_path = "/html/body/div[1]/div/div/section/div/div/div/div/div[4]/section/div/div/div/div/div/section[3]/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div["
    line = 1
    for i in range(7):
        if i + 1 > 4:
            line = 2
            i = i - 4
        print(x_path + str(line) + ']/div[' + str(i + 1) + ']')
        browser.find_element_by_xpath(x_path + str(line) + ']/div[' + str(i+1) + ']').click()
        time.sleep(random.randint(60, 70))
        handles = browser.window_handles
        browser.switch_to.window(handles[1])
        browser.close()
        browser.switch_to.window(handles[0])
    browser.close()

