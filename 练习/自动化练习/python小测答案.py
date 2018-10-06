'''
@Project:Python
@Time:2018/9/18 11:05
@Author:xvnmeng
'''
dict1={
    '1':1,
    '2':2
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get('1'))
print(len(dict1))
dict2=dict1.copy()
print(dict2)
dict1['1']='3'
print(dict1['1'])
del dict1['1']
print(dict1)


a=('a1','a2','a3')
list1=['1,2','3,4','5,2']
list2=['a','b','c','d','e']
list2[4]='f'
print(list2)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(3,'7')
print(list1)

list2.reverse()
print(list2)

list3=list1.copy()
print(list3)

str="hello,my friend"
str.capitalize()
a=str.capitalize()
print(a)

a=str.upper()
print(a)

str.lower()
a=str.split('o')
print(a)
b='_'.join(a)
print(b)


