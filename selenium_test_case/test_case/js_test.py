'''
@author:xvnmeng
@datetime:2018/8/21 22:25
@software:PyCharm Community Editon
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.set_window_size(600, 600)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# js设置窗口滚动条位置
js = 'window.scrollTo(100,450);'
driver.execute_script(js)
sleep(3)

# js输入文本
js = "var sum = document.getElementById('id'); sum.value= '' + text + ''; "
driver.execute_script(js)

driver.quit()