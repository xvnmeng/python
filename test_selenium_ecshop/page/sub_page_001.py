'''
@Project:Python
@Time:2018/8/21 16:03
@Author:xvnmeng
'''
from auto_driveer.auto_driver_001 import AutoDriver001

from page.base_page import BasePage


# 创建继承父类BasePage，sub_page是子页面
class SubPage01(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d2:AutoDriver001):
        # 继承方法  继承父类
        self.driver = d2
        super().__init__(d2)

    # 自定义方法
    # 安全退出
    def safe_quit(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/div/div/div/div/a[14]/img')