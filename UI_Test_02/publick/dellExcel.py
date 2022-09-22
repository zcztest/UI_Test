import csv
from config import conf
import pandas as pd

class ExcelDell():


    """读取测试用例"""
    def ReadCase(self):
        casedata = pd.read_excel(conf.conf().casePath, sheet_name='Sheet1', encoding='gbk')
        return casedata

    """提取用例参数"""
    def getCase(self,element_id,Indenx):
        """

        :param element_id: 列名
        :param Indenx: 第几行
        :return:
        """
        data = ExcelDell().ReadCase()
        pd.options.mode.chained_assignment = None
        caseElement = data[element_id][Indenx]
        return caseElement
    def getlie(self,element_id):
        """

        :param element_id: 列名
        :param Indenx: 第几行
        :return:
        """
        data = ExcelDell().ReadCase()
        pd.options.mode.chained_assignment = None
        caseElement = data[element_id]
        return caseElement

    """修改excel"""
    def writeExcel(self,result,lie,Indenx):
        """

        :param result: 结果
        :param Indenx: 第几行
        """
        data = ExcelDell().ReadCase()
        data[lie][Indenx] = result
        pd.DataFrame(data).to_excel(conf.conf().casePath,sheet_name='Sheet1',index=False, header=True,encoding='gbk')
        #data2 = pd.read_excel(conf.conf().casePath,sheet_name='Sheet1',encoding='gbk')
