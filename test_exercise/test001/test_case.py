import csv
import time
import unittest

from test001.zilei02 import Zilei02
from test001.fuck import Fuck
from test001.zilei01 import Zilei01


'''
测试框架开始，首先用到 
'''




class TestCase123(unittest.TestCase):
    def setUp(self):
        self.driver=Fuck()
        # driver=webdriver.Firefox()
        # s 继承了基础页面和当前子页面的属性   通过 s 可以调用  和 sub_page 的函数
        self.s =Zilei01(self.driver)
        self.s2=Zilei02(self.driver)
        time.sleep(1)
       # driver.maximize_window()
       #  self.driver.zuida()
        time.sleep(1)
    def tearDown(self):
        time.sleep(20)
    def test_ceshi(self):
        self.driver.dakai('')



        findel=open(r'D:\code\python\test_exercise\test001\test.csv',mode='r',encoding='utf8')
        find_data=csv.reader(findel)
        for i in find_data:
            denglu_dict={
                'name':i[0],
                'passwd':i[1]
            }
            ##############读取到账号密码
            print(denglu_dict)

            self.s.xuanze()
            self.s.denglu(denglu_dict['name'],denglu_dict['passwd'])
            time.sleep(1)



            # findel1=open(r'D:\Users\Administrator\xianjianyoujian20180825\data\data02.csv',mode='r',encoding='utf8')
            # findel1_data=csv.reader(findel1)
            # for i in findel1_data:
            #     xiexin_dict={
            #         'zhuti':i[0],
            #         'neirong':i[1]
            #     }


            self.s.xiexin_click()
            time.sleep(1)
            self.s2.shoujian()
            # self.s2.xiexin(xiexin_dict['zhuti'],xiexin_dict['neirong'])

            #########################################
            self.s2.xiexin('zhuti', 'neirong')
            time.sleep(3)
            findel1.close()


        # self.s.tuichu()
        findel.close()
        time.sleep(50)