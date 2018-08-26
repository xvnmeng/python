'''
@author:xvnmeng
@datetime:2018/8/26 18:40
@software:PyCharm Community Editon
'''
            # 测试类型的三种方法
L = [1]
if type(L) == type([]): print('L is list')
if type(L) == list: print('L is list')
if isinstance(L, list): print('L is list')



# 数字表达式操作符
'''
yield x                             # 生成函数发送协议
lambda args: expression             # 生成匿名函数
x if y else z                       # 三元选择表达式
x and y, x or y, not x              # 与或非
x in y, x not in y                  # 成员对象测试
x is y, x is not y                  # 对象实体测试
x<y, x<=y, x>y, x>=y, x==y, x!=y    # 大小比较操作
1 < a < 3                           # python允许连续比较
x|y, x&y, x^y                       # 位或、位与、位异或
x<<y, x>>y                          # 位操作，x左移或者右移y位
-x, +x, ~x                          # 一元加减、取反
x[i], x[i:j:k], x(...)              # 索引、分片、调用
int(3,14)                           # 强制类型转

'''



            # 整数用 bit_length 函数测试占位数
a = 1;          a.bit_length()  # 1
a = 1024;       a.bit_length()  # 11




#  repr格式更像代码
#  str格式打印出啦对用户更友好




            #  数字相关模块
#  math模块
#  Decimal：小数模块
import decimal
from decimal import Decimal
Decimal('0.01') + Decimal('0.02')           # 返回Decimal('0.03')
decimal.getcontext().prec = 4               # 全局精度为小数点后4位

#  Fraction模块：分数
from fractions import Fraction
x = Fraction(4, 6)                          # 分数类型 4/6
x = Fraction("0.25")                        # 接受参数为1/4的字符串类型







            #  集合set
s = set([3, 5, 9, 10])                      # 创建一个数值集合
t = set("hello")                            # 唯一字符集合
a = t | s                                   # t与s的 并集
b = t & s                                   # 交集
c = t - s                                   # 差集
d = t ^ s                                   # 对称差集
t.add('x')
t.remove('x')
t.update([1,2,3])                            # 更新集合

x in s, x not in s

{x**2 for x in [1,2,3,4]}                   # 集合解析，结果：{1,4,9,16}
{x for x in 'spam'}                         # 结果：{'a','p','s','m'}





#  布尔类型
type(True)                  # 返回<class 'bool'>
isinstance(False,int)       # 返回True，因为bool类是整形
True == 1
True is 1        # 输出（True,False)





#  内置的str函数
str = "a ba Ma"
str.upper()
str.lower()
str.swapcase()          # 大小写转换
str.capitalize()        # 首字母大写
str.title()             # 每个单词首字母大写
width =3
str.ljust(width)        # 获取固定长度，右对齐，左边不够空格补
str.rjust(width)
str.center(width)
str.zfill(width)        # 同ljust
str.find('t', 1, 5)     # 寻找字符串，字符、开始位置、结束位置
str.rfind('t')          # 从右边开始查找字符串
str.count('t')          # 查找字符串出现次数

str.replace('old', 'new')       # 替换
str.startswith('start')         # 是否一xx开头
str.endswith('end')
str.isnumeric()                 # 是否字符
str.isalpha()                   # 是否字母
str.isdigit()                   # 数字
str.islower()                   # 小写
str.isupper()                   # 大写




#  字符串连接
name = "liang" "xun"
name = "liang" \
       "xun"





#  常用列表常亮和操作
L = [1,2,3,4,5,6,7,10,9,8]
L.count(1)
L.append([1,2])             # 向列表尾部单个形式添加数据
L.insert(1,'a')             # 在指定index位置加入数据a
L.extend([1,2,3])           # 整块加入数据
L.index(1)                  # 返回列表中1首次出现的index
L.pop(1)                    # 删除并且返回index处的元素，默认是最后一个
L.remove(1)                 # 只删除首次出现的1
L.reverse()                 # 反转列表
# L.sort(cmp=None,key=None,reverse=False)                    # 排序





# 字典操作
D = {'spam':2, 'tol':{'han':1}}             # 嵌套字典
d = dict.fromkeys(['s', 'd'], 8)             # 都赋值8
D.keys()
D.values()
D.items()
D.get('spam')                               # 通过键获取值
# D.update(D_other)                           # 合并字典
D.pop('spam')                   # 删除
D.popitem()
D.setdefault('spam','aaa')      # 设置某一项，不存在则添加设置为aaa
# del D                           # 删除字典
del D['spam']
key = 'a'
if key in D:
    if key not in D:
        pass                    # 测试是否存在






#  文件基本操作
'''
output = oprn(r'path','w')      # 打开输出文件，写
input = open(r'path','r')       # 打开输入文件，读
fp.read([size])                 # 读取的长度
fp.readline([size])             # 读取一行的长度
fp.readlines([size])            # 读取多行

fp.readable()                   # 是否可读
fp.write(str)                   # 写入str
fp.writelines(seq)              # 多行的seq一次性写入
fp.writeable()                  # 是否可写
fp.close()
fp.flush()                      # 缓冲区的内容写入硬盘
fp.fileno()                     # 返回一个文件标签
fp.isatty()                     # 是否设备终端文件
fp.tell()                       # 返回文件操作的当前标记
fp.next()                       # 返回下一行
fp.seek(offset,where)
fp.truncate([size])             # 裁剪文件大小，默认裁剪到当前操作位置

'''




#  手动迭代
L = [1, 2]
I = iter(L)         # I为L的迭代器
# I.next()            # 返回1
# I.next()            # 返回2
# I.next()            # 错误




#  函数相关语句和表达式
'''
myfunc('a')
def myfunc():
return None
global a
nonlocal x   # 在函数或者其他作用域使用外层变量
yield x      # 生成器函数返回
lambda       # 匿名函数
'''






"""数学运算"""
'''
abs(x)
complex(real,imag)              # 创建一个复数
divmod(a, b)                    # 分别取商和余数
int(x, base)                    # 以base进制转x为整数
long(x)
pow(x, y)                       # x的y次幂（mi）
range(start, stop, step)
round(x, n)                     # 精确到n为的四舍五入
sum(iterable, start)            # 对集合求和
oct(c)                          # 八进制
hex(c)                          # 十六进制
chr(int)                        # 返回int的ASCII字符
unichr(int)                     # 返回unicode
ord(c)                          # 返回ASCII字符对应的整数
bin(x)                          # x转为二进制的字符串
bool(x)                         # x转为bool类型


'''




"""集合操作"""
'''
format(value,foramt_spec)       # 格式化字符串输出 “他是{0},他喜欢{1}"
max(iterable[])                 # 返回集合最大值
min(iterable[])
frozenset(iterable)             # 产生不可变的集合
sorted(iterable)                # 排序

'''




"""逻辑判断"""
'''
all(iterable)          # all为真才是真
any(iterable)          # 一个真为真
cmp(x, y)              # x<y返回负数，x=y返回0

'''




"""IO操作"""
'''
file(filename, mode, bufsize)       # file类型的构造函数
input('aaaa')                       # 获取输入
raw_input()                         # 输入都是作为字符串处理

'''



"""断言 和 异常处理"""
'''
assert 判断条件， 结果

with open('text.txt') as myfile:
    for line in myfile:
    print(line)
    
# 等同于
myfile = open('text.txt')
try:
    for line in myfile:
        print(line)
finally:
    myfile.close()
'''



