# -*- coding: utf-8 -*-
from config.config import report_file
from config.config import browser, driver_file, testcase_path, description, report_title, tester, test_objects
from config import logs
from selenium import webdriver
from src.common.HTMLTestRunner import HTMLTestRunner
import unittest
import xlrd
import yaml


class InitTest(unittest.TestCase):
    driver = None
    logs = None
    init_logs = None

    @classmethod
    def setUpClass(cls):
        cls.imgs = []
        cls.logs = logs
        cls.init_logs = cls.logs.Logs('测试初始化')
        if browser.lower() == 'chrome':
            cls.driver = webdriver.Chrome(driver_file)
        elif browser.lower() == 'firefox':
            cls.driver = webdriver.Firefox(driver_file)
        else:
            raise NameError("- [InitTest]初始化失败浏览器只能为：chrome，firefox；请检查config.py的browser是否正确")
        cls.init_logs.logger.info('开始执行测试用例')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.init_logs.logger.info('测试用例执行完成\n')

    # def setUp(self):
    #     self.imgs = []
    #     self.logs = logs
    #     self.init_logs = self.logs.Logs('测试初始化')
    #     if browser.lower() == 'chrome':
    #         self.driver = webdriver.Chrome(driver_file)
    #     elif browser.lower() == 'firefox':
    #         self.driver = webdriver.Firefox(driver_file)
    #     else:
    #         raise NameError("- [InitTest]初始化失败浏览器只能为：chrome，firefox；请检查config.py的browser是否正确")
    #     self.init_logs.logger.info('开始执行测试用例')
    #
    # def tearDown(self):
    #     self.driver.quit()
    #     self.init_logs.logger.info('测试用例执行完成\n')


def runtest():
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test*.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)

    report = open(report_file, 'wb')
    runner = HTMLTestRunner(stream=report, title=report_title, description=description, tester=tester)
    runner.run(test_suit)
    report.close()


def init_data(data_path, flow_name):
    datas_logs = logs.Logs('初始化测试数据')
    try:
        sheets = xlrd.open_workbook(data_path).sheets()
        data_list = []
        for sheet in sheets:
            nrows = sheet.nrows
            for i in range(1, nrows):
                if sheet.cell(i, 3).value == '是':
                    tmp_dic = {}
                    # 系统模块
                    tmp_dic['业务流名称'] = sheet.cell(i, 1).value
                    if tmp_dic['业务流名称'] == flow_name:
                        # 用例名称
                        tmp_dic['用例名称'] = sheet.cell(i, 2).value
                        tmp_dic.update(eval(sheet.cell(i, 4).value))
                        tmp_dic.update(eval(sheet.cell(i, 5).value))
                        data_list.append(tmp_dic)
        return data_list
    except Exception as e:
        datas_logs.logger.error('获取测试用例数据失败，原因：%s' % e)


def init_objects(page_object):
    file = open(test_objects, "r", encoding="utf-8")
    objects = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return objects[page_object]
