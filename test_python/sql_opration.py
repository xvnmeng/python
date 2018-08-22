'''
@Project:Python
@Time:2018/8/14 14:10
@Author:xvnmeng
'''
# # 输出偶数
# for i in range(0,103,2):
#     print(i)
#
# # 创建列表,替换
# list = ["a", "b", "c", "d", "e", "f"]
# for i in range(1,4):
#     list[i] = "mark"
# print(list)
#
# #list1降序排列
# list1 = [1,2,3,5,6,8,7,10]
# list1.sort(reverse=True)
# print(list1)

# import pymysql
# # # 连接数据库
# # conn = pymysql.connect(host='localhost', user='root', passwd='',
# #                        port=3306,db='ecshop')
# # # 通过连接数据库 创建游标 ： 声明游标类型= 字典游标
# # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# # # 通过游标执行sql语句
# # effect_row = cursor.execute("select * from ecs_users")
# # print(cursor.execute("select * from ecs_users"))
# # cursor.
# # # 打印受影响的行
# # print(effect_row)
# # # 提交修改
# # conn.commit
# # # 关闭游标
# # cursor.close()
# # # 断开数据库连接
# # conn.close()


# import pymysql
# db = pymysql.connect(host='localhost', user='root', passwd='',
#           port=3306,db='ecshop')
# cursor = db.cursor()
# # 执行查询语句
# # cursor.execute("select version()")
# cursor.execute("select * from ecs_users")
# # fetchone()方法获取单条数据
# data = cursor.fetchone()
# print(data)
# db.close()


