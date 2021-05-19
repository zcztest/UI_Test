# coding:utf-8
from BaseDriver.Base_Driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import URL_BUY
import time

class PageHome(BaseDriver):
    def __init__(self, wd):
        # 子类继承父类中的__init__，使得子类也拥有父类的属性和方法
        BaseDriver.__init__(self, wd)

    def url_enterhome(self):
        self.get(URL_BUY)
        time.sleep(2)

    def sub_SelectProduct(self):
        self.house_click("#newProduct li:nth-of-type(1) [data-original]","#newProduct li:nth-of-type(1) [type]")
        time.sleep(2)

    def chk_enter_succeess(self):
        pass

    def chk_enter_fail(self):
        pass




