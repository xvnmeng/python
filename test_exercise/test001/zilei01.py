from test001.fuck import Fuck
from test001.fulei1 import Fulei01


class Zilei01(Fulei01):
    # 构造方法
    # Zilei01类从Fuck继承属性
    def __init__(self,d:Fuck):
        # 继承方法  继承父类
        self.driver = d
        super().__init__(d)

    def xiexin_click(self):
        # 定位点击写信
        self.driver.finde('id','composebtn').click()

    def tuichu(self):
        self.driver.finde('xpa','/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/a[3]').click()