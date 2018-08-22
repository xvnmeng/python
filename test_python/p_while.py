'''
@Project:Python
@Time:2018/8/13 12:57
@Author:xvnmeng
'''
#while 语句
numbers = [12, 37, 5, 42, 8 ,3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop() #随机取出一个
    if number % 2 == 0:
        even.append(number) #添加一个
    else:
        odd.append(number)

count: int = 0
while (count < 9):
    print('The count is:',count)
    count +=1
print("Good bye!")

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break