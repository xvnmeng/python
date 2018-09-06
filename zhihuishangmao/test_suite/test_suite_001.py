'''
@Project:Python
@Time:2018/9/5 9:37
@Author:xvnmeng
'''
import unittest
from test_case.test_test import test_base_massege  # 导入要测试的函数包

if __name__  == '__main__':
    # 构造测试集
    suite=unittest.TestSuite()
    # 要测试的函数

    suite.addTest(unittest.makeSuite(test_base_massege.TestCaseCustomerMassege))

    # 运行测试集合
    runner=unittest.TextTestRunner()
    runner.run(suite)