from publick import dellExcel,DellFirefox,dellDict
from selenium.webdriver.support.select import Select
import json


if __name__=="__main__":
    dr = DellFirefox.dell_firefox().open_firefix()
    number = len(dellExcel.ExcelDell().ReadCase())
    for i in range(0,number):
        #判断用例是否执行
        casedone = dellExcel.ExcelDell().getCase('是否执行',i)
        #提取参数
        caseParameter = dellDict.DictDELL().dell()
        #提取会退元素位置
        back_element = (dellExcel.ExcelDell().getCase('回退元素', 0)).split(',')
        #读取检查点
        check_element = dellExcel.ExcelDell().getCase('检查点',i)
        if casedone == '是':
            for j in range(0,len(caseParameter)):
                if caseParameter[j][1] == 'send':
                    dr.find_element_by_xpath(caseParameter[j][0]).send_keys(caseParameter[j][2])

                if caseParameter[j][1] == 'click':
                    dr.find_element_by_xpath(caseParameter[j][0]).click()
                if caseParameter[j][1] == 'iframe':
                    ifreame = dr.find_element_by_xpath(caseParameter[j][0])
                    dr.switch_to.frame(ifreame)
                if caseParameter[j][1] == 'alret':
                    dr.find_element_by_xpath(caseParameter[j][0]).click()
                    dr.switch_to.alert.accept()
                if caseParameter[j][1] == 'select':
                    xiala = dr.find_element_by_xpath(caseParameter[j][0])
                    number = len(xiala.find_elements_by_tag_name('option'))
                    for i in range(0,number-1):
                        Select(xiala).select_by_index(1)
            try:
                result = dr.find_element_by_xpath(check_element).is_displayed()
                if result == True:
                    dellExcel.ExcelDell().writeExcel('pass','是否通过',i)
                    print('第', i, '条用例执行成功')
                else:
                    dr.get_screenshot_as_file(r"F:\pythonworkplace\test\NewUITest\picture\用例%s.png"%i)
                    dellExcel.ExcelDell().writeExcel('fail','是否通过',i)
                    print('第',i,'条用例执行失败')
            except :
                dellExcel.ExcelDell().writeExcel('检查点可能错啦', '备注', i)
            try:
                for i in back_element:
                    dr.find_element_by_xpath(i).click()
            except:
                print("前面的事件没有完成")
        else:
            print('用例编号：',i+1,'\t','不执行')
    DellFirefox.dell_firefox().close_firefox()
