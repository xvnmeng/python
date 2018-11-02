'''
@Project:Python
@Time:2018/8/20 17:08
@Author:xvnmeng
用户自定义函数  user_defined_function
'''
# 从selenium这个包导入webdriver（网页驱动）这个库
from selenium import webdriver

# 创建类（相当于定义各种动作、行为）
# 假设AutoDriver是一个动作集合，那么它包含吃、喝、嫖、赌、学、玩等动作
class AutoDriver(object):

    # 构造方法，作为上面了绑定的附加属性
    # 附加属性。选择了Autodriver，就会有_init_的属性
    def __init__(self):
        # 定义驱动chrome浏览器的函数，并赋值给driver   --》driver：开车去
        self.driver = webdriver.Chrome()
        # 网址参数化                                --》base_url:导航去
        self.url = 'http://www.baidu.com'

    # 定义退出浏览器的方法===================相当于-》吃
    def quit_browser(self):
        self.driver.quit()

    # 窗口最大化=========================相当于-》喝
    def max_window(self):
        self.driver.maximize_window()

    # 窗口最小化=========================相当于嫖
    def min_window(self):
        self.driver.minimize_window()

    # 打开网页===========================相当于赌
    def open_url(self):
        self.driver.get(self.url)

    # 八大定位===========================相当于-》玩====有8种玩法
    # if……else语句====定义八种玩法只能选择一项
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
            return self.driver.find_element_by_link_text(value)
        elif attribute == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(value)
        elif attribute == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif attribute == 'css_selector':
            return self.driver.find_element_by_css_selector(value)