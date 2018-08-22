'''
@Project:Python
@Time:2018/8/17 15:41
@Author:xvnmeng
'''
# 导包
# 导包
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# 浏览器对象实例化
driver = webdriver.Firefox()
driver.maximize_window()
# 打开网址
driver.get("http://localhost/upload/index.php")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
# 定位用户名输入框传值
driver.find_element_by_name('username').send_keys('xvnmeng001')
# 定位密码传值
driver.find_element_by_name('password').send_keys('123456')
# 勾选保存密码
driver.find_element_by_id('remember').click()
# 定位点击登录
driver.find_element_by_name('submit').click()
time.sleep(1)
driver.find_element_by_link_text('用户中心').click()
time.sleep(1)
driver.find_element_by_link_text('我的留言').click()
time.sleep(1)
# 进入信息页面开始修改
driver.find_element_by_name('msg_title').send_keys('借钱充值')
driver.find_element_by_name('msg_content').send_keys('xvnmeng')
# 上传，参数为path
driver.find_element_by_name('message_img').send_keys(r'C:\Users\THINK\Desktop\17--selenium.txt')
driver.find_element_by_class_name('bnt_bonus').click()
