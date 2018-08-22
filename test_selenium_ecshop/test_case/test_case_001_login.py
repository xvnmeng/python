'''
@Project:Python
@Time:2018/8/17 10:40
@Author:xvnmeng
'''
# 1、打开网址
# 2、点击登录按钮
# 3、输入账户信息
# 4、点击登录
# 导包
from selenium import webdriver
import time
# 浏览器对象实例化
driver = webdriver.Firefox()
driver.maximize_window()
# 打开网址
driver.get("http://localhost/upload/index.php")
# 等待
time.sleep(2)
# 定位按钮、元素、点击登录
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
time.sleep(2)
# 定位用户名输入框传值
driver.find_element_by_name('username').send_keys('xvnmeng')
time.sleep(2)
# 定位密码传值
driver.find_element_by_name('password').send_keys('123456')
time.sleep(2)
# 勾选保存密码
driver.find_element_by_id('remember').click()
time.sleep(1)
# 定位点击登录
driver.find_element_by_name('submit').click()
time.sleep(5)
driver.quit()