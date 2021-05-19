# coding:utf-8
# from SeleniumWebdriverPO.BaseDriver.Base_Driver import BaseDriver
from BaseDriver.Base_Driver import BaseDriver
from selenium.webdriver.common.by import By
#from SeleniumWebdriverPO.config import URL_LOGIN
from config import URL_LOGIN
import time


# Page这一层，需要继承BaseDriver这个父类
class PageLogin(BaseDriver):
    def __init__(self, wd):
        # 子类继承父类中的__init__，使得子类也拥有父类的属性和方法
        BaseDriver.__init__(self, wd)

    def url_login(self):
        self.get(URL_LOGIN)
        time.sleep(2)

    def sub_login(self, user, pwd, code):
        self.input(user, "[name='email']")
        self.input(pwd, "[name='password']")
        self.input(code, "[id='changeCode']")
        self.click("[value='登 录']")

    def chk_login_success(self, msg):
        return self.is_text_in_pagesource(msg)

    def chk_login_fail(self, msg):
        r1 = self.is_element_exist("[id='changeCode']")
        r2 = self.is_text_in_pagesource(msg)
        return r1 and r2
