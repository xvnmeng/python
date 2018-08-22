'''
@Project:Python
@Time:2018/8/13 13:29
@Author:xvnmeng
'''
import time
class Order(object):
    def method1(self, a, b, c):
        return a * b + c
    def method2(self):
        return 100
class LittleOrder(Order):
    def method3(self, a, b):
        return a / b + 5
    def methon4(self, a, b, c):
        return self.method1(a, b, c) + self.method2()

if __name__ == "__main__":
    abc = Order()
    print(abc.method1(12, 5, 8))
    ddd = Order()
    print(abc.method1(12, 8, 8))
    print(abc.method1(12, 5, 8) > ddd.method2())
    print("abc.methon1 is %d: " % abc.method1(12, 5, 8))
    print("abc.methon2 is %d: " % abc.method2())

    xiao = LittleOrder()
    print(xiao.method2())
    print(xiao.method3(500, 100))
    print("xiao.methon4 is %d: " % xiao.methon4(12, 5, 8))

    print("打印时间",time.ctime())

#异常
import time
print(time.ctime())

try:
    open("abc.txt","r")
except Exception:
    print("异常")

#读取


