'''
@Project:Python
@Time:2018/9/5 9:33
@Author:xvnmeng
'''
from selenium import webdriver
from selenium.webdriver import ActionChains


class AutoDriver001(object):
    # 构造方法、构造函数，作为上面了绑定的附加属性
    def __init__(self):
        self.driver = webdriver.Firefox()
        # 打开智慧商贸的指定页面
        self.base_url = 'http://web.zhsmjxc.com/UCenter-webapp/Login/choosePV.htm?productversion=1'

    # 定义悬浮
    def action_chains(self, val):
        a = self.driver.find_element_by_xpath(val)
        ActionChains(self.driver).move_to_element(a).perform()

    def iframe(self, val):
        # self.driver.switch_to.frame(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(val))

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 窗口最大化
    def max_window(self):
        self.driver.maximize_window()

    # 最小化
    def min_window(self):
        self.driver.minimize_window()

    # 打开网址 url没有是传 斜杠 /
    def open_url(self, url):
        self.driver.get(self.base_url + url)

    # 八大定位
    # attribute:方法属性； value：属性值
    # 属性：id,name,class_name,tag_name,link_text,partial_link_text,xpath,css_selector
    def find_elements(self, attribute, value):
        if attribute == 'id':
            return self.driver.find_element_by_id(value)
        elif attribute == 'name':
            return self.driver.find_element_by_name(value)
        elif attribute == 'class_name':
            return self.driver.find_element_by_class_name(value)
        elif attribute == 'tag_name':
            return self.driver.find_element_by_tag_name(value)
        elif attribute == 'link_text':
            return  self.driver.find_element_by_link_text(value)
        elif attribute == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(value)
        elif attribute == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif attribute == 'css_selector':
            return self.driver.find_element_by_css_selector(value)