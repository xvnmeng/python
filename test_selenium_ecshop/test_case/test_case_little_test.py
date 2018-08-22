'''
@Project:Python
@Time:2018/8/17 16:55
@Author:xvnmeng
'''
'''
登录ecshop--》搜索诺基亚N96--》购买三部--》完成订单

注意：注册新号，登录，再购买两次
'''
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
time.sleep(3)
################# 登录完毕

# 搜索框输入  点击
driver.find_element_by_name('keywords').send_keys('诺基亚N96')
driver.find_element_by_name('imageField').click()
time.sleep(2)
# 点击进入货物
driver.find_element_by_xpath('//*[@id="compareForm"]/div/div/div/a[1]/img').click()
time.sleep(2)
# 加入购物车
driver.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]/img').click()
time.sleep(2)

# 修改数量 # 清空再修改为3个
num = driver.find_element_by_class_name('inputBg')
num.clear()
num.send_keys('3')
# 更新 会跳转页面
driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table[2]/tbody/tr/td[2]/input[2]').click()
time.sleep(1)
# 返回购物车
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/p[2]/a').click()
time.sleep(1)
# 结算
driver.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
time.sleep(1)

# ############# 填写地址   新用户
# Select(driver.find_element_by_name('selProvinces_0')).select_by_value('6')
# Select(driver.find_element_by_name('selCities_0')).select_by_value('77')
# Select(driver.find_element_by_name('selDistricts_0')).select_by_value('705')
# # 填写姓名 邮件 详细地址 电话
# customers = driver.find_element_by_name('consignee_0')
# customers.clear()
# customers.send_keys('xvnmeng001')
#
# email = driver.find_element_by_name('email_0')
# email.clear()
# email.send_keys('vvv@qq.com')
#
# address = driver.find_element_by_name('address_0')
# address.clear()
# address.send_keys('上梅林')
#
# tel = driver.find_element_by_name('tel_0')
# tel.clear()
# tel.send_keys('13833885354')
#
# driver.find_element_by_xpath('/html/body/div[7]/form/div/table/tbody/tr[6]/td/input[1]').click()
#




######### 已有地址的老用户   name 和 id 混淆#####################################
# 修改地址
driver.find_element_by_xpath('/html/body/div[7]/form/div[3]/h6/a').click()
time.sleep(2)
# 填写地址信息
Select(driver.find_element_by_id('selProvinces_0')).select_by_value('6')
Select(driver.find_element_by_id('selCities_0')).select_by_value('77')
Select(driver.find_element_by_id('selDistricts_0')).select_by_value('705')
# 填写姓名 邮件 详细地址 电话
customers = driver.find_element_by_id('consignee_0')
customers.clear()
customers.send_keys('xvnmeng001')

email = driver.find_element_by_id('email_0')
email.clear()
email.send_keys('vvv@qq.com')

address = driver.find_element_by_id('address_0')
address.clear()
address.send_keys('上梅林')

tel = driver.find_element_by_id('tel_0')
tel.clear()
tel.send_keys('138338853546666')

driver.find_element_by_xpath('/html/body/div[7]/form/div/table/tbody/tr[6]/td/input[1]').click()
time.sleep(2)

########## 付款页面
driver.find_element_by_xpath('/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
driver.find_element_by_xpath('/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
driver.find_element_by_xpath('/html/body/div[7]/form/div[15]/div[2]/input[1]').click()



