#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
 
    # 重写元素定位
    def find_element(self,*loc): # *loc任意数量的位置参数（带单个星号参数）
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('页面未找到%s元素' % (loc))
 
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print('页面未找到%s元素' % (loc))
 
    # 重写send_keys
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))
 
    # 封装判断是否存在toast消息，存在返回True,不存在返回False
    def is_toast_exist(self, driver, text):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            print(e)
            return False

