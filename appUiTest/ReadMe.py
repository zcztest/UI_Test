#
#
#
# coding: utf-8
import uiautomator2 as u2
import time
import base

d = u2.connect()  #括号内为adb devices获取的设备号
time.sleep(2)
d.screen_on()
d.implicitly_wait(30)
d.swipe(0.35, 0.95, 0.85, 0.15)
d.app_start("cn.xuexi.android")   #括号内为要启动的APP包名
time.sleep(2)
'''
# 检查元素是否存在
d.exists(description="需要检查的元素")
# 滚动查找某元素
d.exists(scrollable=True, descriptionContains="去看看"):
'''
d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
time.sleep(2)

# d.swipe(0.35,0.85,0.85,0.25)
print(d.exists(text="去看看"))
ch_video = d.exists(scrollable=True,text="去学习")
print(ch_video)
if ch_video == False:
    print(">>>>>>> 未找到该元素，该项已完成 ")
    time.sleep(2)
else:
    d(text="去学习").click()
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

d.app_stop("cn.xuexi.android")