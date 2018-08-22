'''
@Project:Python
@Time:2018/8/14 16:10
@Author:xvnmeng
'''
# 1.
tup1=(1,2,3,'a','b','c')
print(tup1[4])
print('----1----\n')

# 2
list1=[1,2,3,'a','b','c']
list2=list1*10
print(list2)
print('----2----\n')

# 3.
list1=[1,2,3,'a','b','c']
list1 += list2
list1.reverse()
print(list1)
print('----3----\n')

# 4.
list2.insert(4,'c')
print(list2)
print('----4----\n')

# 5.
list1=[1,2,3,'a','b','c']
del list1[1]
count_a = list1.count('a')
index_3 = list1.index(3)
print(list1)
print(count_a)
print(index_3)
print('----5----\n')

# 6.
list1=[1,2,3,'a','b','c']
del list1[3:8]
print(list1)
print('----6----\n')

# 7.
list1=[1,2,3,'a','b','c']
a = str(list1)
b = a.replace('b','2b')
print(b)
print('----7----\n')


# 8.
dist1={
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    'key5':'value5'
}
print(len(dist1))
print('----8----\n')


# 9.
del dist1['key4']
print(dist1)
print('----9----\n')


# 10
dist1={
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    'key5':'value5'
}
print(dist1.keys())
print(dist1['key2'])
print('----10----\n')

# 11
str1 = "mark"
print(str1.replace('a',''))

print(str1[0] + str1[2:4])

a = str1.split('a')
b = "".join(a)
print(b)

str1 = "mark"
c=list(str1)
c.remove('a')
d="".join(c)
print(d)
print('----11----\n')

list1.a
str1 = "xvn Meng"
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print('----12----\n')


list4 = [1,2,3,4,9,8,7,6,5]
list4.sort(reverse=True)
print(list4)
print('----13----\n')


