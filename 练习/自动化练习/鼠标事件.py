'''
@Project:Python
@Time:2018/9/18 12:03
@Author:xvnmeng
'''
'''
ActionChains类的鼠标操作方法：
perform():
context_click():    右击
double_click():
drag_and_drop():
move_to_element():  悬停
'''

from selenium.webdriver import ActionChains # 导入
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
element = driver.find_element_by_id('kw')
target = driver.find_element_by_id('su')

# 执行元素拖放
ActionChains(driver).drag_and_drop(element, target).perform()