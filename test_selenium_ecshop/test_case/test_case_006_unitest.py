'''
@Project:Python
@Time:2018/8/18 14:28
@Author:xvnmeng
'''
# 测试框架 利用断言
import unittest
from selenium import webdriver
import time


class LoginTests(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 对象实例化
        self.driver = webdriver.Firefox()
        # 绑定url
        self.base_url = "http://localhost/upload/index.php"

    # 尾部条件
    def tearDown(self):
        print('aaa')
        # self.driver.quit()

    # 定义测试部分
    def test_login(self):
        self.driver.get(self.base_url)
        time.sleep(1)
        # 定位按钮、元素、点击登录
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
        time.sleep(1)
        # 定位用户名输入框传值
        self.driver.find_element_by_name('username').send_keys('xvnmeng')
        # 定位密码传值
        self.driver.find_element_by_name('password').send_keys('123456')
        # 勾选保存密码
        self.driver.find_element_by_id('remember').click()
        # 定位点击登录
        self.driver.find_element_by_name('submit').click()
        time.sleep(5)

        # 断言定位是否登录成功  断言用来输出错误信息
        # 期望文本
        eccept_text = '退出'
        # 获取文本
        catch_text = self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]').text

        # 错误的话输出登录是失败
        self.assertEqual(eccept_text, catch_text, '登录失败')
        # time.sleep(5)















