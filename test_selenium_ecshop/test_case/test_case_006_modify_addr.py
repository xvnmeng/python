'''
@Project:Python
@Time:2018/8/23 15:05
@Author:xvnmeng
'''
import csv

'''
@Project:Python
@Time:2018/8/17 15:41
@Author:xvnmeng
'''

import unittest
from time import sleep

from auto_driveer.auto_driver_001 import AutoDriver001
from page.user_central_001 import UserCentral01
from page.delivery_address_003 import DeliveryAddr


class TestCase001Login(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数
        self.driver = AutoDriver001()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用  和 sub_page 的函数
        self.s = UserCentral01(self.driver)
        # 用户信息类的继承
        self.driver_addr = DeliveryAddr(self.driver)

        # 最大化窗口
        self.driver.max_window()

    def tearDown(self):
        # 退出浏览器
        sleep(2)
        self.driver.quit_browser()

    def testRecharge(self):
        '''
        这是一个修改地址的的测试。
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
        # 我的地址
        self.s.delivery_address_click()

        # 传入地址的参数  判断地址是否存在
        self.driver_addr.addr_exist()

        sleep(2)
        # 传入地址信息参数 省 市 区 姓名 邮箱 地址 电话

        file_o = open(r'D:\code\python\test_selenium_ecshop\data\address.csv', mode='r', encoding='utf-8')
        data_r = csv.reader(file_o)
        for i in data_r:
            dict = {
                'province':i[0],
                'city':i[1],
                'district':i[2],
                'name':i[3],
                'email':i[4],
                'addr':i[5],
                'phone':i[6]
            }
            print(dict)
            # 传图地址信息
            self.driver_addr.modify_addr(dict['province'], dict['city'], dict['district'],
                                         dict['name'], dict['email'], dict['addr'], dict['phone'])

        file_o.close()