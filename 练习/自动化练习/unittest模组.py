'''
@Project:Python
@Time:2018/9/18 11:06
@Author:xvnmeng
'''
import unittest

class DemoTests(unittest.TestCase):

    @classmethod # @表明该方法是类的方法
    def setUp(self):
        pass

    def test_01(self):
        pass

    def test_02(self):
        pass

    def test_03(self):
        pass

    @classmethod #测试结束后的清除工作
    def tearDownClass(cls):
        pass

# 执行测试主函数
if __name__ == '__main__':

    # 执行所有test开头的函数
    unittest.main(verbosity=2)