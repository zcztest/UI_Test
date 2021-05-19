# coding: utf-8
import uiautomator2 as u2
import time
from appium.webdriver import webdriver
from base import Action

# adb shell dumpsys activity | findstr "mFocusedActivity"
# com.alibaba.lightapp.runtime.activity.CommonWebViewActivity 积分页面

d = u2.connect()  #括号内为adb devices获取的设备号
time.sleep(2)
d.screen_on()
d.implicitly_wait(30)
d.swipe(0.35, 0.95, 0.85, 0.15)
d.app_start("cn.xuexi.android")   #括号内为要启动的APP包名
time.sleep(2)


class studyTest(Action):

    def __init__(self,d):
        Action.__init__(self,d)

    def enter_Score():
        d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        time.sleep(3)
        kan = d(text="去看看")
        print(kan.count)
        time.sleep(2)

    def sub_Read(): # 我要阅读文章 学习强国的要闻，是要多一点
        # d.xpath('//android.widget.ListView/android.view.View[2]/android.view.View[4]').click()
        d(text="去看看")[0].click()
        time.sleep(3)
        d.swipe(0.35, 0.85, 0.85, 0.25)
        docs = d(resourceId='cn.xuexi.android:id/general_card_title_id')
        print(docs)
        print(docs.count)
        for elm in docs:
            print(elm)
            elm.click()
            time.sleep(65)
            d.swipe(0.35, 0.85, 0.65, 0.25)
            time.sleep(60)
            print("OKKKKKKKKKKKK")
            d.press("back")
            time.sleep(1)

    def sub_Watch(): # 视听学习 看视频，在第一频道有很多视频；
        d(text="去看看")[1].click()
        time.sleep(2)
        # cn.xuexi.android:id/general_card_title_id
        d.swipe(0.35, 0.85, 0.85, 0.25)
        video = d(resourceId='cn.xuexi.android:id/general_card_title_id')
        print(video)
        print(video.count)
        for elm in video:
            print(elm)
            elm.click()
            time.sleep(65)
            d.swipe(0.35, 0.85, 0.65, 0.25)
            time.sleep(60)
            print("OKKKKKKKKKKKK")
            d.press("back")
            time.sleep(1)

    def sub_Study(): # 视听学习时长
        d.swipe(0.35,0.85,0.85,0.25)
        if d.exists(text="去学习") == True:
            pass
        d(text="去学习").click()  # 需要加一个判断，判断“去学习”按钮是否变成“已完成”；
        time.sleep(2)
        d.swipe(0.35, 0.95, 0.85, 0.15)
        video = d(resourceId='cn.xuexi.android:id/general_card_title_id')
        print(video)
        print(video.count)
        for elm in video:
            print(elm)
            elm.click()
            time.sleep(65)
            d.swipe(0.35, 0.85, 0.65, 0.25)
            time.sleep(60)
            print("OKKKKKKKKKKKK")
            d.press("back")
            time.sleep(1)

    def sub_Dayanwser(): # 每日答题
        d.swipe(0.35, 0.85, 0.85, 0.25)
        d.xpath('//android.widget.ListView/android.view.View[5]/android.view.View[4]').click()
        time.sleep(2)
        d(text="退出").click()

    def sub_Weekanwser():  # 每日答题
        d.swipe(0.35, 0.85, 0.85, 0.25)
        d.xpath('//android.widget.ListView/android.view.View[6]/android.view.View[4]').click()
        time.sleep(2)

    def sub_Proanwser(): # 专项答题
        d.swipe(0.35, 0.85, 0.85, 0.25)
        d.xpath('//android.widget.ListView/android.view.View[7]/android.view.View[4]').click()
        time.sleep(2)
        d(text="").click()

    def sub_Order():
        d.swipe(0.35, 0.85, 0.85, 0.25)
        d.swipe(0.35, 0.85, 0.85, 0.25)
        d.xpath('//android.widget.ListView/android.view.View[12]/android.view.View[4]').click()
        time.sleep(2)

    def sub_LocalP():
        d.swipe(0.35, 0.85, 0.85, 0.25)
        time.sleep(1)
        d.swipe(0.35, 0.95, 0.85, 0.15)
        d.xpath('//android.widget.ListView/android.view.View[14]/android.view.View[4]').click()
        time.sleep(2)

    def sub_Share():
        d.swipe(0.35, 0.85, 0.85, 0.15)
        time.sleep(1)
        d.swipe(0.35, 0.95, 0.85, 0.15)
        d.xpath('//android.widget.ListView/android.view.View[12]/android.view.View[4]').click()
        time.sleep(2)
    def test_Readdocs():
        studyTest.enter_Score()
        studyTest.sub_Read()
    def test_Readvideo():
        studyTest.enter_Score()
        studyTest.sub_Watch()
    def test_Hearstudy():
        studyTest.enter_Score()
        studyTest.sub_Study()




if __name__ == '__main__':
    i = 1
    for i in range(100):
        studyTest.test_Readdocs()
        studyTest.test_Readvideo()
        studyTest.test_Hearstudy()
        d.app_stop("cn.xuexi.android")
        time.sleep(2)
        i += 1
        print(">>>>>>>>>>第 %d 次测试完成"%i)
        d.app_start("cn.xuexi.android")
        time.sleep(2)


