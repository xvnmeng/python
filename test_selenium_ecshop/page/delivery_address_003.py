'''
@Project:Python
@Time:2018/8/23 10:25
@Author:xvnmeng
'''
from selenium.webdriver.support.select import Select

from auto_driveer.auto_driver_001 import AutoDriver001

from page.base_page import BasePage

from time import sleep

# 创建继承父类BasePage，sub_page是子页面
class DeliveryAddr(BasePage):
    # 构造方法
    # SubPage类从AutoDriver001继承属性
    def __init__(self,d3:AutoDriver001):
        # 继承方法  全部继承
        self.driver = d3
        super().__init__(d3)

    # 可以考虑通过列表拼接，没有发现递增的id，则选择这个id作为新增地址
    # 修改地址
    def modify_addr(self, province, city, districts, name, email01, addr, phone):
        Select(self.driver.find_elements('id', 'selProvinces_0')).select_by_value(province)
        sleep(1)
        Select(self.driver.find_elements('id', 'selCities_0')).select_by_value(city)
        sleep(1)
        Select(self.driver.find_elements('id', 'selDistricts_0')).select_by_value(districts)

        # 填写姓名
        customers = self.driver.find_elements('id', 'consignee_0')
        customers.clear()
        customers.send_keys(name)

        # 填写邮件
        email = self.driver.find_elements('id', 'email_0')
        email.clear()
        email.send_keys(email01)

        # 填写地址
        address = self.driver.find_elements('id', 'address_0')
        address.clear()
        address.send_keys(addr)

        # 填写电话
        tel = self.driver.find_elements('id', 'tel_0')
        tel.clear()
        tel.send_keys(phone)

        # 点击提交修改
        self.driver.find_elements('xpath', '/html/body/div[7]/div[2]/div/div/div/form[1]/table/tbody/tr[6]/td[2]/input[1]').click()

    # 判断是否存在地址
    def addr_exist(self):
        # 已有地址则修改  没有地址则填写
        try:
            self.driver.find_elements('xpath', '/html/body/div[7]/form/div[3]/h6/a').click()
        except:
            print('没有地址！')