#!/usr/bin/python
from selenium import webdriver
import time

def init_phantomjs_driver(*args, **kwargs):
    headers = {
       'Connection': 'keep-alive',
       'Cache-Control': 'max-age=0',
       'Upgrade-Insecure-Requests': '1',
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
   }



    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

    #driver =  webdriver.PhantomJS(*args, **kwargs)
    driver =  webdriver.PhantomJS()
   # driver.set_window_size(1400,1000)
#    driver.set_window_size(1124, 850)
    driver.set_window_size(1265, 360)

    return driver


def main():
    service_args = [
        '--proxy=127.0.0.1:9999',
        '--proxy-type=http',
        '--ignore-ssl-errors=true'
        ]

    driver = init_phantomjs_driver()

    driver.get('https://www.similarweb.com/')
#    driver.get('http://www.baidu.com/')
    time.sleep(5)
    driver.save_screenshot("smlar.png") 
    print driver.page_source
#    data = driver.find_element_by_id("js-header").text

    driver.find_element_by_id("js-swSearch-input").send_keys(u'office.com')
    driver.find_element_by_class("swSearch-submit").click()
    print data
#    print driver.title
   # print driver.title
    
    #driver.save_screenshot("baidu.png")
    
 #   driver.find_element_by_id("kw").send_keys(u'great wall')
  #  driver.find_element_by_id("su").click()
   # driver.save_screenshot("getoffice.png")
   # print driver.page_source
    #print driver.get_cookies()
    time.sleep(2)
    driver.quit()

main()
