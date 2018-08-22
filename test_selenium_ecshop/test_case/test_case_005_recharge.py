'''
@Project:Python
@Time:2018/8/17 16:37
@Author:xvnmeng
'''
'''
@Project:Python
@Time:2018/8/17 15:41
@Author:xvnmeng
'''
# 导包
from selenium import webdriver
import time
# from selenium.webdriver.support.select import Select
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
# 进入信息页面开始修改 资金 充值 充值金额 留言 付款 提交
driver.find_element_by_link_text('资金管理').click()
time.sleep(1)
driver.find_element_by_link_text('充值').click()
driver.find_element_by_name('amount').send_keys('888888')
driver.find_element_by_name('user_note').send_keys('打劫')
driver.find_element_by_name('payment_id').click()
driver.find_element_by_name('submit').click()