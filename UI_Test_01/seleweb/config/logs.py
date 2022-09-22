# -*- coding: utf-8 -*-
import logging
from config.config import logs_file


class Logs(object):
    def __init__(self, class_name):
        self.class_name = class_name
        self.logger = logging.Logger(self.class_name)
        self.logger.setLevel(logging.INFO)
        self.logfile = logging.FileHandler(logs_file, encoding='utf-8')
        self.logfile.setLevel(logging.INFO)
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater = logging.Formatter('[%(asctime)s] - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %('
                                          'message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)
