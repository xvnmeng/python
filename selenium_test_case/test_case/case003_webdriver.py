'''
@author:xvnmeng
@datetime:2018/8/19 15:14
@software:PyCharm Community Editon
'''
import os

from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# from selenium import webdriver
# option = webdriver.ChromeOptions()
# # 设置成用户自己的数据目录
# option.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
#
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('http://www.baidu.com')
#
#
#



# driver.get('http://www.baidu.com/')
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys('老王')
# driver.find_element_by_id('su').click()
# time.sleep(2)
# driver.find_element_by_link_text('杨绛').click()
# time.sleep(5)
# driver.quit()

# # 设置窗口大小
# driver.get('http://www.baidu.com/')
# driver.set_window_size(400,500)
# time.sleep(3)
# driver.quit()


# # 前进后退
# first_url = 'http://www.baidu.com'
# driver.get(first_url)
#
# sencon_url = 'http://news.baidu.com'
# driver.get(sencon_url)
# # 前进 后退
# driver.back()
# driver.forward()
# # 退出
# driver.quit()


# # 登录126邮箱
# driver.get('http://www.126.com')
# time.sleep(2)
# driver.find_element_by_name('email').send_keys('username')
# driver.find_element_by_name('password').clear()
# driver.find_element_by_name('password').send_keys('password')
# driver.find_element_by_id('dologin').clear()
# time.sleep(2)
# driver.quit()



# # size: 返回元素尺寸
# # text： 返回元素文本
# # get_attribute（name): 获得属性值
# # is_displayed(): 设置该元素是否可见
# driver.get('http://www.baidu.com')
# size = driver.find_element_by_id('kw').size
# print(size)
# # 底部备案信息
# text = driver.find_element_by_id('cp').text
# print(text)
# # 返回属性值
# attribute = driver.find_element_by_id('kw').get_attribute('type')
# print(attribute)
# # 返货元素是否可见
# result = driver.find_element_by_id('kw').is_displayed()
# print(result)
#
# driver.quit()


# # 鼠标操作
# a = driver.find_element_by_id('xx')
# # 右键操作
# ActionChains(driver).context_click(a).perform()
# # 移动到悬停
# ActionChains(driver).move_to_element(a).perform()
# # 双击
# ActionChains(driver).double_click(a).perform()
# # 拖拽
# target = driver.find_element_by_id('tt')
# ActionChains(driver).drag_and_drop(a, target).perform()



# # 获取验证信息
# driver.get('http://www.126.com')
# print('Before login=========')
# # print this page title
# title = driver.title
# print(title)
#
# # print this page url
# now_url = driver.current_url
# print(now_url)
# # 登录之后再次获取title、url，比较是否相同，不相同则不能用作验证信息
# driver.quit()


# # 隐士等待
# driver.implicitly_wait(10)
# driver.get('http://www.baidu.com')
# try:
#     print(time.ctime())
#     driver.find_element_by_id('kw').send_keys('老王')
# except:
#     print('error!')
# finally:
#     print(time.ctime())
#     driver.quit()



# # 操作批量元素
# file_path = 'file:///' + os.path.abspath('checkbox.html')
# driver.get(file_path)
#
# # 选择所有tag_name为input的元素
# inputs = driver.find_elements_by_tag_name('input')
#
# # 从中选出type 为checkbox 的元素，勾选
# for i in inputs:
#     if i.get_attribute('type') == 'checkbox':
#         i.click()
#         time.sleep(1)
# driver.quit()



# # cookie操作
# driver.get('https://www.youku.com')
# # 获取cookie
# cookie = driver.get_cookies()
# print(cookie)
# time.sleep(3)
# driver.quit()


# driver.get('http://videojs.com')
# # 获取video元素
# video = driver.find_element_by_xpath('//*[@id="preview-player"]/div[1]')
# # 执行js语句，返回url
# url = driver.execute('return arguments[0].currentSrc;', video)
# print(url)


# # 窗口截图
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('selenium')
# time.sleep(2)
# # 截图
# driver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\baidu_img.jpg')



