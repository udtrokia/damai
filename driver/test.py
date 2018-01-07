from index import drivers

driver = drivers.pj()

driver.set_window_size(1124, 850) 
driver.get('https://www.baidu.com')
ht = driver.find_element_by_id('wrapper')
print(ht)
