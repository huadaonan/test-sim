#!/usr/bin/python
from selenium import webdriver
from http.cookies import SimpleCookie
import time

def init_phantomjs_driver(*args, **kwargs):

#    headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 #       'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
  #      'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
       # 'Connection': 'keep-alive'
    #}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

    #driver =  webdriver.PhantomJS(*args, **kwargs)
    driver =  webdriver.PhantomJS()
   # driver.set_window_size(1400,1000)
#    driver.set_window_size(1124, 850)
    #driver.set_window_size(360, 640)
    driver.maximize_window() 
    return driver


def get_cookie():
	rawdata = 'Cookie: loyal-user=%7B%22date%22%3A%222018-05-12T04%3A30%3A59.373Z%22%2C%22isLoyal%22%3Atrue%7D; _vwo_uuid=A4EAD63D4759D20F78F2E22B9D4BE71B; trd_taskrestricted=; trd_first_visit=1507570314; trd_exitintentclient=1507570314368367; trd_pw=2; trd_cid=15075703139099080; sgID=263641cd-8318-4947-8039-c74a294eff22; _vis_opt_exp_260_exclude=1; _vis_opt_exp_255_combi=2; D_IID=3D5A4FA2-C566-3434-AC43-F10B499A2230; D_UID=D01B6064-9D81-30F1-A441-5054F4ABCDE0; D_ZID=93C7CCFD-0D15-3DFB-B549-1951CF242627; D_ZUID=FF514C96-FAD5-3A54-86A5-AFD02E94C7FC; D_HID=49DFE008-1565-330B-B9AC-B0ADB009A49B; D_SID=45.76.28.153:/Nzu6LDhp6R3Y5efDOTbIbiSGfZEJ3kizPaMOF2YrqQ; locale=en-US; __RequestVerificationToken=YFdx_d81Af3EDErZ6lM3x6LD3yciPMZyWXH3F7ZJf6wLCWRBipT7tE0Gozi9GeWQDWrBGgHO21rWkixwcoZFJIf7Emxq2Ayw9IDYr_ITgPA1; _ga=GA1.2.874349278.1526099459; _gid=GA1.2.777598502.1526099459; loyal-user=%7B%22date%22%3A%222018-05-12T04%3A30%3A59.373Z%22%2C%22isLoyal%22%3Afalse%7D; _vwo_uuid_v2=DBDB7357C24BC71D552F0B578C8A3F197|6d3ff8c62c7f32d06b16159f91eec16d; user_num=nowset; _pk_ref.1.fd33=%5B%22addon%22%2C%22%22%2C1526099460%2C%22%22%5D; _mkto_trk=id:891-VEY-973&token:_mch-similarweb.com-1526099473536-29989; intercom-id-e74067abd037cecbecb0662854f02aee12139f95=27cdf974-9d48-4f7a-aa42-16455a787a1d; __utma=107333120.874349278.1526099459.1526100726.1526100726.1; __utmc=107333120; __utmz=107333120.1526100726.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); PHPSESSID=jkci3guc10omhq9fjf6i5eq9j2; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; _vis_opt_exp_255_goal_4=1; jaco_uid=5de91f4b-b6f4-4e05-847d-737b09f7b8d0; jaco_provided_id_4316adc2-eb98-4130-828f-0352f2dac395=huadaonan%40gmail.com; intercom-lou-e74067abd037cecbecb0662854f02aee12139f95=1; __zlcmid=mNhKmmGKf9tyo1; .SGTOKEN.SIMILARWEB.COM=6LeIiEAwnfhtJctdwGsD8pdAGJV2BHonCwciV-cPEH3nQ734BjfLEA9UhY8s5QANhWl8uO52Y9J98r5y4bOiLcIorzVjPM-6r-R40fHlDkKKYpI8S0vKD-K0XbayIqyVRLvbMO6hDGulQhBiWgHX9uSjkLtq46nFK0ddVTWnSXP8TcLn-LkAEXbJM5pJX1aG0G5TbKzSBadwn_S7_Z7cSuXwJvocROtOddbMKB0v7cUmMZra1kSD1TOaxRaX-lwvnoI9lMnSqzwbBzB2ObQ5aVBLZFLXA-vzFUcVvSwqRUzORwpjdNeJ7ZKKk5RshGPN; _pk_ses.1.fd33=*; _uetsid=_uet297f6025; sc_is_visitor_unique=rx8617147.1526107124.2D16D2A6BEC44FE75868E7DDBCA586A5.4.3.3.3.3.3.3.3.3; _pk_id.1.fd33=ba4b06e8cc804c6a.1526099460.2.1526107125.1526106068.; intercom-session-e74067abd037cecbecb0662854f02aee12139f95=cHZBdGZ4N0lhbzIydnhKb3I2QXBUdDd3OUMrZWZnT3ovRFd4ZzdUUktaMHN1UlhneTd3cndvSzMwNy8ySm9ici0tVG1HcFE4YXh0eUdBQ2FXUXZUYndoQT09--b42819aff536d8c1e6a38398bfb5f17251651423;'
	
	cookie = SimpleCookie()
	cookie.load(rawdata)
	cookies = {}
	for key,morsel in cookie.items():
		cookies[key] = morsel.value
        cookies['domain'] = '.similarweb.com'
	return cookies


def main():
    service_args = [
        '--proxy=127.0.0.1:9999',
        '--proxy-type=http',
        '--ignore-ssl-errors=true'
        ]

    driver = init_phantomjs_driver()
    cookies  = get_cookie()
    print cookies
    driver.get('http://www.similarweb.com')
    driver.delete_all_cookies()
    driver.add_cookie(cookies)
    time.sleep(3)
#    data = driver.find_element_by_id("wrapper").text
#    print(driver.get_cookies())
 #   driver.delete_all_cookies()
    #driver.add_cookies()
  #  print data
  #  print driver.title
    
    driver.save_screenshot("similarweb.png")
#    print(driver.page_source)
    driver.find_element_by_id("js-swSearch-input").send_keys(u'sina.com')
    time.sleep(2)
    driver.find_element_by_class_name("swSearch-submit").click()
    time.sleep(2)
   # driver.find_element_by_id("kw").send_keys(u'great wall')
   # driver.find_element_by_id("su").click()
    driver.save_screenshot("sina.png")
    print(driver.page_source)
    time.sleep(1)
    #print driver.get_cookies()
    driver.quit()

main()
