'''
@Project:Python
@Time:2018/8/23 10:46
@Author:xvnmeng
'''
from auto_driveer.auto_driver_001 import AutoDriver001

from page.base_page import BasePage


# 创建继承父类BasePage，sub_page是子页面
class Recharge(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d5:AutoDriver001):
        # 继承方法  全部继承
        self.driver = d5
        super().__init__(d5)

    # 充值   传入充值金额
    def recharge(self, number):
        # 点击充值
        self.driver.find_elements('link_text', '充值').click()
        self.driver.find_elements('name', 'amount').send_keys(number)
        self.driver.find_elements('name', 'user_note').send_keys('打劫')
        self.driver.find_elements('name', 'payment_id').click()
        # 确定充值
        self.driver.find_elements('name', 'submit').click()