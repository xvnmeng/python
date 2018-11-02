'''
@Project:Python
@Time:2018/8/21 15:53
@Author:xvnmeng
'''
# 导入下拉框的定位方法
from selenium.webdriver.support.select import Select
# 从baiduMainPage这个项目的auto_driveer文件夹的
# auto_driver这个python文件，导入AutoDriver这个类（一句话：引入吃喝嫖赌这个动作集合）
from baiduMainPage.auto_driveer.auto_driver import AutoDriver

# 定义一个基本页面的类    可以这样理解：这是定义去那个街区酒楼吃喝嫖赌
class BasePage(object):

    # BasePage类从AutoDriver继承属性  相当于有driver、和base_url属性
    def __init__(self, d:AutoDriver):
        # 这里的driver也继承了AUtoDriver类的吃喝嫖赌
        self.driver = d

    # 登录点击          --》相当于：去饭馆吃
    def login_click(self):
        self.driver.find_elements('xpath', '//*[@id="u1"]/a[7]').click()

    # 点击新闻          --》相当于：去青楼嫖
    def news_click(self):
        self.driver.find_elements('xpath', '//*[@id="u1"]/a[1]').click()

    # 点击hao123          --》相当于：去赌档赌
    def hao123_click(self):
        self.driver.find_elements('xpath', '//*[@id="u1"]/a[2]').click()

    # 点击地图          --》相当于：去酒楼喝
    def map_click(self):
        self.driver.find_elements('xpath', '//*[@id="u1"]/a[3]').click()

    # 点击视频          --》相当于：去公园玩
    def video_click(self):
        self.driver.find_elements('xpath', '//*[@id="u1"]/a[4]').click()
