'''
@Project:Python
@Time:2018/8/17 11:47
@Author:xvnmeng
'''
'''
@Project:Python
@Time:2018/8/17 10:40
@Author:xvnmeng
'''
import unittest
from time import sleep
import csv

from auto_driveer.auto_driver_001 import AutoDriver001
from page.user_central_001 import UserCentral01


class TestCase001Login(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用  和 sub_page 的函数
        self.s = UserCentral01(self.driver)

        # 最大化窗口
        # self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        sleep(3)
        self.driver.quit_browser()

    def testRegister(self):
        '''
        这是一个注册的测试。
        '''

        # 打开网址
        self.driver.open_url('/')
        sleep(1)

        username = ''
        # 通过读取文件来登录多个账号  读写模式打开
        file_o = open(r'D:\code\python\test_selenium_ecshop\data\register.csv', mode='r', encoding='utf8')
        data_r = csv.reader(file_o)
        for i in data_r:
            register_dict = {
                'username': i[0],
                'email': i[1]
            }
            username = register_dict['username']
            email = register_dict['email']

            # 注册按钮
            self.s.register_click()
            sleep(1)
            # 输入注册信息
            self.s.register(username, email)
            # 确认注册
            self.s.Submit_click()
            sleep(3)

            # 断言的 期望值
            expect_text = username
            # 实际值
            actual_test = self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/font').text
            # 开始断言
            self.assertEqual(expect_text, actual_test, '登录失败')

            # 点击用户中心
            self.s.user_central_click()
            # 安全退出
            self.s.safe_quit()
            sleep(1)

        file_o.close()

        # 截取字符串的数字
        num = int(username[7:]) + 1
        # 账户名：xvnmen123形式
        username = 'xvnmeng' + str(num)
        # 邮箱：xvnmeng123@qq.com形式
        email = username + '@qq.com'
        data_w = [username, email]

        # 更新一次注册的账号，方便下次测试注册使用
        file_o = open(r'D:\code\python\test_selenium_ecshop\data\register.csv', mode='w', encoding='utf8', newline='')
        file_w = csv.writer(file_o, dialect='excel')
        file_w.writerow(data_w)
        file_o.close()