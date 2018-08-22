'''
@Project:Python
@Time:2018/8/14 15:11
@Author:xvnmeng
'''
#
# # 导包
# import csv
# # 打开文件
# csv_file = open(r'C:\Users\THINK\PycharmProjects\test001\test_data.csv',
#                 mode='r',encoding='utf-8')
# # 读取数据
# csv_data = csv.reader(csv_file)
# # 遍历存入字典
# for i in csv_data:
#     print(i)
#     dict1 = {
#         1:i[0],
#         2:i[1],
#         3:i[2],
#         4:i[3],
#         5:i[4]
#     }
#     # 打印字典
#     print(dict1)
# #
# csv_file.close()

# # 写入文件
# # 导包
# import csv
# # 定义写入的数据
# csv_w_data = ['我', '爱', '你', 'China',520]
# # 打开文件
# csv_op_file = open(r'C:\Users\THINK\PycharmProjects\test001\test_data.csv',
#                    mode='w',encoding='utf-8',newline='')
# # 以书面格式写入到文件
# csv_w_file = csv.writer(csv_op_file,dialect='excel')
# # 写入数据
# csv_w_file.writerow(csv_w_data)
# # 关闭文件
# csv_op_file.close()


# import csv
# csv_w_data = ['我', '爱', '你', 'China',520]
# csv_op_file = open(r'C:\Users\THINK\PycharmProjects\test001\test_data.csv',
#                    mode='w',encoding='utf-8',newline='')
# csv_w_file = csv.writer(csv_op_file,dialect='excel')
# csv_w_file.writerow(csv_w_data)
# csv_op_file.close


# 类的定义与调用方法
# class TestCar():
#     def run(self):
#         print('这是一个跑的方法！')
#
#     def add(self, a, b):
#         return a + b
# from TestCar import TestCar  # 导包
#
# obj = TestCar()
# obj.run()
# print(obj.add(2, 5))




# # 数字求和
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
# sum = float(num1) + float(num2)
# print('数字{0}和{1}相加结果为：{2}'.format(num1, num2, sum))


# # 平方根
# num = float(input('输入一个数字：'))
# num_sqrt = num ** 0.5
# print('%0.3f 的平方根为 %0.3f' %(num,num_sqrt))


# # 负数和复数的平方根
# import cmath
# num = int(input("请输入一个数字: ")) #记得输入类型的转换
# num_sqrt = cmath.sqrt(num)
# print('{0} 的平方根为 {1:0.3f} + {2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))


# # 二次方
# import cmath
# a = float(input('输入 a: '))
# b = float(input('输入 b: '))
# c = float(input('输入 c: '))
#
# d = (b ** 2) - (4 * a * c)
#
# sol1 = (-b - cmath.sqrt(d) / (2 * a))
# sol2 = (-b + cmath.sqrt(d) / (2 * a))
#
# print('结果为 {0} 和 {1}


# # 计算三角形面积
# a = float(input('输入三角形第一边长： '))
# b = float(input('输入三角形第二边长： '))
# c = float(input('输入三角形第三边长： '))
#
# # 计算周长
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('三角形面积为 %0.2f' % area)


# # 随机数生成
# import random
# print(random.randint(0, 9))


# # 温度转化
# celsius = float(input('输入摄氏温度：'))
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f 摄氏温度转化为华氏温度 %0.1f ' %(celsius, fahrenheit))


# # 判断字符串是否为数字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except(TypeError, ValueError):
#         pass
#     return False
# # 测试字符串和数字
# print(is_number('foo'))  # False
# print(is_number('1'))  # True
# print(is_number('1.3'))  # True
# print(is_number('-1.37'))  # True
# print(is_number('1e3'))  # True
#
# # 测试 Unicode
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四'))  # True
# # 版权号
# print(is_number('©'))  # False


# # 判断及奇数偶数
# num = int(input('输入一个数字：'))
# if num % 2 == 0:
#     print('{0} 是偶数'.format(num))
# else:
#     print('{0}


# # 判断闰年
# year = int(input('输入年份：'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if yaer % 400 == 0:
#             print('{0} 是闰年'.format(year))
#         else:
#             print('{0} 不是闰年'.format(year))
#     else
#         print('{0} 不是闰年'.format(year))
# else:
#     print('{0} 不是闰年'.format(year))


# # 质数判断
# num = int(input('输入一个数字：'))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num,'不是质数')
#             print(i, '乘以', num / i, '是', num)
#             break
#         else:
#             print(num, '是质数')
# else:
#     print(num, '是质数')


# # 输出指定范围内的素数
# lower = int(input('输入区间最小值：'))
# upper = int(input('输入区间最大值：'))
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print


