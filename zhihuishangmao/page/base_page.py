'''
@Project:Python
@Time:2018/9/5 10:39
@Author:xvnmeng
'''
from time import sleep

from auto_driver.auto_driver_001 import AutoDriver001

class BasePage(object):
    def __init__(self, d:AutoDriver001):
        self.driver = d

    # 定义进入到主界面的函数
    def into_page(self):
        # 点击行业
        self.driver.find_elements('class_name', 'industry-01').click()
        sleep(1)
        # 点击老板
        self.driver.find_elements('class_name', 'role-01').click()
        # 点击体验
        self.driver.find_elements('xpath', '/html/body/div[25]/div/div/div/a').click()

    # 悬浮慧管客
    def customer(self):
        # 悬浮
        a = self.driver.find_elements('xpath', '/html/body/table/tbody/tr/td[1]/div/ul/li[3]/a')
        print(a)
        # ActionChains(self.driver).move_to_element(a).perform()

    # 选择新增客户
    def add_customer(self):
        self.driver.find_elements('css_selector', '#secondmenu3 > ul:nth-child(1) '
                                                  '> li:nth-child(2) > a:nth-child(2)').click()

    # 增加供应商
    def add_supplier(self):
        self.driver.find_elements('css_selector', '#secondmenu3 > ul:nth-child(1) '
                                                  '> li:nth-child(5) > a:nth-child(2)').click()

    # 管理客户
    def manage_customer(self):
        self.driver.find_elements('css_selector', '#secondmenu3 > ul:nth-child(1) > l'
                                                  'i:nth-child(2) > a:nth-child(1)').click()

    # 管理供应商
    def manage_supplier(self):
        self.driver.find_elements('css_selector', '#secondmenu3 > ul:nth-child(1) > '
                                                  'li:nth-child(5) > a:nth-child(1)').click()

    # 搜索框
    def search(self, val):
        a = self.driver.find_elements('id', 'keyword')
        a.send_keys(val)
        self.driver.find_elements('css_selector', '#searchDiv > a:nth-child(2)').click()

