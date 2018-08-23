'''
@Project:Python
@Time:2018/8/23 10:40
@Author:xvnmeng
'''
from auto_driveer.auto_driver_001 import AutoDriver001

from page.base_page import BasePage

# 创建继承父类BasePage，sub_page是子页面
class MyMessage(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d4:AutoDriver001):
        # 继承方法  全部继承
        self.driver = d4
        super().__init__(d4)

    # 留言
    def send_message(self):
        # 进入信息页面开始修改
        self.driver.find_elements('name', 'msg_title').send_keys('借钱充值')
        self.driver.find_elements('name', 'msg_content').send_keys('xvnmeng')
        # 上传留言文件，参数为path
        self.driver.find_elements('name', 'message_img').send_keys(r'C:\Users\THINK\Desktop\17--selenium.txt')
        # 确认点击
        self.driver.find_elements('class_name', 'bnt_bonus').click()