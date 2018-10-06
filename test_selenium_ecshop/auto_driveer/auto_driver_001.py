'''
@Project:Python
@Time:2018/8/20 17:08
@Author:xvnmeng


用户自定义函数  user_defined_function
'''

from selenium import webdriver

# 创建类
class AutoDriver001(object):
    # 构造方法、构造函数，作为上面了绑定的附加属性
    # 附加属性。选择这个类，就有init的属性
    def __init__(self):
        self.driver = webdriver.Firefox()
        # 打开ecshop的首页
        self.base_url = 'http://localhost/upload'

    # 自定义方法
    # 退出浏览器
    def quit_browser(self):
        # 可以改动下面的行来更新方法
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
        # 定义一个传入参数不正确的方法