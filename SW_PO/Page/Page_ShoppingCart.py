# coding:utf-8

from BaseDriver.Base_Driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import URL_SHOPCART
import time

class PageProductDetail(BaseDriver):
    def __init__(self, wd):
        # 子类继承父类中的__init__，使得子类也拥有父类的属性和方法
        BaseDriver.__init__(self, wd)

    def url_enter_ShopCart(self):
        # <span class="cart_nums">6</span>
        self.click("span[class='cart_nums']")
        # self.get(URL_SHOPCART)
        time.sleep(2)

    def sub_Product(self):
        # self.click("[for='0899e158a29e11eba2ec00163e0cc54c']")
        time.sleep(2)
        # 全选商品按钮 <label for="all" class=""></label>
        self.click("label[for='all']")
        # 结算 <a href="javascript:;" class="btn_sty">结算</a>
        self.click(".btn_sty")
        time.sleep(2)
        # 跳转到订单页面
        self.click("[tabindex='1']")
        time.sleep(2)

    def chk_jump_succeess(self,msg):

        # 下单成功：//body/div[4]/p[.='生成订单成功，接下来为你跳转到订单页面']
        return self.is_text_in_pagesource(msg)


    def chk_jump_fail(self,msg):

        r1 = self.is_element_exist("[data-has-cancel-button] p:nth-child(7)")
        r2 = self.is_text_in_pagesource(msg)
        return r1 and r2
