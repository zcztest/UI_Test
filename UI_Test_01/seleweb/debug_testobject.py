import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep


def select_element(eles, val):
    for ele in eles:
        if ele.text == val:
            ele.click()
            break

def highlight_element(element):
    driver.execute_script("element = arguments[0];" +
                               "original_style = element.getAttribute('style');" +
                               "element.setAttribute('style', original_style + \";" +
                               "background: #1874cd; border: 1px solid red;\");" +
                               "setTimeout(function(){element.setAttribute('style', original_style);}, 1000);",
                               element)

# Chrome --remote-debugging-port=58999 --user-data-dir="/Users/zhaowei/Documents/selenium/AutomationProfile"

# 使用现有浏览器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:58999")
chrome_driver = '/Users/zhaowei/Documents/AutoTestPOM/web/drivers/chromedriver'
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)

# aaa = len(driver.find_elements_by_class_name('ant-select-dropdown-menu-item'))
# aaa = driver.find_elements_by_class_name('ant-btn-primary')
# highlight_element(aaa[1])
# # driver.find_element_by_xpath('//*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[2]/div').click()
#
# table_fixed = driver.find_element_by_class_name('ant-table-body').find_element_by_class_name('ant-table-fixed')
#
# eles_tr = table_fixed.find_elements_by_tag_name('tr')
# cls_name = eles_tr[0].get_attribute('class')
#
# table_fixed_right = driver.find_element_by_class_name('ant-table-body-outer').find_element_by_class_name('ant-table-fixed')
# cols_count = table_fixed_right.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')
#
# cols_count = len(cols_count)
#
# for row in range(0, len(eles_tr)):
#     eles_td = eles_tr[row].find_elements_by_tag_name('td')
#     if eles_td[1].text == 'customer001':
#         # 检查点
#         # 删除
#         ele = table_fixed_right.find_elements_by_tag_name('tr')[row].find_elements_by_tag_name('td')[0]
#         highlight_element(ele)
#         sleep(1)
#         ActionChains(driver).move_to_element(ele).perform()
#         elelis = driver.find_elements_by_class_name('ant-dropdown-menu-item')
#         elelis_count = len(elelis)
#         elelis[-1].click()
#
#         eles_btn = driver.find_elements_by_class_name('ant-btn-primary')
#         len(eles_btn)
#         eles_btn[1].click()


# 新增
# driver.find_element_by_xpath('//*[@id="main-wrap"]/div/div[2]/div[1]/div[1]/div[2]/a[2]/button').click()
sleep(2)

driver.find_element_by_xpath('//*[@id="main-wrap"]/div/div[2]/div[3]/div/button[2]').click()

sleep(1)

# 确认弹框/html/body/div[6]/div/div[2]/div/div[1]/div/div/div[2]/button[2]
# 确认弹框/html/body/div[7]/div/div[2]/div/div[1]/div/div/div[2]/button[2]
driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[1]/div/div/div[2]/button[2]').click()

driver.find_element_by_id('contactor').send_keys('aaaaaa')

driver.find_element_by_xpath('//*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div/div').click()
sleep(1)

cang_list = driver.find_elements_by_class_name('ant-select-dropdown-menu-item')
select_element(cang_list, '默认仓')

# for cang in cang_list:
#     if cang.text == '默认仓':
#         cang.click()
#         break
str_bumen = '科技部-研发部'
driver.find_element_by_xpath('//*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div[1]/div/div[2]').click()

sleep(1)

gen_list = driver.find_elements_by_class_name('ant-select-tree-title')

select_element(gen_list, str_bumen.split('-')[0])
#
# for gen_ele in gen_list:
#     if gen_ele.text == str_bumen.split('-')[0]:
#         gen_ele.click()
#         break
#
zi_list = driver.find_elements_by_class_name('ant-select-tree-title')
select_element(zi_list, str_bumen.split('-')[1])

# for zi_ele in zi_list:
#     if zi_ele.text == str_bumen.split('-')[1]:
#         zi_ele.click()
#         break




# driver = webdriver.Chrome('/Users/zhaowei/Documents/AutoTestPOM/web/drivers/chromedriver')
# driver.get('https://sso.dinghuo123.com/login')
# driver.find_element_by_id('username').send_keys('18018696469')
# driver.find_element_by_id('password').send_keys('519219')


