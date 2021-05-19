# coding:utf-8
from SeleniumbasePO.DataHelp.sqlhelp import getSqlData
from SeleniumbasePO.DataHelp.Data_Rnd import DataRnd
import random


class DataUser():
    @staticmethod
    def email_only(kk=5, ext='@qq.com', number=0):
        while True:
            email = DataRnd.getRndEmail(kk=kk, ext=ext)
            # 去数据库查询是否存在此数据
            sql = "SELECT * FROM `user` u WHERE u.`email`=%s"
            data = getSqlData(sql, email)
            if len(data) == number: return email

    @staticmethod
    def username_only(kk=5, number=0):
        while True:
            username = DataRnd.getRndUser(kk=kk)
            sql = "select * from user u where u.username = %s"
            data = getSqlData(sql, username)
            if len(data) == number: return username
    @staticmethod
    def email_duplicate():
        sql = "SELECT u.id,u.`email`,u.`username` FROM `user` u LIMIT 1;"
        data = getSqlData(sql)
        return data[0][1]
if __name__ == "__main__":
    c = DataUser.email_duplicate()
    print(c)
