# coding:utf-8
from BaseDriver.Base_Driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import *
import time

class PageOrder(BaseDriver):
    def __init__(self, wd):
        # 子类继承父类中的__init__，使得子类也拥有父类的属性和方法
        BaseDriver.__init__(self, wd)

    def url_enter_Order(self):
        self.webdriver.switch_to_window(self.webdriver.window_handles[1])

    def sub_confirmOrder(self):
        # self.click("img[src='/static/images/finalbutton.gif]")
        self.click("input[id='addCart']")
        # <input id="addCart" class="addCart" value="加入购物车" type="button">
        time.sleep(2)

    def chk_confirm_succeess(self):
        pass

    def chk_comfirm_fail(self):
        pass
