'''
@Project:Python
@Time:2018/8/17 10:39
@Author:xvnmeng
'''
# # 多表单 登录
# from selenium import webdriver
# import time
#
# from selenium.webdriver import ActionChains
# driver = webdriver.Firefox()
# right = driver.find_element_by_xpath("xx")
# ActionChains(driver).context_click(right).perform()
#
# #定位到要双击的元素
# double =driver.find_element_by_xpath("xxx")
# #对定位到的元素执行鼠标双击操作
# ActionChains(driver).double_click(double).perform()




#
# driver = webdriver.Firefox()

# # 登录lol界面
# driver.get('http://lol.qq.com')
# time.sleep(2)
# driver.maximize_window()
# # 点击登录
# driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/em').click()
# time.sleep(2)
# driver.switch_to.frame('loginIframe')
# # 账号密码
# driver.find_element_by_id('switcher_plogin').click()
# time.sleep(1)
# driver.find_element_by_id('u').send_keys('xvnmeng')


# # 浏览器句柄事件
# driver.get('http://www.xyb2b.com')
# # 获取当前句柄（窗口）
# a = driver.current_window_handle
# time.sleep(1)
# driver.maximize_window()
# driver.find_element_by_class_name('loginBtn').click()

# # 登录 方法一
# # 获取all句柄
# all = driver.window_handles
# time.sleep(1)
# for i in all:
#     if i != a:
#         driver.switch_to.window(i)
#         # 输入用户信息
#         driver.find_element_by_id('userName').send_keys('xvnmeng')


# # 登录 方法二
# all = driver.window_handles
# # 跳转到左后一个句柄
# driver.switch_to.window(all[-1])
# driver.find_element_by_id('userName').send_keys('xvnmeng')




# # 键盘事件
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Firefox()
# driver.get('http://baidu.com')
# driver.find_element_by_id("kw").send_keys("selenium")
# time.sleep(2)
# # 删除多输入的一个m
# driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
# time.sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# driver.find_element_by_id("kw").send_keys("教程")
# time.sleep(3)
# #ctrl+a 全选输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')


'''
link_text 要为直接文字链接
xpath、css_selector调用遍历搜索用时较长
鼠标事件：ActionChains-》conten_click()、double_click()、drag_and_drop()、move_to_element()
获取url:current_url
等待：
定位：len()计算长度，pop（0）获取第一个元素
多表单：switch_to.frame()
        切换方式：switch_to.parent_content()    最外层：switch_to.default_content()
多窗口 switch_to.window()  current_window_handle   window_handles
警告框：定位：switch_to.alert
        参数：text、accept（）、dismiss（）解散、
截图：Get_screenshot_as_file()
下拉菜单：Select(driver.find_element_by_id('areaId')).select_by_index(1)
'''
from selenium import webdriver
option = webdriver.ChromeOptions()
#设置成用户自己的数据目录
option.add_argument(r'--user-data-dir=C:\Users\THINK\AppData\Local\Google\Chrome\User Data')
browser=webdriver.Chrome(chrome_options=option)
browser.get('http://www.baidu.com/')


# 加载个人浏览器配置办法  配置加载浏览器的路径  与信息
fp=webdriver.FirefoxProfile(r"C:\Users\THINK\AppData\Roaming\Mozilla\Firefox\Profiles\nc2c6nsu.default")
driver=webdriver.Firefox(fp)
driver.get('http://www.baidu.com')