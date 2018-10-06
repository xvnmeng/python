'''
@Project:Python
@Time:2018/8/21 15:53
@Author:xvnmeng
'''

'''
包含了基本页面。和基本操作的函数定义
'''
from time import sleep

from selenium.webdriver.support.select import Select

from test_selenium_ecshop.auto_driveer.auto_driver_001 import AutoDriver001


class BasePage(object):
    # BasePage类从AutoDriver001继承属性
    def __init__(self,d:AutoDriver001):
        self.driver = d

    # 登录点击
    def login_click(self):
        # 点击登录
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()

    # 注册点击
    def register_click(self):
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img').click()

    # 用户中心点击
    def user_central_click(self):
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[1]').click()

    # 退出点击
    def quit_click(self):
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]').click()

    # 小写的提交点击
    def submit_click(self):
        # 定位点击登录    submit
        self.driver.find_elements('name', 'submit').click()

    # 大写的提交点击
    def Submit_click(self):
        # 点击提交注册
        self.driver.find_elements('name', 'Submit').click()

    # 首页按钮点击
    def home_page_click(self):
        self.driver.find_elements('class_name', 'cur').click()

    # 搜索点击
    def search_click(self):
        self.driver.find_elements('class_name', 'go').click()

    # 发送的搜索信息
    def search_message(self,product_name):
        self.driver.find_elements('id', 'keyword').send_keys(product_name)

    # 登录
    def login(self,username,passwd):
        # 定位用户名输入框传值
        self.driver.find_elements('name', 'username').send_keys(username)
        # 定位密码传值
        self.driver.find_elements('name', 'password').send_keys(passwd)
        # 勾选保存密码
        self.driver.find_elements('id', 'remember').click()


    # 注册
    def register(self,username,useremail):
        # 填写注册信息   设计一个可以传入参数修改的注册信息
        self.driver.find_elements('id', 'username').send_keys(username)
        self.driver.find_elements('id', 'email').send_keys(useremail)
        self.driver.find_elements('id', 'password1').send_keys('123456')
        self.driver.find_elements('id', 'conform_password').send_keys('123456')
        # msn  qq  电话  家庭电话   手机
        self.driver.find_elements('name', 'extend_field1').send_keys('xxx@qq.com')
        self.driver.find_elements('name', 'extend_field2').send_keys('12345657')
        self.driver.find_elements('name', 'extend_field3').send_keys('075588888888')
        self.driver.find_elements('name', 'extend_field4').send_keys('075588889999')
        self.driver.find_elements('name', 'extend_field5').send_keys('13833885354')
        # 密码提示  问题答案   注册
        Select(self.driver.find_elements('name', 'sel_question')).select_by_value('favorite_food')
        self.driver.find_elements('name', 'passwd_answer').send_keys('food')

    # 搜索  传入参数 搜索的商品名
    def search_product(self, product_name):
        # 输入信息
        search = self.driver.find_elements('name', 'keywords')
        search.clear()
        search.send_keys(product_name)
        # 点击搜搜
        self.driver.find_elements('name', 'imageField').click()

    # 更新购物车
    def update_car(self, number):
        # 修改数量 # 清空再修改为3个
        self.driver.find_elements('class_name', 'inputBg').clear()
        self.driver.find_elements('class_name', 'inputBg').send_keys(number)
        # 更新 会跳转页面
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/form/table[2]/tbody/tr/td[2]/input[2]').click()
        sleep(1)
        # 返回购物车
        self.driver.find_elements('xpath', '/html/body/div[6]/div/div/div/div/p[2]/a').click()

    # 订单确定
    def order_sure(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[15]/div[2]/input[1]').click()