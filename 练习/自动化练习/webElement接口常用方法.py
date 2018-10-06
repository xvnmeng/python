'''
@Project:Python
@Time:2018/9/18 11:57
@Author:xvnmeng
'''
'''
size
text
get_attribute(name): 获取属性值
is_displayed():         是否可见
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获取输入框大小
size = driver.find_element_by_id('kw').size
print(size)

# 获取底部备案信息
text = driver.find_element_by_id('cp').text
print(text)

# 获取元素属性值
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

# 是否可见
result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()


driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.quit()