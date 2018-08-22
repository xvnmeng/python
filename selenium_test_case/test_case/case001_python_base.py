'''
@author:xvnmeng
@datetime:2018/8/19 13:42
@software:PyCharm Community Editon
'''
# dict = {
#     1:1,
#     2:2,
#     3:3
# }


# # 合并字典
# keys = ['a', 'b', 'c']
# values = ['1', '2', '3']
# for key,value in zip(keys, values):
#     print(key, value)


# from time import ctime
# print(ctime())


# from time import *
# print(ctime())
# sleep(2) # time sleep two second
# print(ctime())


# # 跨页面调用函数  from case002_python_base2 import add
# from test_case.case002_python_base2 import add
# print(add(2, 3))


# # 提示接收到什么异常，打印出来
# try:
#     print(aa)
# except BaseException as msg:
#     print(msg)

# try:
#     print(aa)
# except Exception as msg:
#     print(msg)
# else:
#     print('cc')

# try:
#     print(aa)
# except Exception as msg:
#     print(msg)
# finally:
#     print('cc')

# # 抛出异常
# from random import randint
# number = randint(1, 9)
# if number % 2 == 0:
#     raise NameError("%d is even" % number)
# else:
#     raise NameError("%d is odd" % number)