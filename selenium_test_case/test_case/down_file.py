'''
@author:xvnmeng
@datetime:2018/8/21 21:58
@software:PyCharm Community Editon
'''
from selenium import webdriver
from time import sleep
import os

fp = webdriver.FirefoxProfile()

# ���浽ָ��Ŀ¼
fp.set_preference('browser.download.foldList',2)
# ����ʾ
fp.set_preference('browser.download.manager.showWhenStarting',False)
fp.set_preference('browser.download.dir', os.getcwd())
# �����ļ�����
fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octer-stream')

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("url")
driver.find_element_by_link_text('text').click()

