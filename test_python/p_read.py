'''
@Project:Python
@Time:2018/8/13 13:50
@Author:xvnmeng
'''
#f = open('test.txt')
#for row in f:
#    print(row)
#f.close()

#写语句
import csv

list = ['1', '2','3','4']
out = open('test.csv', 'w')
csv_writer = csv.writer(out)
csv_writer.writerow(list)

#csv_writer = csv.writer(out, dialect='excel')
#csv_writer.writerrow(list)
