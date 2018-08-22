'''
@Project:Python
@Time:2018/8/14 16:03
@Author:xvnmeng
'''
# 数字1,2,3,4  组成不重复的三位数
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (i != k) and (j != k):
                print(i,j,k)
                count += 1
print(count)