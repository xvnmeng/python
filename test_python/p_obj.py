
def add(a, b):
    print(a + b)
add(3, 5)
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 5))

#类和类成员
class Abb(object):
    def add(self, a, b):
        return a + b
if  __name__ == '__main__':
    count = Abb()
    print(count.add(5, 9))

#新建类
class Abb(object):

    def add(self, a, b):
        return a + b
#Baa集成有Abb的方法类型
class Baa(Abb):

    def sub(self, a, b):
        return a - b
if  __name__ == "__main__":
    count == Abb()
    print(count.add(5, 9))
    count2 = Baa()
    print(count2.add(5, 9))
    print(count2.sub(5, 9))
