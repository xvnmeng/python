'''
@author:xvnmeng
@datetime:2018/8/21 21:58
@software:PyCharm Community Editon
'''
from selenium import webdriver
from time import sleep
import os

fp = webdriver.FirefoxProfile()

# 保存到指定目录
fp.set_preference('browser.download.foldList',2)
# 不显示
fp.set_preference('browser.download.manager.showWhenStarting',False)
fp.set_preference('browser.download.dir', os.getcwd())
# 下载文件类型
fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octer-stream')

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("url")
driver.find_element_by_link_text('text').click()

