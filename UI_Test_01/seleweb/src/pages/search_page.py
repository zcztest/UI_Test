# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from src.common.keywords import Page
from src.common.base_element import Element
from src.common.init_test_suite import init_objects


class SearchPage(Page, Element):
    def __init__(self, driver, logs, img):
        # 初始化登录页面对象库
        super().__init__(driver, logs, img)
        self.login_logs = logs.Logs('百度页面对象')
        search_objects = init_objects('search')
        self.login_logs.logger.info('初始化页面元素对象：%s' % search_objects)
        self.url = search_objects.get('url')
        self.ele_username = search_objects.get('kw')
        self.ele_password = search_objects.get('su')

    def input_search_text(self, text):
        self.set_value(self.get_element(By.ID, 'kw'), text)

    def click_search_btn(self):
        self.left_click(self.get_element(By.ID, 'su'))

    def open_browser(self):
        self.open(self.url)
