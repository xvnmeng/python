'''
@Project:Python
@Time:2018/8/21 16:56
@Author:xvnmeng
'''
import unittest
from time import sleep
import csv

# 模块化的调用
from auto_driveer.auto_driver_001 import AutoDriver001
from page.user_central_001 import UserCentral01


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
        sleep(7)
        self.driver.quit_browser()

    def testLogin(self):
        # 打开网址
        self.driver.open_url('/')
        sleep(1)

        # 通过读取文件来登录多个账号
        # file_o = open(r'D:\code\python\test_selenium_ecshop\data\username.csv', mode='r', encoding='utf8')
        # data_r = csv.reader(file_o)
        # for i in data_r:
        #     login_dict = {
        #         'username': i[0],
        #         'passwd': i[1]
        #     }
        #     # print(dict)



        # 点击登录按钮
        self.s.login_click()
        sleep(1)
        self.s.test_login('xvnmeng', '123456')
        # 断言的 期望值
        expect_text = 'xvnmeng'
        # 实际值
        actual_test = self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/font').text
        # 开始断言
        self.assertEqual(expect_text, actual_test, '登录失败')
        # 点击用户中心
        self.s.user_central_click()
        # 安全退出
        self.s.safe_quit()