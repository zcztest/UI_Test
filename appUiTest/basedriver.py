from appium import webdriver
import time

def android_driver():

    desired_caps = {
        'platformName':'Android',
        'deviceName': '1f1141308b',
        'udid':'3ced88a',   # adb device 获得的字符串
        'platformVersion':"5.1",
        'appPackage':'cn.xuexi.android',
        'appActivity':'com.alibaba.android.rimet.biz.home.activity.HomeActivity',
        'unicodeKeyboard': True,
        'resetKeyBoard': True,
        'noReset': True,
        # "automationName":"uiautomator2"

    }
    
    #使用adb命令可以查看当前运行的包名和activity
    #adb shell dumpsys window | findstr mCurrentFocus

    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    time.sleep(3)
    d = driver.current_activity
    print(d)
    return driver
'''
def ios_drvier():
    desired_caps = {
    
    }
'''

if __name__=='__main__':
    driver = android_driver()

