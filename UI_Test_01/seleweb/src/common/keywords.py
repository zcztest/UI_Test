# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep


class Page(object):
    def __init__(self, driver, logs, imgs):
        self.driver = driver
        self.imgs = imgs
        self.page_logs = logs.Logs('关键字')

    def ele_exist(self, loc, wait=5):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc))
        except Exception as e:
            element = False
            self.page_logs.logger.error('- [ele_exist]方法执行失败，原因：%s' % e)
        return element

    def find_element(self, *loc):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc))
            return element
        except Exception as e:
            self.page_logs.logger.error('- [find_element]方法执行失败，原因：%s' % e)

    def find_elements(self, *loc):
        try:
            elements = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(loc))
            return elements
        except Exception as e:
            self.page_logs.logger.error('- [find_elements]方法执行失败，原因：%s' % e)

    def get_table_rows(self, loc):
        try:
            table = self.find_element(*loc)
            trs = table.find_elements_by_tag_name('tr')
            self.page_logs.logger.info('获取表格[%s，%s]，总行数：' % loc + '[%s]' % len(trs))
            return trs
        except Exception as e:
            self.page_logs.logger.error('- [get_table_rows]方法执行失败，原因：%s' % e)

    def get_table_row_cont(self, loc, text, col=0):
        try:
            trs = self.get_table_rows(loc)
            for r in range(len(trs)):
                td = trs[r].find_elements_by_tag_name('td')
                if td[col].text == text:
                    self.page_logs.logger.info('获取文本[%s]所在行[%s]：' % (text, r + 1))
                    return r+1
                elif r == len(trs) - 1:
                    return -1
        except Exception as e:
            self.page_logs.logger.error('- [get_table_row]方法执行失败，原因：%s' % e)
        return 0

    def get_table_cols(self, loc, row):
        try:
            trs = self.get_table_rows(loc)
            tds = trs[row].find_elements(*loc)
            self.page_logs.logger.info('获取表格[%s，%s]，第：' % loc + '[%s]行的列数为: [%s]' % (row + 1, len(tds)))
            return tds
        except Exception as e:
            self.page_logs.logger.error('- [get_table_cols]方法执行失败，原因：%s' % e)

    def get_table_value(self, loc, row, col):
        try:
            value = self.get_table_cols(loc, row-1)[col-1].text
            self.page_logs.logger.info('获取表格[%s，%s]，第：' % loc + '[%s]行[%s]列的值为: [%s]' % (row, col, value))
            return value
        except Exception as e:
            self.page_logs.logger.error('- [get_table_value]方法执行失败，原因：%s' % e)

    def set_date(self, loc, tdate):
        pass

    def select_element(self, loc, val):
        eles = self.find_elements(*loc)
        if val.find('-') > 0:
            for i in val.split('-'):
                self.select_element(loc, i)
        for ele in eles:
            if ele.text == val:
                ele.click()
                sleep(1)
                break

    def set_select_value(self, loc, val):
        try:
            ele = self.find_element(*loc)
            Select(ele).select_by_value(val)
            self.page_logs.logger.info('在下拉框元素[%s，%s]，选择：' % loc + '[%s]' % val)
        except Exception as e:
            self.page_logs.logger.error('- [set_select_value]方法执行失败，原因：%s' % e)

    def open(self, url):
        self.driver.get(url)
        self.page_logs.logger.info('打开网页[%s]' % url)

    def make_maxwindow(self):
        self.driver.maximize_window()
        self.page_logs.logger.info('最大化浏览器')

    def set_winsize(self, wide, hight):
        self.driver.set_window_size(wide, hight)
        self.page_logs.logger.info('设置窗口尺寸宽[%s]高[%s]' % (wide, hight))

    def set_value(self, loc, text):
        try:
            ele = self.find_element(*loc)
            ele.send_keys(text)
            self.page_logs.logger.info('在元素[%s，%s]，输入：' % loc + '[%s]' % text)
        except TimeoutException as e:
            self.page_logs.logger.error('- set_value()方法执行失败，原因TimeoutException:%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- 用例执行失败，原因：%s' % e)

    def clear_input_text(self, loc, text):
        try:
            ele = self.find_element(*loc)
            ele.clear()
            ele.send_keys(text)
            self.page_logs.logger.info('清空元素[%s，%s]内容，并输入' % loc + '[%s]' % text)
        except TimeoutException as e:
            self.page_logs.logger.error('- clear_input_text()方法执行失败，原因TimeoutException：%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- 用例执行失败，原因：%s' % e)

    def element_clear(self, loc):
        try:
            ele = self.find_element(*loc)
            ele.clear()
            sleep(1)
            self.page_logs.logger.info('点击[%s，%s]的元素并清空内容' % loc)
        except TimeoutException as e:
            self.page_logs.logger.error('- [clear]方法执行失败，原因TimeoutException：%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- 用例执行失败，原因：%s' % e)

    def left_click(self, loc):
        try:
            ele = self.find_element(*loc)
            ele.click()
            sleep(1)
            self.page_logs.logger.info('点击[%s，%s]的元素' % loc)
        except TimeoutException as e:
            self.page_logs.logger.error('- [left_click]方法执行失败，原因TimeoutException：%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- [left_click]执行失败，原因：%s' % e)

    def right_click(self, loc):
        try:
            ele = self.find_element(*loc)
            ActionChains(self.driver).context_click(ele).perform()
            self.page_logs.logger.info('右键点击[%s，%s]的元素' % loc)
        except TimeoutException as e:
            self.page_logs.logger.error('- [right_click]方法执行失败，原因TimeoutException：%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- [right_click]执行失败，原因：%s' % e)

    def move_element(self, loc):
        ele = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page_logs.logger.info('鼠标移动到[%s，%s]元素' % loc)

    def move_table_element(self, ele):
        ActionChains(self.driver).move_to_element(ele).perform()

    def double_click(self, loc):
        ele = self.find_element(*loc)
        ActionChains(self.driver).double_click(ele).perform()
        self.page_logs.logger.info('双击[%s，%s]元素' % loc)

    def drag_and_drop(self, e1, e2):
        ActionChains(self.driver).drag_and_drop(e1, e2).perform()

    def click_text(self, loc):
        ele = self.find_element(loc)
        ele.click()
        self.page_logs.logger.info("点击超链接元素：[%s，%s]" % loc)

    def close(self):
        self.driver.close()
        self.page_logs.logger.info('关闭浏览器当前窗口')

    def browser_quit(self):
        self.page_logs.logger.info('退出浏览器\n')
        self.driver.quit()

    def submit(self, loc):
        ele = self.find_element(*loc)
        ele.submit()
        self.page_logs.logger.info("提交表单，元素：[%s，%s]" % loc)

    def refresh(self):
        self.page_logs.logger.info('刷新页面')
        self.driver.refresh()
        self.driver.implicitly_wait(5)

    def js(self, sprit):
        sleep(2)
        self.page_logs.logger.info('执行js：%s' % sprit)
        self.driver.execute_script(sprit)

    def get_attribute(self, loc, attribute):
        ele = self.find_element(*loc)
        return ele.get_attribute(attribute)

    def get_text(self, loc):
        try:
            ele1 = self.find_element(*loc)
            if ele1.text is None or ele1.text == '':
                sleep(3)
                ele2 = self.find_element(*loc)
                self.page_logs.logger.info('重试，获取[%s，%s]' % loc + '元素的文本值，return:[%s]' % ele2.text)
                return ele2.text
            else:
                self.page_logs.logger.info('获取[%s，%s]' % loc + '元素的文本值，return:[%s]' % ele1.text)
                return ele1.text
        except TimeoutException as e:
            self.page_logs.logger.error('- [get_text]方法执行失败，原因：TimeoutException:%s' % e)
        except Exception as e:
            self.page_logs.logger.error('- 用例执行失败，原因：%s' % e)

    def get_title(self):
        title = self.driver.title
        self.page_logs.logger.info('获取当前页面的[title]，return：[%s]' % title)
        return title

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.page_logs.logger.info('获取当前窗口的截图。')

    def accept_warning_box(self):
        self.page_logs.logger.info('接受警告框')
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, loc):
        self.page_logs.logger.info('切换到iframe表单')
        if1 = self.find_element(*loc)
        self.driver.switch_to.frame(if1)

    def browser_driver(self):
        return self.driver
