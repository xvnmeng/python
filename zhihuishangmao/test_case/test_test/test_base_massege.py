'''
@Project:Python
@Time:2018/9/5 10:08
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
        '''这是一个测试客户基本信息填写的自动化测试。'''
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
        # 点击新增客户
        self.s1.add_customer()
        sleep(5)

        # 跳到多表单
        self.driver.iframe("//iframe[contains(@src,'ClientInfo')]")

        # 遍历读取信息
        file_o = open(r'D:\code\python\zhihuishangmao\data\customer_massege', mode='r', encoding='utf8')
        data_r = csv.reader(file_o)
        for i in data_r:
            dict = {
                '1': i[0],
                '2': i[1],
                '3': i[2],
                '4': i[3],
                '5': i[4]
            }
            clientname = dict['1']
            clientlink = dict['2']
            clienttel = dict['3']
            clientaddress = dict['4']
            initreceamt = dict['5']

            self.s2.send_massege(clientname, clientlink, clienttel, clientaddress, initreceamt)
        file_o.close()
        sleep(2)