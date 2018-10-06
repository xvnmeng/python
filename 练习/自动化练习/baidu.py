'''
@Project:Python
@Time:2018/9/18 11:42
@Author:xvnmeng
'''

'''
需要把驱动程序安装好
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.quit()