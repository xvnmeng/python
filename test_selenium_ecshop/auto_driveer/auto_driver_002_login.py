'''
@Project:Python
@Time:2018/8/20 17:19
@Author:xvnmeng
'''

# 测试框架 利用断言
import unittest
import selenium
from selenium import webdriver
import time
# 从文件夹-文件 导入 一个class
from selenium.webdriver.support.select import Select
# 文件。类  导入其中的方法
from auto_driveer.auto_driver_001 import AutoDriver001
from auto_driveer.auto_driver_003_common import Common


class TestLogin(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # 对象实例化
        self.driver = AutoDriver001()
        self.c =Common(self.driver)
        # 最大化窗口
        self.driver.max_window()

    # 尾部条件
    def tearDown(self):
        # 退出浏览器
        pass
        # self.driver.quit_browser()

    # 定义测试部分
    def testLogin(self):
        # 打开网页         参数：后缀部分
        # 加上 “/" 导致网页加载不完整
        self.driver.open_url('')

        # 登录
        self.c.test_login()

        # # 留言
        # self.c.test_send_message()

        # # 充值   参数：金额
        # self.c.test_recharge(99999)

        # 修改个人信息        可以再优化一下，传入信息参数
        self.c.test_modify_user_message()

        # # 注册
        # self.c.test_register(username='xvnmeng001',useremail='xvnmen001@qq.com')

        # # 搜索商品
        # self.c.test_search('诺基亚N96')
        # # 点击进入商品
        # self.driver.find_elements('xpath', '//*[@id="compareForm"]/div/div/div/a[1]/img').click()
        # time.sleep(2)
        # # 点击加入购物车
        # self.driver.find_elements('xpath', '/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[8]/a[1]/img').click()
        # time.sleep(1)
        #
        # # 更新购物车  传入购买数量参数
        # self.c.test_update_car(3)
        #
        # # 已有地址则修改  没有地址则填写
        # try:
        #     self.driver.find_elements('xpath', '/html/body/div[7]/form/div[3]/h6/a').click()
        # except:
        #     print('没有地址！')
        # finally:
        #     time.sleep(2)
        #     # 传入地址信息参数 省 市 区 姓名 邮箱 地址 电话
        #     self.c.test_modify_address('6', '77', '705', 'xvnmeng007', '123@qq.com', '上梅林街道', '13344556677')
        #
        # # 确定订单
        # self.c.test_order_sure()

        #
        # time.sleep(2)
        # # 定位按钮、元素、点击登录
        # self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
        # time.sleep(2)
        # # 定位用户名输入框传值
        # self.driver.find_elements('name', 'username').send_keys('xvnmeng')
        # # 定位密码传值
        # self.driver.find_elements('name', 'password').send_keys('123456')
        # # 勾选保存密码
        # self.driver.find_elements('id', 'remember').click()
        # # 定位点击登录
        # self.driver.find_elements('name', 'submit').click()
        #
        # # 断言定位是否登录成功  断言用来输出错误信息
        # # 期望文本
        # eccept_text = '退出'
        # # 获取文本
        # catch_text = self.driver.find_elements('xpath','/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]').text
        #
        # # 错误的话输出登录是失败
        # self.assertEqual(eccept_text, catch_text, '登录失败')
        # # time.sleep(5)



    # # 注册
    # def testReginter(self):
    #     # 打开首页
    #     self.driver.open_url('')
    #
    #     # 点击注册按钮
    #     self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img').click()
    #     time.sleep(2)
    #     self.driver.find_elements('id', 'username').send_keys('xvnmeng017')
    #     self.driver.find_elements('id', 'email').send_keys('xxx017@qq.com')
    #     self.driver.find_elements('id', 'password1').send_keys('123456')
    #     self.driver.find_elements('id', 'conform_password').send_keys('123456')
    #     # msn  qq  电话  家庭电话   手机
    #     self.driver.find_elements('name', 'extend_field1').send_keys('xxx@qq.com')
    #     self.driver.find_elements('name', 'extend_field2').send_keys('12345657')
    #     self.driver.find_elements('name', 'extend_field3').send_keys('075588888888')
    #     self.driver.find_elements('name', 'extend_field4').send_keys('075588889999')
    #     self.driver.find_elements('name', 'extend_field5').send_keys('13833885354')
    #     # 密码提示  问题答案   注册
    #     Select(self.driver.find_elements('name', 'sel_question')).select_by_value('favorite_food')
    #     self.driver.find_elements('name', 'passwd_answer').send_keys('food')
    #     self.driver.find_elements('name', 'Submit').click()
    #     time.sleep(2)
    #
    #     # 断言 定位退出按钮判断是否注册成功
    #     eccept_text = '退出'
    #     # 获取文本
    #     catch_text = self.driver.find_elements('xpath','/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]').text
    #
    #     # 错误的话输出登录是失败
    #     self.assertEqual(eccept_text, catch_text, '登录失败')
    #     # time.sleep(5)


    # # 修改用户信息
    # def testUserMessage(self):
    #     # 登录
    #     self.driver.open_url('')
    #     time.sleep(2)
    #     self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    #     time.sleep(2)
    #     self.driver.find_elements('name', 'username').send_keys('xvnmeng')
    #     self.driver.find_elements('name', 'password').send_keys('123456')
    #     self.driver.find_elements('id', 'remember').click()
    #     self.driver.find_elements('name', 'submit').click()
    #     time.sleep(1)
    #     # 期望文本
    #     eccept_text = '退出'
    #     # 获取文本
    #     catch_text = self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[2]').text
    #     # 错误的话输出登录是失败
    #     self.assertEqual(eccept_text, catch_text, '登录失败')
    #
    #     # 进入修改
    #     self.driver.find_elements('link_text', '用户中心').click()
    #     time.sleep(1)
    #     self.driver.find_elements('link_text', '用户信息').click()
    #     time.sleep(1)
    #     # 进入信息页面开始修改
    #     Select(self.driver.find_elements('name', 'birthdayYear')).select_by_value('2018')
    #     Select(self.driver.find_elements('name', 'birthdayMonth')).select_by_value('10')
    #     Select(self.driver.find_elements('name', 'birthdayDay')).select_by_value('10')
    #     # 选择性别
    #     self.driver.find_elements('name', 'sex').click()
    #     # 先清空再修改
    #     # 邮箱
    #     self.driver.find_elements('name', 'email').clear()
    #     self.driver.find_elements('name', 'email').send_keys('yyy@qq.com')
    #     # msn  qq  电话  家庭电话   手机
    #     self.driver.find_elements('name', 'extend_field1').clear()
    #     self.driver.find_elements('name', 'extend_field1').send_keys('yyy@qq.com')
    #
    #     self.driver.find_elements('name', 'extend_field2').clear()
    #     self.driver.find_elements('name', 'extend_field2').send_keys('123456578')
    #
    #     self.driver.find_elements('name', 'extend_field3').clear()
    #     self.driver.find_elements('name', 'extend_field3').send_keys('075588888899')
    #
    #     self.driver.find_elements('name', 'extend_field4').clear()
    #     self.driver.find_elements('name', 'extend_field4').send_keys('075588889988')
    #
    #     self.driver.find_elements('name', 'extend_field5').clear()
    #     self.driver.find_elements('name', 'extend_field5').send_keys('13833885453')
    #     # 密保
    #     Select(self.driver.find_elements('name', 'sel_question')).select_by_value('motto')
    #     # 清空输入
    #     self.driver.find_elements('name', 'passwd_answer').clear()
    #     self.driver.find_elements('name', 'passwd_answer').send_keys('人生苦短，我用python')
    #     # 提交
    #     self.driver.find_elements('name', 'submit').click()
    #     # 退出
    #     # driver.quit()



    # # 留言功能
    # def testMessagre(self):
    #     self.driver.open_url('')
    #     time.sleep(2)
    #     self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    #     time.sleep(2)
    #     self.driver.find_elements('name', 'username').send_keys('xvnmeng')
    #     self.driver.find_elements('name', 'password').send_keys('123456')
    #     self.driver.find_elements('id', 'remember').click()
    #     self.driver.find_elements('name', 'submit').click()
    #     time.sleep(2)
    #
    #     self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    #     # 定位用户名输入框传值
    #     self.driver.find_elements('name', 'username').send_keys('xvnmeng001')
    #     # 定位密码传值
    #     self.driver.find_elements('name', 'password').send_keys('123456')
    #     # 勾选保存密码
    #     self.driver.find_elements('id', 'remember').click()
    #     # 定位点击登录
    #     self.driver.find_elements('name', 'submit').click()
    #     time.sleep(1)
    #     self.driver.find_element('link_text', '用户中心').click()
    #     time.sleep(1)
    #     self.driver.find_elements('link_text', '我的留言').click()
    #     time.sleep(1)
    #     # 进入信息页面开始修改
    #     self.driver.find_elements('name', 'msg_title').send_keys('借钱充值')
    #     self.driver.find_elements('name', 'msg_content').send_keys('xvnmeng')
    #     # 上传，参数为path
    #     self.driver.find_elements('name', 'message_img').send_keys(r'C:\Users\THINK\Desktop\17--selenium.txt')
    #     self.driver.find_elements('class_name', 'bnt_bonus').click()

    # def testRecharge(self):
    #     self.driver.open_url('')
    #     time.sleep(2)
    #     self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    #     time.sleep(2)
    #     self.driver.find_elements('name', 'username').send_keys('xvnmeng')
    #     self.driver.find_elements('name', 'password').send_keys('123456')
    #     self.driver.find_elements('id', 'remember').click()
    #     self.driver.find_elements('name', 'submit').click()
    #     time.sleep(2)
    #
    #     # self.driver.find_elements('xpath', '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    #     # # 定位用户名输入框传值
    #     # self.driver.find_elements('name', 'username').send_keys('xvnmeng001')
    #     # # 定位密码传值
    #     # self.driver.find_elements('name', 'password').send_keys('123456')
    #     # # 勾选保存密码
    #     # self.driver.find_elements('id', 'remember').click()
    #     # # 定位点击登录
    #     # self.driver.find_elements('name', 'submit').click()
    #     # time.sleep(1)
    #     self.driver.find_elements('link_text', '用户中心').click()
    #     time.sleep(1)
    #     # 进入信息页面开始修改 资金 充值 充值金额 留言 付款 提交
    #     self.driver.find_elements('link_text', '资金管理').click()
    #     time.sleep(1)
    #     self.driver.find_elements('link_text', '充值').click()
    #     self.driver.find_elements('name', 'amount').send_keys('888888')
    #     self.driver.find_elements('name', 'user_note').send_keys('打劫')
    #     self.driver.find_elements('name', 'payment_id').click()
    #     self.driver.find_elements('name', 'submit').click()
