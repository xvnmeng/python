'''
@Project:Python
@Time:2018/8/21 16:56
@Author:xvnmeng
'''
import unittest
from selenium import webdriver
import time

# 模块化的调用
from auto_driveer.auto_driver_001 import AutoDriver001
from page.sub_page_001 import SubPage01


class TestCase001Login(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用 base_page 和 sub_page 的函数
        self.s = SubPage01(self.driver)

        # 最大化窗口
        self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        time.sleep(7)
        self.driver.quit_browser()

    def testLogin(self):
        # 打开网址
        self.driver.open_url('/')
        # 点击登录按钮
        self.s.login_click()
