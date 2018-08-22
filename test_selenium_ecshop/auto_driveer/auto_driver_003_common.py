'''
@Project:Python
@Time:2018/8/21 10:27
@Author:xvnmeng
'''

# 创建类
import time

from selenium.webdriver.support.select import Select

from auto_driveer.auto_driver_001 import AutoDriver001


class Common(object):
    # 构造方法         dd变量绑定
    def __init__(self, dd:AutoDriver001):
        self.driver = dd

    # 自定义方法   登录
    def test_login(self):
        # 定位按钮、元素、点击登录
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
        time.sleep(2)
        # 定位用户名输入框传值
        self.driver.find_elements('name', 'username').send_keys('xvnmeng')
        # 定位密码传值
        self.driver.find_elements('name', 'password').send_keys('123456')
        # 勾选保存密码
        self.driver.find_elements('id', 'remember').click()
        # 定位点击登录    submit
        self.driver.find_elements('name', 'submit').click()
        time.sleep(5)

    # 注册             设计没有传入值，则默认
    def test_register(self,username,useremail):

        # 点击注册按钮   注册的网址：http://localhost/upload/user.php?act=register
        self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img').click()
        time.sleep(2)
        # 填写注册信息   设计一个可以传入参数修改的注册信息
        self.driver.find_elements('id', 'username').send_keys(username)
        self.driver.find_elements('id', 'email').send_keys(useremail)
        self.driver.find_elements('id', 'password1').send_keys('123456')
        self.driver.find_elements('id', 'conform_password').send_keys('123456')
        # msn  qq  电话  家庭电话   手机
        self.driver.find_elements('name', 'extend_field1').send_keys('xxx@qq.com')
        self.driver.find_elements('name', 'extend_field2').send_keys('12345657')
        self.driver.find_elements('name', 'extend_field3').send_keys('075588888888')
        self.driver.find_elements('name', 'extend_field4').send_keys('075588889999')
        self.driver.find_elements('name', 'extend_field5').send_keys('13833885354')
        # 密码提示  问题答案   注册
        Select(self.driver.find_elements('name', 'sel_question')).select_by_value('favorite_food')
        self.driver.find_elements('name', 'passwd_answer').send_keys('food')

        # # 点击提交注册
        # self.driver.find_elements('name', 'Submit').click()
        # time.sleep(2)

    # 留言
    def test_send_message(self):
        self.driver.find_elements('link_text', '用户中心').click()
        time.sleep(1)
        self.driver.find_elements('link_text', '我的留言').click()
        time.sleep(1)
        #进入信息页面开始修改
        self.driver.find_elements('name', 'msg_title').send_keys('借钱充值')
        self.driver.find_elements('name', 'msg_content').send_keys('xvnmeng')
        # 上传留言文件，参数为path
        self.driver.find_elements('name', 'message_img').send_keys(r'C:\Users\THINK\Desktop\17--selenium.txt')
        # # 确认点击
        # self.driver.find_elements('class_name', 'bnt_bonus').click()

    # 充值   传入充值金额
    def test_recharge(self,number):
        self.driver.find_elements('link_text', '用户中心').click()
        time.sleep(1)
        # 进入信息页面开始修改 资金 充值 充值金额 留言 付款 提交
        self.driver.find_elements('link_text', '资金管理').click()
        time.sleep(1)

        self.driver.find_elements('link_text', '充值').click()
        self.driver.find_elements('name', 'amount').send_keys(number)
        self.driver.find_elements('name', 'user_note').send_keys('打劫')
        self.driver.find_elements('name', 'payment_id').click()

        # self.driver.find_elements('name', 'submit').click()

    # 判断是否存在地址
    def test_addr_exist(self):
        # 已有地址则修改  没有地址则填写
        try:
            self.driver.find_elements('xpath', '/html/body/div[7]/form/div[3]/h6/a').click()
        except:
            print('没有地址！')
        finally:
            time.sleep(2)
            # 传入地址信息参数 省 市 区 姓名 邮箱 地址 电话
            self.test_modify_address('6', '77', '705', 'xvnmeng007', '123@qq.com', '上梅林街道', '13344556677')


    # 修改地址
    def test_modify_address(self,province,city,districts,name,email01,addr,phone):
        Select(self.driver.find_elements('id', 'selProvinces_0')).select_by_value(province)
        time.sleep(1)
        Select(self.driver.find_elements('id', 'selCities_0')).select_by_value(city)
        time.sleep(1)
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
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div/table/tbody/tr[6]/td/input[1]').click()
        time.sleep(2)

    # 修改用户信息
    def test_modify_user_message(self):
        # 进入修改
        self.driver.find_elements('link_text', '用户中心').click()
        time.sleep(1)
        self.driver.find_elements('link_text', '用户信息').click()
        time.sleep(1)
        # 进入信息页面开始修改
        Select(self.driver.find_elements('name', 'birthdayYear')).select_by_value('2018')
        Select(self.driver.find_elements('name', 'birthdayMonth')).select_by_value('10')
        Select(self.driver.find_elements('name', 'birthdayDay')).select_by_value('10')
        # 选择性别
        self.driver.find_elements('name', 'sex').click()
        # 先清空再修改
        # 邮箱
        self.driver.find_elements('name', 'email').clear()
        self.driver.find_elements('name', 'email').send_keys('yyy@qq.com')
        # msn  qq  电话  家庭电话   手机
        self.driver.find_elements('name', 'extend_field1').clear()
        self.driver.find_elements('name', 'extend_field1').send_keys('yyy@qq.com')

        self.driver.find_elements('name', 'extend_field2').clear()
        self.driver.find_elements('name', 'extend_field2').send_keys('123456578')

        self.driver.find_elements('name', 'extend_field3').clear()
        self.driver.find_elements('name', 'extend_field3').send_keys('075588888899')

        self.driver.find_elements('name', 'extend_field4').clear()
        self.driver.find_elements('name', 'extend_field4').send_keys('075588889988')

        self.driver.find_elements('name', 'extend_field5').clear()
        self.driver.find_elements('name', 'extend_field5').send_keys('13833885453')
        # 密保
        Select(self.driver.find_elements('name', 'sel_question')).select_by_value('motto')
        # 清空输入
        self.driver.find_elements('name', 'passwd_answer').clear()
        self.driver.find_elements('name', 'passwd_answer').send_keys('人生苦短，我用python')

        # # 提交
        # self.driver.find_elements('name', 'submit').click()
        # # 退出
        # # driver.quit()

    # 搜索  传入参数 搜索的商品名
    def test_search(self,product_name):
        # 输入信息
        search = self.driver.find_elements('name', 'keywords')
        search.clear()
        search.send_keys(product_name)
        # 点击搜搜
        self.driver.find_elements('name', 'imageField').click()
        time.sleep(2)

    # 更新购物车
    def test_update_car(self, number):
        # 修改数量 # 清空再修改为3个
        self.driver.find_elements('class_name', 'inputBg').clear()
        self.driver.find_elements('class_name', 'inputBg').send_keys(number)
        # 更新 会跳转页面
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/form/table[2]/tbody/tr/td[2]/input[2]').click()
        time.sleep(1)
        # 返回购物车
        self.driver.find_elements('xpath', '/html/body/div[6]/div/div/div/div/p[2]/a').click()
        time.sleep(1)
        # 结算
        self.driver.find_elements('xpath', '/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()

    # 订单确定
    def test_order_sure(self):
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[5]/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[7]/table/tbody/tr[3]/td[1]/input').click()
        self.driver.find_elements('xpath', '/html/body/div[7]/form/div[15]/div[2]/input[1]').click()

    # name = Submit 可以最为一个点击函数