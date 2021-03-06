from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}


class drivers:
    #chrome
    def chrome():
        options = webdriver.ChromeOptions()
        ug= 'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"'
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(ug)
        chrome = webdriver.Chrome(chrome_options=options)
        return chrome

    #phantomjs
    def pj():
        for key, value in enumerate(headers):
            capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
            webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.loadImages"] = False
            service_args = ['--proxy=127.0.0.1:9999','--proxy-type=socks5']
            pj = webdriver.PhantomJS(desired_capabilities=dcap)
            #pj = webdriver.PhantomJS()
        return pj
            
