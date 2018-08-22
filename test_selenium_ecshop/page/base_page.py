'''
@Project:Python
@Time:2018/8/21 15:53
@Author:xvnmeng
'''
import time

from selenium.webdriver.support.select import Select

from auto_driveer.auto_driver_001 import AutoDriver001


class BasePage(object):
    # BasePage类从AutoDriver001继承属性
    def __init__(self,d:AutoDriver001):
        self.driver = d

    def login_click(self):
        # 点击登录
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
        time.sleep(2)

    def test_login(self,username,passwd):
        # 定位用户名输入框传值
        self.driver.find_elements('name', 'username').send_keys(username)
        # 定位密码传值
        self.driver.find_elements('name', 'password').send_keys(passwd)
        # 勾选保存密码
        self.driver.find_elements('id', 'remember').click()
        # 定位点击登录    submit
        self.driver.find_elements('name', 'submit').click()
        time.sleep(3)

    def register_click(self):
        # 点击注册按钮
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img').click()
        time.sleep(2)

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

        # # 点击提交注册
        # self.driver.find_elements('name', 'Submit').click()
        # time.sleep(2)

    def user_central_click(self):
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[1]').click()
