from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
while driver.find_element_by_xpath('//body'):
    print('go')
    break;

driver.quit()
