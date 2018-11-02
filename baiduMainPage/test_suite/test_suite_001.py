import unittest
# 测试套件
# 导包，从测试用例，导图百度搜索里面的TestCase类          相当于：导入第一批去吃喝嫖赌的人
from baiduMainPage.test_case.baidu_search import  TestCase1

# 判断
if __name__=='__main__':
    # 构造测试集
    suite=unittest.TestSuite()
    # 添加测试用例（类名+测试方法名）
    # suite.addTest(TestCase001Login('test_login'))
    suite.addTest(unittest.makeSuite(TestCase1))

    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)