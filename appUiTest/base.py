#!python3.7
# -*- coding: utf-8 -*-

__author__ = 'haiertamendie'
__data__ = "2019-11-15 19-56"

import base64

"""
界面元素基础操作
"""
import uiautomator2 as u2
import datetime
import os
import time
from unittest import TestCase


class Action:
    def __init__(self,d):
        self.device = d
        time.sleep(2)
        self.device.screen_on()
        self.device.implicitly_wait(30)

    def connect_wifi(self, ip):
        """
        通过WiFi连接设备：ip根据情况自己修改
        :param ip:
        :return:
        """
        return u2.connect_wifi(ip)

    def connect_usb(self):
        """
        通过USB连接设备
        :return:
        """
        return u2.connect_usb()

    def healthcheck(self):
        """
        检查并维持设备端守护进程处于运行状态
        :return:
        """
        self.device.healthcheck()

    def app_start(self, package_name,
                  activity=None,
                  extras={},
                  wait=True,
                  stop=True,
                  unlock=False,
                  launch_timeout=30,
                  use_monkey=False):
        """
        启动APP
        :param package_name:
        :param activity:
        :param extras:
        :param wait:
        :param stop:
        :param unlock:
        :param launch_timeout:
        :param use_monkey:
        :return:
        """
        self.device.app_start(package_name, activity=activity, extras=extras, wait=wait, stop=stop, unlock=unlock,
                              launch_timeout=launch_timeout, use_monkey=use_monkey)

    def app_stop(self, package_name):
        """
        关闭app
        :param package_name: 应用包名
        :return:
        """
        self.device.app_stop(package_name)

    def app_clear(self, package_name):
        """
        清除app缓存
        :param package_name: 应用包名
        :return:
        """
        self.device.app_clear(package_name)

    def get_app_info(self, package_name):
        """
        获取应用信息
        :param package_name: 应用包名
        :return:
        """
        return self.device.app_info(package_name)

    def app_stop_all(self, excludes=[]):
        """
        关闭excludes中的所有应用
        :param excludes: 应用包名集合
        :return:
        """
        self.device.app_stop_all(excludes)

    def get_app_list_running(self):
        """
        获取已启动的应用
        :return:
        """
        return self.device.app_list_running()

    def wait_activity(self, activity, timeout=10):
        """
        等待activity加载出来
        :param activity:
        :param timeout:
        :return:
        """
        self.wait_activity(activity=activity, timeout=timeout)

    def app_wait(self, package_name, timeout=20.0,
                 front=False):
        """
        等待应用启动
        :param package_name: 应用包名
        :param timeout:  超时时间
        :param front:
        :return:
        """
        return self.device.app_wait(package_name, timeout=timeout, front=front)

    def app_insatll(self, url, installing_callback=None, server=None):
        """
        安装应用
        :param url: 设备名字或者地址
        :param installing_callback:
        :param server:
        :return:
        """
        self.device.app_install(url, installing_callback=installing_callback, server=server)

    def app_uninstall(self, package_name):
        """
        卸载应用
        :param package_name: 应用包名
        :return:
        """
        self.device.app_uninstall(package_name)

    def app_uninstall_all(self, excludes=[], verbose=False):
        """
        卸载多个应用
        :param excludes: 应用包名集合
        :param verbose:
        :return:
        """
        self.device.app_uninstall_all(excludes=excludes, verbose=verbose)

    def get_element_xpath(self, xpath):
        """
        根绝xpath路径获取元素
        :param xpath: xpath路径
        :return:
        """
        return self.device.xpath(xpath)

    def get_elements(self, childCount=None, **kwargs):
        """获取元素
        @:param childCount 子元素数量
        """
        ele = self.device(**kwargs)
        if childCount:
            eles = []
            for i in ele:
                if i.info.get("childCount") == childCount:
                    eles.append(i)
            return eles
        else:
            return ele

    def get_count(self, **kwargs):
        """
        获取元素个数
        :param kwargs: 元素定位
        :return:
        """
        return self.device(**kwargs).count

    def get_child_element(self, element, childCount=None, **kwargs):
        """
        获取子对象
        :param element: 元素对象
        :param childCount:
        :param kwargs:
        :return:
        """
        ele = element.child(**kwargs)
        if childCount == None or len(ele) == 1:
            return ele
        else:
            eles = []
            for i in ele:
                if i.info.get("childCount") == childCount:
                    eles.append(i)
            return eles

    def get_left_element(self, element, **kwargs):
        """
        获取element左侧元素
        :param element: 元素对象
        :param kwargs:
        :return:
        """
        return element.left(**kwargs)

    def get_right_element(self, element, **kwargs):
        """获取element右侧元素"""
        return element.right(**kwargs)

    def get_up_element(self, element, **kwargs):
        """
        获取element上方元素
        :param element: 元素对象
        :param kwargs:
        :return:
        """
        return element.up(**kwargs)

    def get_down_element(self, element, **kwargs):
        """
        获取element下方元素"
        :param element: 元素对象
        :param kwargs: 
        :return: 
        """""
        return element.down(**kwargs)

    def get_sibling_elements(self, index=0, **kwargs):
        """
        获取兄弟元素
        :param index: 第几个兄弟，默认为全部
        :param kwargs: 元素定位(唯一)
        :return:
        """
        self.wait(**kwargs)
        if index == 0:
            return self.device(**kwargs).sibling()
        return self.device(**kwargs).sibling()[index]

    def get_sibling_elements_by_element(self, element, **kwargs):
        """
        获取兄弟元素
        :param element: 元素
        :param kwargs: 兄弟元素定位(唯一)
        :return:
        """
        return element.sibling(**kwargs)

    def click(self, **kwargs):
        """
        点击元素
        :param index: 索引值
        :param kwargs: 元素定位()
        :return:
        """
        self.device(**kwargs).click()

    def click_xpath(self, xpath, timeout=5):
        """
        根据xpath路径点击元素
        :param xpath:
        :param timeout:
        :return:
        """
        self.device.xpath(xpath).click(timeout=timeout)

    def click_element(self, element):
        """
        点击元素
        :param element: 元素对象
        :return:
        """
        element.click()

    def click_child_element(self, element, **kwargs):
        """
        点击element的子元素
        :param element: 元素对象
        :param kwargs: 子元素定位信息
        :return:
        """
        ele = self.get_child_element(element, **kwargs)[0]
        self.click_element(ele)

    def click_by_point(self, x, y):
        """
        点击坐标点
        :param x: 横坐标
        :param y: 纵坐标
        :return:
        """
        self.device.click(x, y)

    def double_click(self, x, y, duration=0.1):
        """双击
        @:param duration 间隔
        """
        self.device.double_click(x, y, duration=duration)

    def long_click(self, duration=10, timeout=10, **kwargs):
        """
        长按指定的对象
        :param duration: 持续时间
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        self.device(**kwargs).long_click(duration=duration, timeout=timeout)

    def long_click_by_element(self, element, duration=10, timeout=10):
        """
        长按
        :param element: 元素对象
        :param duration: 持续时间
        :param timeout: 超时时间
        :return:
        """
        element.long_click(duration=duration, timeout=timeout)

    def long_click_by_point(self, x, y):
        """
        长按坐标点
        :param x: 横坐标
        :param y: 纵坐标
        :return:
        """
        self.device.long_click(x, y)

    def get_element_info(self, **kwargs):
        """
        获取元素信息
        :param kwargs: 元素定位
        :return:
        """
        return self.device(**kwargs).info

    def get_info_by_element(self, element):
        """
        获取元素信息
        :param element: 元素对象
        :return:
        """
        return element.info

    def input_text(self, content, **kwargs):
        """
        输入文本
        :param content: 文本内容
        :param kwargs: 元素定位信息
        :return:
        """
        self.wait(**kwargs)
        self.device(**kwargs).set_text(content)
        self.press("enter")

    def input_text_xpath(self, content, xpath):
        """
        输入文本
        :param content: 文本内容
        :param xpath: 元素xpath定位信息
        :return:
        """
        self.wait_xpath(xpath)
        element = self.get_element_xpath(xpath)
        self.click_element(element)
        element.set_text(content)

    def input_text_by_element(self, element, content):
        """输入"""
        self.click_element(element)
        element.set_text(content)
        self.press("enter")

    def clear_text(self, **kwargs):
        """
        清除输入框数据
        :param kwargs: 输入文本框定位
        :return:
        """
        self.device(**kwargs).clear_text()

    def clear_text_by_element(self, element):
        """清除数据"""
        element.clear_text()

    def click0(self, **kwargs):
        """点击UI对象中心位置"""
        self.device(**kwargs).click0()

    def click0_by_element(self, element):
        """点击UI对象中心位置"""
        element.click0()

    def click_bottomright(self, **kwargs):
        """点击UI对象右下角"""
        self.device(**kwargs).click.bottomright()

    def click_bottomright_by_element(self, element):
        """点击UI对象右下角"""
        element.click.bottomright()

    def click_topleft(self, **kwargs):
        """点击UI对象左上角"""
        self.device(**kwargs).click.topleft()

    def click_topleft_by_element(self, element):
        """点击UI对象左上角"""
        element.click.topleft()

    def long_click_bottomright(self, **kwargs):
        """长按UI对象右下角"""
        self.device(**kwargs).long_click.bottomright()

    def long_click_bottomright_by_element(self, element):
        """长按UI对象右下角"""
        element.long_click.bottomright()

    def long_click_topleft(self, **kwargs):
        """长按UI对象左上角"""
        self.device(**kwargs).long_click.topleft()

    def long_click_topleft_by_element(self, element):
        """长按UI对象左上角"""
        element.long_click.topleft()

    def drag_to_point(self, element, x, y, duration=1):
        """拖动指定对象到x,y位置，0.5s完成"""
        element.drag.to(x, y, duration=duration)

    def drag_to_element(self, element, **kwargs):
        """拖拽某一UI对象到另外一个UI对象（中心）"""
        element.drag.to(**kwargs, steps=100)

    def refresh(self):
        """刷新页面"""
        wedith = self.get_window_size()[0]
        height = self.get_window_size()[1]
        self.swipe(wedith / 2, height * 1 / 4, wedith / 2, height * 5 / 6)

    def swipe_right(self, **kwargs):
        """从UI对象的中心滑动到UI对象的右边缘"""
        self.device(**kwargs).swipe.right()

    def swipe_right_by_element(self, element):
        """从UI对象的中心滑动到UI对象的右边缘"""
        element.swipe.right()

    def swipe_up(self, **kwargs):
        """从UI对象的中心滑动到UI对象的上边缘"""
        self.device(**kwargs).swipe.up()

    def swipe_up_screen(self, scre=1, steps=100):
        """
        向上滑动屏幕，默认为一屏
        :param scre: 滑动比例
        :return:
        """
        device_info = self.get_device_info()
        height = device_info.get("displayHeight")
        width = device_info.get("displayWidth")
        self.device.swipe(width / 2, height * 8 * scre / 9, width / 2, height / 9, steps=steps)

    def swipe_down_screen(self, scre=1, steps=100):
        """
        向下滑动屏幕，默认为一屏
        :param scre: 滑动比例
        :return:
        """
        device_info = self.get_device_info()
        height = device_info.get("displayHeight")
        width = device_info.get("displayWidth")
        self.device.swipe(width / 2, height / 9, width / 2, height * 8 * scre / 9, steps=steps)

    def swipe_up_by_element(self, element):
        """从UI对象的中心滑动到UI对象的上边缘"""
        element.swipe.up()

    def swipe_left(self, **kwargs):
        """从UI对象的中心滑动到UI对象的左边缘"""
        self.device(**kwargs).swipe.left()

    def swipe_left_by_element(self, element):
        """从UI对象的中心滑动到UI对象的左边缘"""
        element.swipe.left()

    def swipe_down(self, **kwargs):
        """从UI对象的中心滑动到UI对象的下边缘"""
        self.device(**kwargs).swipe.down()

    def swipe_down_by_element(self, element):
        """从UI对象的中心滑动到UI对象的下边缘"""
        element.swipe.down()

    def pinch_In(self, **kwargs):
        """从边缘到中心"""
        self.device(**kwargs).pinch.In(percent=100, steps=10)

    def pinch_In_by_element(self, element):
        """从边缘到中心"""
        element.pinch.In(percent=100, steps=10)

    def pinch_Out(self, percent=33, steps=100):
        """从屏幕外侧向中心滑动，percent为左右起始位置占两边的比例"""
        self.device().pinch_out(percent=percent, steps=steps)

    def pinch_Out_element(self, element, percent=33, steps=100):
        """从中心到边缘"""
        element.pinch_out(percent=percent, steps=steps)

    def set_implicitly_wait(self, timeout=30):
        """设置全局最长等待时间"""
        return self.device.implicitly_wait(timeout)

    def click_wait(self, timeout=10, **kwargs):
        """
        当timeout s内对象出现就点击
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        self.device(**kwargs).click_exists(timeout)

    def click_wait_xpath(self, xpath, timeout=10):
        """
        当timeout s内对象出现就点击
        :param xpath: xpath定位
        :param timeout: 超时时间
        :return:
        """
        self.wait_xpath(xpath, timeout=timeout)
        self.click_xpath(xpath)

    def click_gone(self, maxretry=10, interval=1.0, **kwargs):
        """
        点击并轮询对象直到消失
        :param maxretry: 最多点击次数
        :param interval: 轮询时间间隔
        :param kwargs: 元素定位
        :return:
        """
        self.device(**kwargs).click_gone(maxretry=maxretry, interval=interval)

    def wait_exists_by_element(self, element, timeout=10):
        """
        等待UI对象出现
        :param element: 元素对象
        :param timeout: 超时时间
        :return:
        """
        return element.exists(timeout=timeout)

    def wait(self, timeout=10, **kwargs):
        """
        等待
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        return self.device(**kwargs).wait(timeout)

    def wait_should_be_contains(self, timeout=10, **kwargs):
        """
        等待包含元素，超时抛出错误
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        self.device(**kwargs).must_wait(exists=True, timeout=timeout)

    def wait_xpath(self, xpath, timeout=10):
        """
        等待
        :param xpath: xpath路径
        :param timeout: 超时时间
        :return:
        """
        return self.device.xpath(xpath).wait(timeout=timeout)

    def wait_gone(self, timeout=10, **kwargs):
        """
        等待UI对象消失
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        return self.device(**kwargs).wait_gone(timeout=timeout)

    def wait_gone_xpath(self, xpath, timeout=10):
        """
        等待UI对象消失
        :param xpath: xpath定位
        :param timeout: 超时时间
        :return:
        """
        return self.device.xpath(xpath).wait_gone(timeout=timeout)

    def wait_gone_by_element(self, element, timeout=3000):
        """
        等待UI对象消失
        :param element: 元素对象
        :param timeout: 超时时间
        :return:
        """
        return element.wait_gone(timeout=timeout)

    def scroll_up(self, steps=10):
        """
        向上滑动
        :param steps: 步长
        :return:
        """
        self.device(scrollable=True).scroll(steps=steps)

    def scroll_up_to_content_element(self, max_scroll_num=15, **kwargs):
        """
        向上滑动直到某个元素出现
        :param max_scroll_num: 最大滑动次数
        :param kwargs: 元素定位
        :return:
        """
        self.sleep()
        num = 0
        while num < max_scroll_num:
            if self.exists(timeout=0.5, **kwargs):
                return True
            else:
                try:
                    self.swipe_up_screen(0.5, steps=20)
                except:
                    return False
            num = num + 1
            self.sleep(0.2)
        if num == max_scroll_num:
            return False
        else:
            return True

    def vert_backward(self):
        """
        向下滑动
        :return:
        """
        self.device(scrollable=True).scroll.vert.backward()

    def vert_backward_to_content_element(self, **kwargs):
        """
        向下滑动直到某个元素出现
        :param kwargs: 元素定位
        :return:
        """
        while True:
            if self.exists(**kwargs):
                break
            else:
                self.device(scrollable=True).scroll.vert.backward(steps=100)

    def scroll_to_beginning(self, steps=10, max_swipes=1000):
        """
        向左滑动到开始位置
        :param steps: 步长
        :param max_swipes:
        :return:
        """
        self.device(scrollable=True).scroll.horiz.toBeginning(steps=steps, max_swipes=max_swipes)

    def horiz_forward(self, steps=10):
        """
        向右滑动"
        :param steps: 步长
        :return: 
        """""
        self.device(scrollable=True).scroll.horiz.forward(steps=steps)

    def scroll_to_end(self, steps=10):
        """
        向结束方向滑动
        :param steps: 步长
        :return:
        """
        self.device(scrollable=True).scroll.toEnd(steps=steps)

    def scroll_to(self, **kwargs):
        """
        向前滚动到指定UI位置
        :param kwargs: 元素定位
        :return:
        """
        self.device(scrollable=True).scroll.to(**kwargs)

    def get_device_info(self):
        """
        获取设备信息
        :return:
        """
        return self.device.info

    def get_window_size(self):
        """
        获取窗口大小
        :return:
        """
        return self.device.window_size()

    def get_device_height(self):
        """
        获取设备的高度
        :return:
        """
        return self.device.info.get("displayHeight")

    def get_device_width(self):
        """
        获取设备的宽度
        :return:
        """
        return self.device.info.get("displayWidth")

    def screen_on(self):
        """
        打开屏幕
        :return:
        """
        self.device.screen.on()

    def screen_off(self):
        """
        关闭屏幕
        :return:
        """
        self.device.screen.off()

    def wakeup(self):
        """
        唤醒设备
        :return:
        """
        self.device.wakeup()

    def device_sleep(self):
        """
        关闭设备
        :return:
        """
        self.device.sleep()

    def sleep(self, seconds=2):
        """
        强制等待时间
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def press_home(self):
        """
        按home键
        :return:
        """
        self.device.press("home")

    def press_back(self):
        """
        按返回键
        :return:
        """
        self.device.press("back")

    def press(self, key):
        """
        按下键码
        :param key: 键码值
        :return:
        """
        self.device.press(key)

    def press_enter(self):
        """
        按下回车键
        :return:
        """
        self.device.press.enter()

    def swipe(self, sx, sy, ex, ey, steps=10):
        """
        从sx，sy坐标滑动至ex，ey坐标
        :param sx: 起点横坐标
        :param sy: 起点纵坐标
        :param ex: 终点横坐标
        :param ey: 终点纵坐标
        :param steps:
        :return:
        """
        self.device.swipe(sx, sy, ex, ey, steps=steps)

    def gesture(self, a, b, c, d, a1, b1, c1, d1, steps=100):
        """
        双指从(a,b)，(c,d)滑动(a1,b1)，(c1,d1)，步长100
        :param a:
        :param b:
        :param c:
        :param d:
        :param a1:
        :param b1:
        :param c1:
        :param d1:
        :param steps:
        :return:
        """
        self.device.gesture((a, b), (c, d), (a1, b1), (c1, d1), steps=steps)

    def drag(self, sx, sy, ex, ey, steps=10):
        """
        从sx，sy坐标拖动至ex，ey坐标
        :param sx: 起点横坐标
        :param sy: 起点纵坐标
        :param ex: 终点横坐标
        :param ey: 终点纵坐标
        :param steps: 步长
        :return:
        """
        self.device.drag(sx, sy, ex, ey, steps=steps)

    def screenshot(self, name=""):
        """
        截屏
        :param name: 图片名字
        :return:
        """
        if name != "":
            path = os.path.join(self.path_screenshot, name + ".png")
        else:
            path = os.path.join(self.path_screenshot, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M') + ".png")
        self.device.screenshot(path)

    def get_screenshot_as_base64(self):
        """
        截屏并转换成base64
        :return:
        """
        content = self.device.screenshot(format="raw")
        base64_data = base64.b64encode(content)
        # base64.b64decode(base64data)
        return str(base64_data, "utf-8")

    def dump(self, path):
        """
        将当前屏幕结构保存在本机,xml文件
        :param path: 保存路径
        :return:
        """
        self.device.dump_hierarchy(path)

    def notification(self):
        """
        打开通知消息
        :return:
        """
        self.device.notification()

    def open_quick_settings(self):
        """
        打开快捷设置栏
        :return:
        """
        self.device.open.quick_settings()

    def register_watcher_click(self, name, **kwargs):
        """
        创建并运行监听器
        :param name:
        :param kwargs:
        :return:
        """
        watcher = self.device.watcher(name).when(**kwargs).click(**kwargs)
        self.watchers_run()
        return watcher

    def remove_watcher(self, name):
        """
        移除监听器
        :param name: 监听器名字
        :return:
        """
        self.device.watcher(name).remove()

    def watchers(self):
        """
        获取所有监听器
        :return:
        """
        return self.device.watcher()

    def watchers_triggered(self, name):
        """
        获取所有已触发监听器
        :param name:
        :return:
        """
        return self.device.watcher(name).triggered

    def watchers_reset(self):
        """
        重置所有已触发的监视器
        :return:
        """
        self.device.watchers.reset()

    def watchers_run(self):
        """
        运行所有已注册的监听器
        :return:
        """
        self.device.watchers.run()

    def exists(self, timeout=10, **kwargs):
        """
        判断元素是否存在
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        return self.device(**kwargs).exists(timeout=timeout)

    def exists_xpath(self, xpath):
        """
        判断元素是否存在
        :param xpath: xpath路径
        :return:
        """
        return self.device.xpath(xpath).exists

    def wait_not_exists(self, timeout=15, **kwargs):
        """
        等待元素消失
        :param timeout: 超时时间
        :param kwargs: 元素定位
        :return:
        """
        num = 1
        while num <= timeout * 2:
            if self.exists(**kwargs):
                self.sleep(0.5)
                num = num + 1
            else:
                return True
        return False

    def exists_by_element(self, element, timeout=10):
        """
        判断元素是否存在
        :param element: 元素对象
        :param timeout: 超时时间
        :return:
        """
        return element.exists(timeout=timeout)

    def disable_popups(self, disable=True):
        """弹出窗口
        @:param disable True:自动跳过弹出窗口，False:禁用自动跳过弹出窗口
        """
        self.device.disable_popups(disable)

    def get_toast(self, wait_timeout=15,
                  cache_timeout=8,
                  default=None):
        """
        获取toast提示
        :param wait_timeout: 超时时间
        :param cache_timeout: 从现在开始多少时间以内
        :param default: 超时提示
        :return:
        """
        toast = self.device.toast.get_message(wait_timeout=wait_timeout,
                                              cache_timeout=cache_timeout,
                                              default=default)
        if toast:
            self.reset_toast()
        return toast

    def reset_toast(self):
        """
        清除设备toast提示
        :return:
        """
        self.device.toast.reset()

