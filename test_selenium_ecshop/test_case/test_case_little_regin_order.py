'''
@Project:Python
@Time:2018/8/17 19:48
@Author:xvnmeng
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('http://localhost/upload/user.php?act=register')
driver.maximize_window()
time.sleep(1)
# 定位内容点击注册
driver.find_element_by_xpath('//*[@id="username"]').click()
driver.find_element_by_id('username').send_keys('xvnmeng012')
driver.find_element_by_id('email').send_keys('xxx012@qq.com')
driver.find_element_by_id('password1').send_keys('123456')
driver.find_element_by_id('conform_password').send_keys('123456')
# msn  qq  电话  家庭电话   手机
driver.find_element_by_name('extend_field1').send_keys('xxx@qq.com')
driver.find_element_by_name('extend_field2').send_keys('12345657')
driver.find_element_by_name('extend_field3').send_keys('075588888888')
driver.find_element_by_name('extend_field4').send_keys('075588889999')
driver.find_element_by_name('extend_field5').send_keys('13833885354')
# 密码提示  问题答案   注册
Select(driver.find_element_by_name('sel_question')).select_by_value('favorite_food')
driver.find_element_by_name('passwd_answer').send_keys('food')
driver.find_element_by_name('Submit').click()
time.sleep(5)
########### 注册成功



##########返回首页，搜索
driver.find_element_by_xpath('/html/body/div[3]/a[1]')
time.sleep(3)

# 开始搜索 搜索框输入  点击
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
# 填写地址信息
Select(driver.find_element_by_xpath('//*[@id="selProvinces_0"]')).select_by_value('6')
time.sleep(1)
Select(driver.find_element_by_xpath('//*[@id="selCities_0"]')).select_by_value('77')
time.sleep(1)
Select(driver.find_element_by_xpath('//*[@id="selDistricts_0"]')).select_by_value('705')
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
tel.send_keys('13833885354')

driver.find_element_by_xpath('/html/body/div[7]/form/div/table/tbody/tr[6]/td/input[1]').click()
time.sleep(2)

########## 付款页面
driver.find_element_by_xpath('/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
driver.find_element_by_xpath('/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
driver.find_element_by_xpath('/html/body/div[7]/form/div[15]/div[2]/input[1]').click()
time.sleep(2)



############## 完成新用户第一次购买
############   第二次购买
##########返回首页，搜索
driver.find_element_by_xpath('/html/body/div[3]/a[1]')
time.sleep(3)

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



