# -*- coding: utf-8 -*-
import os
import platform
import time

# 框架根目录
frame_path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])

# 当前操作系统
OS = platform.system()

# 当前时间
now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

browser = 'chrome'

# 全局配置
if OS == "Darwin":
    data_file = frame_path + '/data/test_data.xlsx'
    logs_path = frame_path + '/logs/' + today + '/'
    pictures_path = frame_path + '/pictures/' + today + '/'
    report_path = frame_path + '/reports/' + today + '/'
    driver_file = frame_path + "/config/chromedriver"
    test_objects = frame_path + "/src/objects/objects.yaml"
    testcase_path = frame_path + '/src/testcase'
else:
    data_file = frame_path + '\\data\\test_data.xlsx'
    logs_path = frame_path + '\\logs\\' + today + '\\'
    pictures_path = frame_path + '\\pictures\\' + today + '\\'
    report_path = frame_path + '\\reports\\' + today + '\\'
    driver_file = frame_path + "\\config\\chromedriver.exe"
    test_objects = frame_path + "\\src\\objects\\objects.yaml"
    testcase_path = frame_path + '\\src\\testcase'

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

logs_file = logs_path + time.strftime("%Y-%m-%d_%H", time.localtime(time.time())) + '.log'

if not os.path.exists(report_path):
    os.mkdir(report_path)

report_file = report_path + now + '.html'

# 测试报告参数
report_title = '自动化测试报告-' + now
description = '测试集执行情况如下'  # 在测试报告隐藏了，暂时废弃了
tester = "EvanZou"  # 测试人员
