# -*- coding: utf-8 -*-
from src.common import ddt
from src.pages.search_page import SearchPage
from src.common.init_test_suite import InitTest
from src.common.init_test_suite import init_data
from config.config import data_file


@ddt.ddt
class TestSearch(InitTest):
    test_data = init_data(data_file, '百度搜索')

    @ddt.data(*test_data)
    def test_search(self, data_dic):
        test_logs = self.logs.Logs('百度测试')
        test_logs.logger.info('初始化测试数据：%s' % data_dic)
        search_page = SearchPage(self.driver, self.logs, self.imgs)
        kw = data_dic.get('搜索')
        expected_value = data_dic.get('预期结果')

        search_page.open_browser()
        search_page.make_maxwindow()
        search_page.input_search_text(kw)
        search_page.click_search_btn()

        search_page.add_img()

        actual_value = search_page.get_title()
        self.assertEqual(expected_value, actual_value)
        test_logs.logger.info('断言预期结果：[%s]是否等于实际结果：[%s]' % (expected_value, actual_value))
