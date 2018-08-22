'''
@author:xvnmeng
@datetime:2018/8/21 22:17
@software:PyCharm Community Editon
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

cookie = driver.get_cookies()
print(cookie)

driver.quit()