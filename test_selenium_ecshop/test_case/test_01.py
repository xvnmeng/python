'''
@Project:Python
@Time:2018/8/16 14:13
@Author:xvnmeng
操作浏览器脚本
'''
from selenium import webdriver
import time
# 对象实例化
driver=webdriver.Firefox()
# 打开url
driver.get('http://www.baidu.com')
# time.sleep(2)
# 窗口最大化
# driver.maximize_window()
# 定位搜索框 输入值    #火狐浏览器可能不点击就搜索
# 八大定位 tag没有鸟用
# driver.find_element_by_id('kw').send_keys('老王')
# name定位需要唯一性
# driver.find_element_by_name('wd').send_keys('老王')
# 唯一性
# driver.find_element_by_class_name('s_ipt').send_keys('老王')
#
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input').send_keys('老王')
#
# driver.find_element_by_css_selector('html body div#wrapper div#head div.head_wrapper div.s_form div.s_form_wrapper.soutu-env-nomac.soutu-env-index form#form.fm span.bg.s_ipt_wr.quickdelete-wrap input#kw.s_ipt').send_keys('老王')
# 找到并且 点击
# driver.find_element_by_link_text('hao123').click()
#
driver.find_element_by_id('kw').send_keys('老王')
time.sleep(2)
# driver.find_element_by_partial_link_text('hao').click()
driver.find_element_by_partial_link_text('杨绛').click()

# time.sleep(2)
# 定位搜索按钮 点击
# driver.find_element_by_id('su').click()
# 停留五秒 退出浏览器
time.sleep(5)
# driver.quit()