'''
@Project:Python
@Time:2018/8/18 15:53
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


def new_user():
    # 打开网页    新注册账号购买
    open_page('http://localhost/upload/user.php?act=register')
    max()
    waiting(2)

    # 点击注册按钮
    xpath('//*[@id="username"]').click()
    # 填写注册信息 传入参数 名字 邮箱 密码 确认密码
    # msn  qq  办公电话  家庭电话  手机  密保问题  密保答案     username,email,
    username = str(input('获取索要注册的用户名：'))
    email = username + '@qq.com'
    register(username, email, '123456', '123456',
             'xxx@qq.com', '12345657', '075588888888', '075588889999', '13833885354', 'favorite_food', 'food')
    # 注册成功，点击返回首页
    xpath('/html/body/div[3]/a[1]')
    waiting(2)

def old_user():
    # 打开网页 最大化 等待1秒    用已有账户购买
    open_page(r"http://localhost/upload/index.php")
    max()
    waiting(1)
    # 点击登录按钮
    xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    login('xvnmeng','123456')

# 定义注册函数，传入参数
def register(username,email,passwd,comfor_passwd,msn,qq,tel01,tel02,phone,question,answer):
    id('username').send_keys(username)
    id('email').send_keys(email)
    id('password1').send_keys(passwd)
    id('conform_password').send_keys(comfor_passwd)
    # msn  qq  办公电话  家庭电话   手机
    name('extend_field1').send_keys(msn)
    name('extend_field2').send_keys(qq)
    name('extend_field3').send_keys(tel01)
    name('extend_field4').send_keys(tel02)
    name('extend_field5').send_keys(phone)
    # 密码提示  问题答案   注册
    Select(name('sel_question')).select_by_value(question)
    name('passwd_answer').send_keys(answer)

    # 如何获取提示文字，判断是否可以注册
    # name('Submit').click()
    time.sleep(5)

# 传入省、市、区、   姓名、地址、电话、邮箱 参数
def send_address(procince,city,districts,name,email01,addr,phone):
    # 选择省 市 区
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

# 定义搜索函数，传入参数 商品名称
def find(product):
    # 输入信息
    name('keywords').send_keys(product)
    # 点击搜搜
    name('imageField').click()
    waiting(2)

# 定义付款页面点击选择函数
def pay_click():
    xpath('/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
    xpath('/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
    xpath('/html/body/div[7]/form/div[15]/div[2]/input[1]').click()


# 定义一个 登录后或者注册后 返回首页 到付款完成的函数
def all_opration():
    # 进行搜索
    find('诺基亚N96')

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

    # 已有地址则修改  没有地址则填写
    try:
        xpath('/html/body/div[7]/form/div[3]/h6/a').click()
    except:
        print('没有地址！')
    finally:
        waiting(2)
        # 传入地址信息参数 省 市 区 姓名 邮箱 地址 电话
        send_address('6', '77', '705', 'xvnmeng007', '123@qq.com', '上梅林街道', '13344556677')

    # 点击付款选项
    pay_click()


user_num = int(input('输入“1”使用新注册账号，输入“2”使用已有账号：'))
if user_num == 1:
    # 新注册用户购买
    new_user()
elif user_num == 2:
    # 使用老用户购买
    old_user()
else:
    print('选择错误')


# 回到首页后的操作到付款结束
all_opration()

# 第二次购买 返回首页，搜索
xpath('/html/body/div[3]/a[1]')
waiting(2)
# 回到首页后的操作到付款结束
all_opration()