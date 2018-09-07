'''
@Project:Python
@Time:2018/8/23 10:07
@Author:xvnmeng
'''
from selenium.webdriver.support.select import Select

from test_selenium_ecshop.auto_driveer.auto_driver_001 import AutoDriver001

from test_selenium_ecshop.page.base_page import BasePage
from time import sleep

# 创建继承父类BasePage，sub_page是子页面
class UserMessage01(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d2:AutoDriver001):
        # 继承方法  全部继承
        self.driver = d2
        super().__init__(d2)

    # 修改用户信息
    def modify_user_message(self,year,month,day,email,msn,qq,tel,home_tel,phone,security,security_answer):
        Select(self.driver.find_elements('name', 'birthdayYear')).select_by_value(year)
        # sleep(1)
        Select(self.driver.find_elements('name', 'birthdayMonth')).select_by_value(month)
        # sleep(1)
        Select(self.driver.find_elements('name', 'birthdayDay')).select_by_value(day)

        # # 选择性别
        # self.driver.find_elements('name', 'sex').click()

        # 邮箱
        self.driver.find_elements('name', 'email').clear()
        self.driver.find_elements('name', 'email').send_keys(email)
        # msn
        self.driver.find_elements('name', 'extend_field1').clear()
        self.driver.find_elements('name', 'extend_field1').send_keys(msn)
        # qq
        self.driver.find_elements('name', 'extend_field2').clear()
        self.driver.find_elements('name', 'extend_field2').send_keys(qq)
        # 电话
        self.driver.find_elements('name', 'extend_field3').clear()
        self.driver.find_elements('name', 'extend_field3').send_keys(tel)
        # 家庭电话
        self.driver.find_elements('name', 'extend_field4').clear()
        self.driver.find_elements('name', 'extend_field4').send_keys(home_tel)
        # 手机
        self.driver.find_elements('name', 'extend_field5').clear()
        self.driver.find_elements('name', 'extend_field5').send_keys(phone)
        # 密保
        Select(self.driver.find_elements('name', 'sel_question')).select_by_value(security)
        # 清空输入
        self.driver.find_elements('name', 'passwd_answer').clear()
        self.driver.find_elements('name', 'passwd_answer').send_keys(security_answer)


