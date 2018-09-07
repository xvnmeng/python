'''
@Project:Python
@Time:2018/8/17 16:37
@Author:xvnmeng
'''
import unittest
from time import sleep

from auto_driveer.auto_driver_001 import AutoDriver001
from page.user_central_001 import UserCentral01
from page.recharge_005 import Recharge


class TestCase001Login(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用  和 sub_page 的函数
        self.s = UserCentral01(self.driver)
        # 用户信息类的继承
        self.driver_charge = Recharge(self.driver)

        # 最大化窗口
        self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        sleep(2)
        self.driver.quit_browser()

    def testRecharge(self):
        '''
        这是一个充值功能的测试。
        '''

        # 登录
        self.driver.open_url('/')
        sleep(1)
        # 通过读取指定行 用指定用户名登录
        self.s.login_click()
        sleep(1)
        self.s.login('xvnmeng1', '123456')
        self.s.submit_click()
        sleep(1)

        # 点击用户中心
        self.s.user_central_click()
        sleep(1)
        # 点击资金管理
        self.s.money_manage_click()

        # 传入充值参数   最好就是每次传入数据都是通过读取文件来传入
        self.driver_charge.recharge(8888)