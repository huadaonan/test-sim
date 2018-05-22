#!/usr/bin/python
import time
import requests
from http.cookies import SimpleCookie
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
import os


#chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"')

##proxy


###custom cookie




#define chrome driver path
def get_proxy():
    return requests.get("http://47.91.217.49:8080/get/").content

def delete_proxy(proxy):
    requests.get("http://47.91.217.49:8080//delete/?proxy={}".format(proxy))

# your spider code

def getHtml(domain_name):
    # ....
#    proxy = get_proxy()
 #   chrome_options.add_argument("--proxy-server=http://{}".format(proxy))
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument("--window-size=1920x1080") # windows size import for reverse scrapy
    #chrome_options.add_argument("--window-size=360x640") # windows size import for reverse scrapy
    chrome_options.add_argument('Connection=keep-alive')
    chrome_options.add_argument('Cache-Control="max-age=0"')
    chrome_options.add_argument('Upgrade-Insecure-Requests=1')
    chrome_options.add_argument('Accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"')
    chrome_options.add_argument('User-Agent="Samsung Galaxy S4=Mozilla/5.0 (Linux; Android 4.2.2; GT-I9300 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36"')
    chrome_options.add_argument('Referer="https://account.similarweb.com/login"')
    
    retry_count = 5
    while retry_count > 0:
        try:
           # html = requests.get('http'.format(domain_name),headers=headers, cookies=cookies,proxies={"http": "http://{}".format(proxy)})
	    #requests.get('https://widget.similarweb.com/smlrdstl.js?PID=2CF818FC-9807-35AF-8423-9832CC464303')
	    chrome_driver = "/root/selemium/chromedriver"
	    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
	    driver.get("https://publicwww.com/")
            domain_name = "\"" + domain_name.strip('\n') + "\""
	    print domain_name
            driver.find_element_by_id("maininput").send_keys(domain_name)
            driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
 #           time.sleep(1)
	    filename = domain_name + ".png"
#            driver.save_screenshot(filename)
            data = driver.find_element_by_xpath("//div[@class='col-xs-8']/h4").text
    	    driver.quit()
            return data
	    #print driver.page_source
           # return driver
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    return None

f = open('expiredomain_check.txt','a')
for domain in open("domainlist1.txt"):
	number = getHtml(domain)
	data_result =  domain.strip('\n') + " link number:" + str(number) + '\n'
        f.write(data_result)
	print data_result


