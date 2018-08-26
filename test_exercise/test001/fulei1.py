import time

# from autodriver.fengzhuang import Fuck

##################
from test001.fuck import Fuck


class Fulei01(object):
    # Fulei01类从Fuck继承属性
    def __init__(self,d:Fuck):
        self.driver = d
    def xuanze(self):
        # 点击账户
        self.driver.swi('login_frame')
        # self.driver.finde('id','switcher_plogin').click()
    def denglu(self,name,passwd):
        # 定位帐号输入
        self.driver.finde('id','u').send_keys(name)
        time.sleep(1)
        # 点击密码输入
        self.driver.finde('xpa','/html/body/div[1]/div[4]/div/div/div[2]/form/div[2]/div[1]/input').send_keys(passwd)
        time.sleep(1)
        # 点击登录
        self.driver.finde('id','login_button').click()
        time.sleep(30)
