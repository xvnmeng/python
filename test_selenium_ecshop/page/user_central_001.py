'''
@Project:Python
@Time:2018/8/21 16:03
@Author:xvnmeng
'''
from test_selenium_ecshop.auto_driveer.auto_driver_001 import AutoDriver001

from test_selenium_ecshop.page.base_page import BasePage


# 创建继承父类BasePage，sub_page是子页面
class UserCentral01(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d1:AutoDriver001):
        # 继承方法  继承父类
        self.driver = d1
        super().__init__(d1)

    # 自定义方法
    # 安全退出
    def safe_quit(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[14]/img').click()

    # 用户信息点击
    def user_message_click(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[2]').click()

    # 收货地址点击
    def delivery_address_click(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[4]').click()

    # 我的留言
    def my_message_click(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[6]').click()

    # 资金管理
    def money_manage_click(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[13]').click()


