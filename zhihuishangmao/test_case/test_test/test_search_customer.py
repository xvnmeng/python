'''
@Project:Python
@Time:2018/9/6 10:31
@Author:xvnmeng
'''
import unittest
from time import sleep
import csv

from auto_driver.auto_driver_001 import AutoDriver001
from page.base_page import BasePage
from page.base_massege import CustomerMassege



class TestCaseCustomerMassege(unittest.TestCase):
    def setUp(self):
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性
        self.s1 = BasePage(self.driver)
        self.s2 = CustomerMassege(self.driver)
        # 最大化窗口
        # self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        sleep(3)
        self.driver.quit_browser()

    def testRegister(self):
        '''这是一个测试搜索功能的测试的自动化测试。'''
        # 打开网址
        self.driver.open_url('')
        sleep(1)
        # 进入主界面
        self.s1.into_page()
        sleep(1)
        # 悬浮慧管家
        self.driver.action_chains('/html/body/table/tbody/tr/td[1]/div/ul/li[3]/a')

        # self.s1.customer()
        sleep(1)
        # 点击客户
        self.s1.manage_supplier()
        sleep(5)

        # # 跳到多表单
        # self.driver.iframe("//iframe[contains(@src,'ClientInfo')]")
        # 跳到多表单
        self.driver.iframe("//iframe[contains(@src,'List')]")

        # 搜索
        self.s1.search('盛唐酒店')
        sleep(8)

