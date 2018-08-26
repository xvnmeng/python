from selenium import webdriver

# 创建类
class Fuck(object):
    # 构造方法、构造函数，作为上面了绑定的附加属性
    # 附加属性。选择这个类，就有init的属性
    def __init__(self):
        ##################################################
        self.driver = webdriver.Chrome()

        # self.driver = webdriver.Firefox()
        # 打开网站的首页
        self.wangzhi= 'https://mail.qq.com/'
    # 自定义方法
    # 退出浏览器
    def tuichu(self):
        # 可以改动下面的行来更新方法
        self.driver.quit()
    # 窗口最大化
    def zuida(self):
        self.driver.maximize_window()
    # 最小化
    # def min_window(self):
    #     self.driver.minimize_window()

    # 打开网址 url没有是传 斜杠 /
    def dakai(self, url):
        self.driver.get(self.wangzhi+ url)
    def swi(self,string):
        self.driver.switch_to.frame(string)

    # 八大定位
    # attribute:方法属性； value：属性值
    # 属性：id,name,class_name,tag_name,link_text,partial_link_text,xpath,css_selector
    def finde(self, attribute, value):
        if attribute == 'id':
            return self.driver.find_element_by_id(value)
        elif attribute == 'name':
            return self.driver.find_element_by_name(value)
        elif attribute == 'cla':
            return self.driver.find_element_by_class_name(value)
        elif attribute == 'tag':
            return self.driver.find_element_by_tag_name(value)
        elif attribute == 'lin':
            return  self.driver.find_element_by_link_text(value)
        elif attribute == 'par':
            return self.driver.find_element_by_partial_link_text(value)
        elif attribute == 'xpa':
            return self.driver.find_element_by_xpath(value)
        elif attribute == 'cssr':
            return self.driver.find_element_by_css_selector(value)