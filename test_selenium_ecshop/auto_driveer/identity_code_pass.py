'''
@Project:Python
@Time:2018/8/17 11:43
@Author:xvnmeng
'''
import re
from typing import Dict, List, Any, Union
from selenium import webdriver
# from PIL import Image
import pytesseract
# import os,time
import time

# # chromedriver = "D:\Program Files\Anaconda3\selenium\webdriver\chromedriver.exe" #这里写本地的chromedriver 的所在路径
# # os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
# # driver = webdriver.Chrome(chromedriver)
#
# driver = webdriver.Firefox()
# driver.maximize_window() #浏览器最大化
# # 打开网址 脚本之家有验证码
# driver.get("http://tougao.jb51.net/index.php?c=index&a=login&forward=http%3A%2F%2Ftougao.jb51.net%2F") #该处为具体网址
# # driver.refresh() #刷新页面
# #获取全屏图片，并截取验证码图片的位置
# driver.get_screenshot_as_file('a.png')
# # 通过id查找图片  获取尺寸
# location = driver.find_element_by_id('code_img').location
# size = driver.find_element_by_id('code_img').size
# # 通过定位左上角和右下角实现图片定位
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
#
# print(left)
# print(top)
# print(right)
# print(bottom)
#
# a = Image.open("a.png")
# im = a.crop((left,top,right,bottom))
# im.save('a.png')
# time.sleep(1)
#
# #打开保存的验证码图片


# image = Image.open(r"D:\code\python\a.png")
# print(image)
# vcode = pytesseract.image_to_string(image)  ## 识别的时候没有安装包
# vcode = pytesseract.image_to_string(image)
# print(vcode)
# #填充用户名 密码 验证码
# driver.find_element_by_id("staffCode").send_keys("username")
# driver.find_element_by_id("pwd").send_keys("password")
# driver.find_element_by_id("validateCode").send_keys(vcode)
# #点击登录
# driver.find_element_by_id("loginBtn").click()
# driver.quit(2)


# from PIL import Image as myImage
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = 'c:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "c:/Program Files (x86)/Tesseract-OCR/tessdata"'
#
# text = ''
#
# img = myImage.open(r'D:\code\python\a.png')
# # img.load()
# text = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)
#
#
# image = myImage.open(r"D:\code\python\a.png")
# print(image)
# vcode = pytesseract.image_to_string(image)  ## 识别的时候没有安装包
# print(text)
# print('aaa   %s ' % vcode)

#
# import pytesseract
# from PIL import Image
# # 访问相对路径如下图，绝对路径是下一行代码
# image = Image.open(r'D:\2.jpg')
#
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#
# tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
#
# code = pytesseract.image_to_string(image)
#
# print(code)
#



import csv

csv_file1=open(r'D:\code\python\test_selenium_ecshop\data_file\username.csv', mode='r', encoding='utf8')
csv_data1=csv.reader(csv_file1)
for i in csv_data1:
    user_dict={
        'year':i[0],
        'month':i[1],
        'dav':i[2],
        'email':i[3],
        'msn':i[4],
        'qq':i[5],
        'office':i[6],
        'family':i[7],
        'phone':i[8],
        'answer':i[9]
    }
    print(user_dict)
    # 1999,9,1,wadf@qq.com,ada@sd.com,2131321321,12341234,123412341,124123412,kk