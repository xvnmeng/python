'''
@author:xvnmeng
@datetime:2018/8/19 20:28
@software:PyCharm Community Editon
'''
# C++ 100道经典python语言


# '''
# 【程序1】
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
# 　　　　　　掉不满足条件的排列。
# 2.程序源代码：
# '''
# count = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if(i != j) and (i != k) and (j != k):
#                 count += 1
#                 print(i, j, k)
#
# print('总数为%d' % count)



# '''
# 【程序2】
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
# 　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
# 　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
# 　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　　　　　　
# 2.程序源代码：
# '''
# # 奖金层次
# bonus1 = 100000 * 0.1
# bonus2 = bonus1 + 100000 * 0.500075
# bonus4 = bonus2 + 200000 * 0.5
# bonus6 = bonus4 + 200000 * 0.3
# bonus10 = bonus6 + 400000 * 0.15
#
# i = int(input('input gain:\n'))
# if i <= 100000:
#     bonus = i * 0.1
# elif i <= 200000:
#     bonus = bonus1 + (i - 100000) * 0.075
# elif i <= 400000:
#     bonus = bonus2 + (i - 200000) * 0.05
# elif i <= 600000:
#     bonus = bonus4 + (i - 400000) * 0.03
# elif i <= 1000000:
#     bonus = bonus6 + (i - 600000) * 0.015
# else:
#     bonus = bonus10 + (i - 1000000) * 0.01
# print('bonus = ',bonus)




'''
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
　　　　　　的结果满足如下条件，即是结果。请看具体分析：
2.程序源代码：

#include "math.h"
main()
{
long int i,x,y,z;
for (i=1;i<100000;i++)
　{ x=sqrt(i+100); 　　/*x为加上100后开方后的结果*/
　　y=sqrt(i+268); 　　/*y为再加上168后开方后的结果*/
　　　if(x*x==i+100&&y*y==i+268)/*如果一个数的平方根的平方等于该数，这说明此数是完全平方数*/
　　　　printf("\n%ld\n",i);
　}
} 
'''
# import math
# for i in range(10000):
#     #转化为整型值
#     x = int(math.sqrt(i + 100))
#     y = int(math.sqrt(i + 268))
#     if(x * x == i + 100) and (y * y == i + 268):
#         print(i)





'''题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.程序源代码：
'''
# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 <= month <= 12:
#     sum = months[month - 1]
# else:
#     print 'data error'
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print 'it is the %dth day.' % sum




'''
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
2.程序源代码：
'''
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)




'''
【程序6】
题目：用*号输出字母p的图案。
1.程序分析：可先用'*'号在纸上写出字母C，再分行输出。
2.程序源代码：
'''
# print('Hello Python world!\n')
# print ('*' * 10)
# for i in range(5):
#     print ('*        *')
# print ('*' * 10)
# print ('*\n' * 6)



'''
【程序7】
题目：输出特殊图案，请在c环境中运行，看一看，Very Beautiful!
1.程序分析：字符共有256个。不同字符，图形不一样。　　　　　　
2.程序源代码：
'''
# a = 176
# b = 219
# print (chr(b),chr(a),chr(a),chr(a),chr(b))
# print (chr(a),chr(b),chr(a),chr(b),chr(a))
# print (chr(a),chr(a),chr(b),chr(a),chr(a))
# print (chr(a),chr(b),chr(a),chr(b),chr(a))
# print (chr(b),chr(a),chr(a),chr(a),chr(b))


'''
【程序8】
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
2.程序源代码：
#include "stdio.h"
main()
{
　int i,j,result;
　printf("\n");
　for (i=1;i<10;i++)
　　{ for(j=1;j<10;j++)
　　　　{
　　　　　result=i*j;
　　　　　printf("%d*%d=%-3d",i,j,result);/*-3d表示左对齐，占3位*/
　　　　}
　　　printf("\n");/*每一行后换行*/
　　}
}
'''
# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print('%d * %d = % -3d' % (i, j, result))
#     print('')




'''
【程序11】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1.程序分析：　兔子的规律为数列1,1,2,3,5,8,13,21....
2.程序源代码：
main()
{
long f1,f2;
int i;
f1=f2=1;
for(i=1;i<=20;i++)
　{ printf("%12ld %12ld",f1,f2);
　　　if(i%2==0) printf("\n");/*控制输出，每行四个*/
　　　f1=f1+f2; /*前两个月加起来赋值给第三个月*/
　　　f2=f1+f2; /*前两个月加起来赋值给第三个月*/
　}
}
'''
# f1 = 1
# f2 = 1
# for i in range(1,21):
#     print('%12d %12d' % (f1,f2))
#     if (i % 2) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 + f2