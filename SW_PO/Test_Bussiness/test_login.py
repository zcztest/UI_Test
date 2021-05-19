# coding:utf-8

# from SeleniumWebdriverPO.Page.Page_Login import PageLogin
from Page.Page_Login import PageLogin
from selenium import webdriver
# from SeleniumWebdriverPO.mylog import log
from mylog import log
from unittest import TestCase
import unittest
# from SeleniumWebdriverPO.config import DRIVER_PATH
from config import DRIVER_PATH
# pip install unittestreport
# 失败重试
from unittestreport import rerun
import ddt

@ddt.ddt
class TestLogin(TestCase):
    def setUp(self) -> None:
        self.wd = webdriver.Chrome(DRIVER_PATH)
        self.login = PageLogin(self.wd)

    def tearDown(self) -> None:
        self.wd.quit()

    def test_1_login_success(self):
        self.login.url_login()
        self.login.sub_login('gyppp@qq.com', '123456', '1111')
        self.login.chk_login_success('g6627738')

    @ddt.data(['gyppp@qq.com', '1234', '1111', '用户名或者密码错误'],
              ['@qq.com', '123456', '1111', '用户名或者密码错误']
              )
    # @unittest.skipIf(True, "暂时不执行")
    def test_login_fail(self, p):
        self.login.url_login()
        self.login.sub_login(p[0], p[1], p[2])
        self.login.chk_login_fail(p[3])
