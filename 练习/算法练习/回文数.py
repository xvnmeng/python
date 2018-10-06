'''
@Project:Python
@Time:2018/9/13 9:24
@Author:xvnmeng
'''
# 回文数，比如12321
def huiwen(x):
    flag = True
    # 通过判断对称位是否相等
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            flag = False
            break
    if flag:
        print('这是一个回文数。')
    else:
        print('这不是一个回文数')

x = int(input('请输入一个回文数：'))
x = str(x)
print(type(x))
huiwen(x)