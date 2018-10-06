'''
@Project:Python
@Time:2018/8/17 14:16
@Author:xvnmeng
'''
import unittest
from time import sleep
import csv

from auto_driveer.auto_driver_001 import AutoDriver001
from page.user_central_001 import UserCentral01
from page.user_message_002 import UserMessage01


class TestCase001Login(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用  和 sub_page 的函数
        self.s = UserCentral01(self.driver)
        # 用户信息类的继承
        self.driver_user = UserMessage01(self.driver)

        # 最大化窗口
        self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        sleep(2)
        self.driver.quit_browser()

    def testUserMessage(self):
        '''
        这是一个修改用户信息的测试。
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
        # 点击用户信息
        self.s.user_message_click()
        sleep(1)

        # 读取用户信息文件
        file_o = open(r'D:\code\python\test_selenium_ecshop\data\user_message.csv', mode='r', encoding='utf8')
        data_r = csv.reader(file_o)
        for i in data_r:
            dict = {
                'year': i[0],
                'month': i[1],
                'day': i[2],
                'email': i[3],
                'msn': i[4],
                'qq': i[5],
                'tel': i[6],
                'home_tel': i[7],
                'phone': i[8],
                'security': i[9],
                'security_answer': i[10]
            }
            # 修改用户信息
            self.driver_user.modify_user_message(dict['year'], dict['month'], dict['day'],dict['email'],
                                                 dict['msn'], dict['qq'], dict['tel'], dict['home_tel'],
                                                 dict['phone'], dict['security'], dict['security_answer'])
            # 点击提交修改
            self.driver.find_elements('xpath', '/html/body/div[7]/div[2]/div/div/div/form[1]/table/tbody/tr[11]/td/input[2]').click()
        # 关闭文件
        file_o.close()

        sleep(1)
        # 点击用户中心
        self.s.user_central_click()
        # 安全退出
        self.s.safe_quit()