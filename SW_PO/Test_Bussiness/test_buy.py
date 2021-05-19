# coding:utf-8

from Page.Page_Order import PageOrder
from Page.Page_Home import PageHome
from Page.Page_ShoppingCart import PageProductDetail
from Page.Page_Login import PageLogin
from selenium import webdriver
from mylog import log
from unittest import TestCase
import unittest
from config import DRIVER_PATH
# pip install unittestreport
# 失败重试
from unittestreport import rerun
import ddt

class TestBuy(TestCase):
    def setUp(self) -> None:
        self.wd = webdriver.Chrome(DRIVER_PATH)
        self.login = PageLogin(self.wd)
        self.home = PageHome(self.wd)
        self.order = PageOrder(self.wd)
        self.shop = PageProductDetail(self.wd)


    def tearDown(self) -> None:
        self.wd.quit()

    def test_buy_success(self):
        # 登录
        self.login.url_login()
        self.login.sub_login('gyppp@qq.com', '123456', '1111')
        self.login.chk_login_success('g6627738')
        # 进入首页，选择商品
        self.home.url_enterhome()
        self.home.sub_SelectProduct()
        # 进入订单页面，
        self.order.url_enter_Order()
        self.order.sub_confirmOrder()
        # 购买
        self.shop.url_enter_ShopCart()
        self.shop.sub_Product()

    '''    
    def test_buy_fail(self):
        pass
    '''




