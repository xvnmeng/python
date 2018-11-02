'''
@Project:Python
@Time:2018/8/17 10:40
@Author:xvnmeng
'''

import unittest
from time import sleep
import csv

# 模块化的调用        引入吃喝嫖赌的动作集合
from baiduMainPage.auto_driveer.auto_driver import AutoDriver
# 导入基础页面的基础页面类      引入去那里吃喝嫖赌的地方
from baiduMainPage.page.base_page import BasePage

# 构建一个测试用例的类        相当于是第几批去吃喝嫖赌的人
# 这是第一批去吃喝嫖赌的人
class TestCase1(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 继承之后，通过driver调用AutoDriver001的函数   引入吃喝嫖赌的动作集合
        self.driver = AutoDriver()
        sleep(1)
        # s 继承了基础页面和当前子页面的属性             引入吃喝嫖赌的地方
        self.s = BasePage(self.driver)
        # 最大化窗口             相当于：开始喝-》
        # self.driver.max_window()

    # 结尾条件
    def tearDown(self):
        # 退出浏览器             相当于：开始吃
        sleep(2)
        self.driver.quit_browser()

    # 定义百度搜索的方法
    def testSearch(self):
        '''这是一个打开百度首页，并且进行搜搜的测试'''
        # 打开网址          相当于：开车导航去
        self.driver.open_url()
        # 休眠一秒
        sleep(1)
        # 传入“梅西”到输入框            开车去，只玩id这种游戏
        # 通过八大定位的id定位，传入值
        self.driver.find_elements('id', 'kw').send_keys('梅西')
        sleep(3)
        # 点击搜索按钮
        self.driver.find_elements('id', 'su').click()
        sleep(5)


def main():
    # 构造测试集
    suite = unittest.TestSuite()
    # 添加测试用例（类名+测试方法名）
    # suite.addTest(TestCase001Login('test_login'))
    suite.addTest(unittest.makeSuite(TestCase1))

    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)


# 判断
if __name__=='__main__':
    main()
