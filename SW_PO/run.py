# coding:utf-8
import unittest
from HtmlTestRunner import HTMLTestRunner

discover = unittest.defaultTestLoader.discover("./Test_Bussiness/", pattern="test_buy.py")
r = HTMLTestRunner(combine_reports=True)
r.run(discover)
