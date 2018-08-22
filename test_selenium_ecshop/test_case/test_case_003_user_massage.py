'''
@Project:Python
@Time:2018/8/17 14:16
@Author:xvnmeng
'''
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
driver.find_element_by_link_text('用户信息').click()
time.sleep(1)
# 进入信息页面开始修改
Select(driver.find_element_by_name('birthdayYear')).select_by_value('2018')
Select(driver.find_element_by_name('birthdayMonth')).select_by_value('10')
Select(driver.find_element_by_name('birthdayDay')).select_by_value('10')
# 选择性别
driver.find_element_by_name('sex').click()
# 先清空再修改
# 邮箱
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('yyy@qq.com')
# msn  qq  电话  家庭电话   手机
driver.find_element_by_name('extend_field1').clear()
driver.find_element_by_name('extend_field1').send_keys('yyy@qq.com')

driver.find_element_by_name('extend_field2').clear()
driver.find_element_by_name('extend_field2').send_keys('123456578')

driver.find_element_by_name('extend_field3').clear()
driver.find_element_by_name('extend_field3').send_keys('075588888899')

driver.find_element_by_name('extend_field4').clear()
driver.find_element_by_name('extend_field4').send_keys('075588889988')

driver.find_element_by_name('extend_field5').clear()
driver.find_element_by_name('extend_field5').send_keys('13833885453')
# 密保
Select(driver.find_element_by_name('sel_question')).select_by_value('motto')
# 清空输入
driver.find_element_by_name('passwd_answer').clear()
driver.find_element_by_name('passwd_answer').send_keys('人生苦短，我用python')
# 提交
# driver.find_element_by_name('submit').click()
# 退出
# driver.quit()