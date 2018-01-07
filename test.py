from selenium import webdriver
from driver.index import drivers
import time 

#####pj
#headers = { 'Accept':'*/*',
#    'Accept-Encoding':'gzip, deflate, sdch',
#    'Accept-Language':'en-US,en;q=0.8',
#    'Cache-Control':'max-age=0',
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
#}
#
#for key, value in enumerate(headers):
#    capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
#    webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value
#
#service_args = [
#    '--proxy=127.0.0.1:9999',
#    '--proxy-type=socks5',
#]    
#
#pj = webdriver.PhantomJS()
#
#
#
####chrome
#options = webdriver.ChromeOptions()
#ug= 'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"'
#options.add_argument('lang=zh_CN.UTF-8')
#options.add_argument(ug)
#chrome = webdriver.Chrome(chrome_options=options)
#
url ='https://piao.damai.cn/125066.html?spm=a2o6e.home.0.0.22ac3938KVGiGw'

driver = drivers.pj()


###main
driver.get(url)

driver.find_element_by_id('btnXuanzuo').click()
time.sleep(5)
pwd = chrome.find_element_by_id('layer').find_element_by_id('ulogin')
print(pwd)
#chrome.quit()
