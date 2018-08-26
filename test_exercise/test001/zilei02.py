import time

from test001.fuck import Fuck
from test001.zilei01 import Zilei01


class Zilei02(Zilei01):
    # 构造方法
    # Zilei01类从Fuck继承属性
    def __init__(self,d:Fuck):
        # 继承方法  继承父类
        self.driver = d
        super().__init__(d)
    #     self.driver.finde('xpa','/html/body/div/div[1]/div/div[2]/span[2]/a[1]').click()

    def shoujian(self):
        # 定位收件人
        self.driver.finde('xpa','/html/body/form[2]/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[4]/div[1]/div/div/div/a').click()
        self.driver.finde('xpa','/html/body/form[2]/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[4]/div[2]/div[10]/a').click()

    def xiexin(self,zhuti,neirong):
        time.sleep(1)
        # 定位主题
        self.driver.finde('id','subject').send_keys(zhuti)
        time.sleep(1)
        # 定位内容
        self.driver.swi('mainFrame')
        self.driver.finde('xpa','/html/body/form[2]/div[2]/div[7]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/iframe').send_keys(neirong)
        time.sleep(1)
        # 定位发送
        self.driver.finde('xpa','/html/body/form[2]/div[3]/div/a[1]').click()
        time.sleep(1)