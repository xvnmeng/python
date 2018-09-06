# '''
# @Project:Python
# @Time:2018/9/5 10:43
# @Author:xvnmeng
# '''
#
# from time import sleep
# from selenium import webdriver
# import time
#
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Firefox()
# base_url = 'http://web.zhsmjxc.com/UCenter-webapp/Login/choosePV.htm?productversion=1'
# driver.get(base_url)
#
# # 点击行业
# driver.find_element_by_class_name('industry-01').click()
# # 点击老板
# driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/a').click()
# # 点击体验
# driver.find_element_by_xpath('/html/body/div[25]/div/div/div/a').click()
# time.sleep(1)
#
# a = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/div/ul/li[3]/a')
# ActionChains(driver).move_to_element(a).perform()
#
#
#
#
# # a = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/div/ul/li[3]/a')
# # ActionChains(driver).move_to_element(a).perform()
#
#
# # 遍历读取信息
# # import csv
# # file_o = open(r'D:\code\python\zhihuishangmao\data\customer_massege', mode='r', encoding='utf8')
# # data_r = csv.reader(file_o)
# # for i in data_r:
# #     print(i)
# #     print(i[0])
# #     print(i[1])
# #     print('name')

