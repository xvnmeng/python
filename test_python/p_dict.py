'''
@Project:Python
@Time:2018/8/13 13:03
@Author:xvnmeng
'''
lists = [1, 2, 3, "a", 5, "8"]
print(lists)
print(lists[0])
print(lists[4])
lists[4] = "b"
print(lists[4])
print(lists)
print(len(lists))

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[0])
print(tup2[1:5])

dicts = {"username":"zhangsan", "password":"123456"}
print(dicts.keys())
print(dicts.values())
print(dicts.items())
print(dicts)
print(dicts.get("username"))
dicts2 = dicts.copy()
print(dicts2)

for key,value in dicts.items():
    print(key)
    print(value)

order = {
    "message":"ok",
    "nu":"123456",
    "companytype":"zhongtong",
    "ischeck":"1",
    "com":"zhongtong",
    "status":"200",
    "condition":"F00"
}
for key in order.keys():
    print(key)
for value in order.values():
    print(value)
for key, value in order.items():
    print((key, value))