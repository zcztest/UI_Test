from appium import webdriver
import time
import unittest
from pages.login_page import LoginPage
from pages.my_page import MyPage
from pages.set_page import SetPage
from common.My_swipe import swipe_up
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class Test_lgin(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'android',
            'deviceName': '740dc3d1',
            'platformVersion': '8.0.0',
            'appPackage': 'com.mld.LanTin',
            'appActivity': 'com.mld.LanTin.main.activity.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        # 配置
        cls.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        # 实例化
        # 每子页面的page类都继承了basepage父类，而basepage父类需要传入driver来初始化，所以子类也需传driver来实例化
        cls.login_page = LoginPage(cls.driver)
        cls.my_page = MyPage(cls.driver)
        cls.set_page = SetPage(cls.driver)
 
    def test_login01(self):
        u'微信登录成功'
        self.my_page.click_my()
        self.my_page.click_login_button()
        self.login_page.wechat_login()
        time.sleep(11)
        # 获取当前context
        cont = self.driver.current_context
        print(cont)
        # 切换至当前context
        self.driver.switch_to.context(cont)
        print(self.driver.current_context)
        time.sleep(1)
        # 登录后返回我的页面，验证用户名
        t = self.login_page.show_name()
        print(t)
        # 断言是否登录成功
        self.assertEqual('我是一朵花', t)
 
    def test_login02(self):
        # 向上滑动
        swipe_up(self.driver)
        # 退出登录
        self.set_page.logout()
        # 检查是否退出成功
        t2 = self.driver.current_context
        self.driver.switch_to.context(t2)
        time.sleep(2)
        # 当前页面若有登录按钮则推出成功
        try:
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(self.login_page.submit_loc))
            print('退出登录成功')
            return True
        except Exception as e:
            raise
 
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
 
if __name__=='__main__':
    unittest.main()

