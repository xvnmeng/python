'''
@Project:Python
@Time:2018/8/17 11:47
@Author:xvnmeng
'''
## 通过读取文件，改变变量 可以批量注册
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('http://localhost/upload/user.php?act=register')
driver.maximize_window()
time.sleep(1)
# 定位内容点击注册
driver.find_element_by_xpath('//*[@id="username"]').click()
driver.find_element_by_id('username').send_keys('xvnmeng001')
driver.find_element_by_id('email').send_keys('xxx@qq.com')
driver.find_element_by_id('password1').send_keys('123456')
driver.find_element_by_id('conform_password').send_keys('123456')
# msn  qq  电话  家庭电话   手机
driver.find_element_by_name('extend_field1').send_keys('xxx@qq.com')
driver.find_element_by_name('extend_field2').send_keys('12345657')
driver.find_element_by_name('extend_field3').send_keys('075588888888')
driver.find_element_by_name('extend_field4').send_keys('075588889999')
driver.find_element_by_name('extend_field5').send_keys('13833885354')
# 密码提示  问题答案   注册
Select(driver.find_element_by_name('sel_question')).select_by_value('favorite_food')
driver.find_element_by_name('passwd_answer').send_keys('food')
driver.find_element_by_name('Submit').click()