'''
@Project:Python
@Time:2018/9/5 14:28
@Author:xvnmeng
'''
'''
@Project:Python
@Time:2018/9/5 10:39
@Author:xvnmeng
'''
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from auto_driver.auto_driver_001 import AutoDriver001


class CustomerMassege(object):
    def __init__(self, d:AutoDriver001):
        self.driver = d

    # 定义进入到主界面的函数
    def send_massege(self, clientname, clientlink, clienttel, clientaddress, initreceamt):

        # 添加或者修改姓名
        # a = self.driver.find_elements('id', 'clientname')
        a = self.driver.find_elements('xpath', '//*[@id="clientname"]')
        a.clear()
        a.send_keys(clientname)

        # 联系人
        a = self.driver.find_elements('id', 'clientlink')
        a.clear()
        a.send_keys(clientlink)

        # 电话
        a = self.driver.find_elements('id', 'clienttel')
        a.clear()
        a.send_keys(clienttel)

        # 地址
        a = self.driver.find_elements('id', 'clientaddress')
        a.clear()
        a.send_keys(clientaddress)

        # 初期欠款
        a = self.driver.find_elements('id', 'initreceamt')
        a.clear()
        a.send_keys(initreceamt)

        # # 关联业务员
        # Select(self.driver.find_elements('class_name', 'trigger')).select_by_index(2)  #########括号

    # 更多信息
    def more_massege(self, wxcode, companytel, clientfax, clientemail, clientqq, clientremark):
        # 微信
        a = self.driver.find_elements('id', 'wxcode')
        a.clear()
        a.send_keys(wxcode)

        # 单位电话
        a = self.driver.find_elements('id', 'companytel')
        a.clear()
        a.send_keys(companytel)

        # 传真
        a = self.driver.find_elements('id', 'clientfax')
        a.clear()
        a.send_keys(clientfax)

        # 邮编
        a = self.driver.find_elements('id', 'clientemail')
        a.clear()
        a.send_keys(clientemail)

        # QQ
        a = self.driver.find_elements('id', 'clientqq')
        a.clear()
        a.send_keys(clientqq)

        # 备注
        a = self.driver.find_elements('id', 'clientremark')
        a.clear()
        a.send_keys(clientremark)




