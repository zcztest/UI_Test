# coding:utf-8

from BaseDriver.Base_Driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import URL_PRODUCTDETAIL
import time

class PageProductDetail(BaseDriver):
    def __init__(self, wd):
        # 子类继承父类中的__init__，使得子类也拥有父类的属性和方法
        BaseDriver.__init__(self, wd)

    def url_enter_ProductDetail(self):
        self.get(URL_PRODUCTDETAIL)
        time.sleep(2)

    def sub_product(self):
        self.click("[value='加入购物车']")

    def chk_add_succeess(self):
        pass

    def chk_add_fail(self):
        pass