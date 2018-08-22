'''
@author:xvnmeng
@datetime:2018/8/21 21:48
@software:PyCharm Community Editon
'''
from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

# 定位上传按钮，添加文件
driver.find_element_by_name('file').send_keys('upload_file.txt')

driver.quit()