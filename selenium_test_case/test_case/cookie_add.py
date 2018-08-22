'''
@author:xvnmeng
@datetime:2018/8/21 22:20
@software:PyCharm Community Editon
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

# Ìí¼Ócookie
driver.add_cookie({'name' : 'key-aaa', 'value' : 'value-bbb'})
if cookie in driver.get_cookies():
    print('%s -> %s' % (cookie['name'], cookie['value']))

driver.quit()