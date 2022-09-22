from selenium import webdriver
from time import sleep
from config import conf

class dell_firefox():
    def open_firefix(self):
        global dr
        dr = webdriver.Firefox()
        dr.implicitly_wait(15)
        dr.get(conf.conf().url)
        return dr

    def close_firefox(self):
        dr.close()