'''
@Project:Python
@Time:2018/8/18 14:28
@Author:xvnmeng
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

# 定义打开浏览器和最大化函数
def max():
    return driver.maximize_window()
# 设置窗口大小
def window_size(width,height):
    return driver.set_window_size(width,height)
# 打开网页
def open_page(url):
    return driver.get(url)

# 定义八大定位
def id(id):
    return driver.find_element_by_id(id)
def name(name):
    return driver.find_element_by_name(name)
def class_name(class_name):
    return driver.find_element_by_class_name(class_name)
def tag_name(tag_name):
    return driver.find_element_by_tag_name(tag_name)
def link_text(link_text):
    return driver.find_element_by_link_text(link_text)
def partial_link_text(partial_link_text):
    return driver.find_element_by_partial_link_text(partial_link_text)
def xpath(xpath):
    return driver.find_element_by_xpath(xpath)
def css_selector(css_selector):
    return driver.find_element_by_css_selector(css_selector)

# d登录函数
def login(username,passwd):
    # 定位用户名输入框传值
    name('username').send_keys(username)
    # 定位密码传值
    name('password').send_keys(passwd)
    # 勾选保存密码
    id('remember').click()
    # 定位点击登录
    name('submit').click()
    waiting(3)


# 等待几秒函数
def waiting(sec):
    return time.sleep(sec)

# 传入省、市、区、   姓名、地址、电话、邮箱 参数
def send_address(procince,city,districts,name,email01,addr,phone):
    # 选择省 市 区  下拉栏需要暂停来加载
    Select(id('selProvinces_0')).select_by_value(procince)
    waiting(1)
    Select(id('selCities_0')).select_by_value(city)
    waiting(1)
    Select(id('selDistricts_0')).select_by_value(districts)
    # 填写姓名
    customers = id('consignee_0')
    customers.clear()
    customers.send_keys(name)
    # 填写邮件
    email = id('email_0')
    email.clear()
    email.send_keys(email01)

    # 填写地址
    address = id('address_0')
    address.clear()
    address.send_keys(addr)
    # 填写电话
    tel = id('tel_0')
    tel.clear()
    tel.send_keys(phone)
    # 点击提交修改
    xpath('/html/body/div[7]/form/div/table/tbody/tr[6]/td/input[1]').click()
    waiting(2)

# 定义付款页面点击选择函数
def pay_click():
    xpath('/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
    xpath('/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
    xpath('/html/body/div[7]/form/div[15]/div[2]/input[1]').click()




# 打开网页 最大化 等待1秒
open_page(r"http://localhost/upload/index.php")
max()
waiting(1)
# 点击登录按钮
xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()

login('xvnmeng001','123456')

# 搜索框输入  点击
name('keywords').send_keys('诺基亚N96')
name('imageField').click()
waiting(2)
# 点击进入货物
xpath('//*[@id="compareForm"]/div/div/div/a[1]/img').click()
waiting(2)
# 加入购物车
xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]/img').click()
waiting(2)


# 修改数量 # 清空再修改为3个
class_name('inputBg').clear()
class_name('inputBg').send_keys('3')
# 更新 会跳转页面
xpath('/html/body/div[7]/div[1]/form/table[2]/tbody/tr/td[2]/input[2]').click()
waiting(1)
# 返回购物车
xpath('/html/body/div[6]/div/div/div/div/p[2]/a').click()
waiting(1)
# 结算
xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
waiting(1)

# 已有地址的老用户   先点击修改地址按钮
xpath('/html/body/div[7]/form/div[3]/h6/a').click()
waiting(2)

# 传入地址信息参数 省 市 区 姓名 邮箱 地址 电话
send_address('6', '77', '705', 'xvnmeng007', '123@qq.com', '上梅林街道','13344556677')
# 点击付款选项
pay_click()