# # 阶乘
# num = int(input('输入一个数字：'))
# factorial = 1
# if num < 0:
#     print('负数没有阶乘！')
# elif num == 0:
#     print('0的阶乘为1！')
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("%d 的阶乘为 %d" % (num, factorial))


# # 九九乘法表
# for i in range(1,10):
#     for j in range(1, 1 + i):
#         print('{0}x{1}={2}\t'.format(i, j, i * j), end='')
#     print()

# # 斐波那契数列
# nterms = int(input('你需要几项？'))
# n1 = 0
# n2 = 1
# n3 = 2
# count = 2
# if nterms <= 0:
#     print('请输入一个正整数。')
# elif nterms == 1:
#     print('斐波那契数列：')
#     print(n1)
# else:
#     print('斐波那契数列：')
#     print(n1, " , ", n2,end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         n1 = n2
#         n2 = nth
#         count += 1


# # 阿姆斯特郎数
# num = int(input('输入一个数字：'))
# sum = 0
# n = len(str(num))
#
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# if num == sum:
#     print(num, '是阿姆斯特郎数')
# else:
#     print(num, '不是阿姆斯特朗数')


# # 用户输入字符
# c = input("请输入一个字符: ")
#
# # 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
#
# print(c + " 的ASCII 码为", ord(c))
# print(a, " 对应的字符为", chr(a))


# # 最大公约数
# def hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if(x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
# num1 = int(input('输入第一个数字：'))
# num2 = int(input('输入第二个数字：'))
# print(num1, '和', num2, '的最大公约数为', hcf(num1, num2))


# # 最小公倍数
# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if(greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
# num1 = int(input('输入第一个数字：'))
# num2 = int(input('输入第二个数字：'))
# print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))


# # 简易计算器
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")
#
# choice = input('输入你的选择（1/2/3/4）:')
# num1 = int(input('输入第一个数字：'))
# num2 = int(input('输入第二个数字：'))
# if choice == '1':
#     print(num1, '+', num2, '=', add(num1, num2))
# elif choice == '2':
#     print(num1, '-', num2, '=', subtract(num1, num2))
# elif choice == '3':
#     print(num1, '*', num2, '=', multiply(num1, num2))
# elif choice == '4':
#     print(num1, '/', num2, '=', add(num1, num2))
# else:
#     print('非法输入。')


# # 生成日历
# import calendar
# yy = int(input('输入年份：'))
# mm = int(input('输入月份：'))
# print(calendar.month(yy, mm))


# # 递归斐波那契数列
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fibo(n-1) + recur_fibo(n-2))
# #获取输入
# nterms = int(input('需要输出几项？'))
# if nterms <= 0:
#     print('输入整数')
# else:
#     print('斐波那契数列')
#     for i in range(nterms):
#         print(recur_fibo(i))


# 文件IO
# with open(r'C:\Users\THINK\PycharmProjects\test001\test001.txt','wt') as out_file:
# #     out_file.write('xvnmeng')
# #
# # with open(r'C:\Users\THINK\PycharmProjects\test001\test001.txt','rt') as in_file:
# #     text = in_file.read()
# # print(text)


# # 字符串判断
# str = 'xvnmeng'
# print(str.isalnum()) # 都是数字 或 字母
# print(str.isalpha()) # 都是字母
# print(str.isdigit()) # 都是数字
# print(str.islower()) # 都是小写
# print(str.isupper()) # 都是大写
# print(str.istitle()) # 首字母都是大写，像标题
# print(str.isspace()) # 都是空白字符


# # 字符串大小写转换
# str = "www.runoob.com"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


# # 获取昨天日期
# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=1)
#     yesterday = today - oneday
#     return yesterday
# print(getYesterday())


# # 计算每月天数
# import calendar
# monthRange = calendar.monthrange(2018, 8)
# print(monthRange)
# # 假设输出（3,30）：第一表示星期，从0开始，第二表示本月天数



# # list的使用
# li = ['a', 'b', 'mpilgrim', 'z', 'example']
# # 增加元素
# li.append("new")
# li.insert(2,'new')
# li.extend(['two', 'elements'])
# print(li)
#
# # 搜索
# print(li.index('new'))
# # 删除
# li.remove('z') # 多个值时，删除第一个
# # pop：删除最后一个，返回删除的元素
# li.pop()
# # join连接
# ",".join(li)
# # split("-")：以“-”为分割符号
# s='xvn-meng'
# s.split('-')
# # 过滤filter
# # 字典解析
# params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# params.keys()
# params.values()
# params.items()



