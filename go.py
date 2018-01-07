from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from driver.index import drivers

#options = webdriver.ChromeOptions()
#
#ug= 'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"'
#options.add_argument('lang=zh_CN.UTF-8')
#options.add_argument(ug)
#driver = webdriver.Chrome(chrome_options=options)
driver = drivers.chrome()
driver.set_window_size(1124, 850) # set browser size.
#add cookie
#cks={'domain': '.damai.cn', 'expiry': 1526024790, 'httpOnly': False, 'name': 'isg', 'path': '/', 'secure': False, 'value': 'AldXeiP9wakJ9kUlZYsdKan65s0NhaYw2m6GbKmEciaN2HUasWy7ThVqXE69'}
#cks =json.load(file.open('cks.json','rb'))
#print(type(cks))


###login
loginPage = 'https://secure.damai.cn/login.aspx?ru=https://www.damai.cn/'
driver.get(loginPage)
driver.find_element_by_id('login_email').send_keys('15555603375')
print('input account')
driver.find_element_by_id('login_pwd_txt').click()
driver.find_element_by_id('login_pwd').send_keys('19961118z')
print('input pwd')
driver.find_element_by_id('subbtn').click()
time.sleep(1)

###jump to ticket page
ticketPage = 'https://piao.damai.cn/135243.html?spm=a2o6e.rock.0.0.7ff45a7f3W9an9'

driver.get(ticketPage)
print('get ticket page')
driver.find_element_by_id('btnBuyNow').click()
print('jump to the pay page and sleep 1')
time.sleep(1)
driver.find_element_by_id('orderConfirmSubmit').click()
print('OK')
print('...')
driver.current_window_handle
### save cookies
#cks = open('cks','w')
#cks.write(str(driver.get_cookies()[0]))
#cks.close()
###    

###confirm
while 1:
    try:
        dropper = driver.find_element_by_class_name('nc_1_n1z')
        ActionChains(driver).drag_and_drop_by_offset(dropper,250,0).perform()
        break;
    except:
        pass
    


#while 1:
#    try:
#        driver.find_element_by_id('dom_id_td').drag_and_drop(0,250)
#        print('ok!')
#        break;
#    except:
#        pass
#driver.find_element_by_xpath('//button[@ma-on-click="@tongdunModal.onConfirm()"]').click()

