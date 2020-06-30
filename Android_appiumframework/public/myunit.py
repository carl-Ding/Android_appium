# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""

import unittest
import logging
import time
from public.desired_caps import appium_desired

class  StartEnd(unittest.TestCase):
    '''
    测试用例的执行开始、结束的封装
    '''
    def  setUp(self):
        '''
        测试开始，启动
        :return:
        '''
        logging.info("======setUp========")
        self.driver = appium_desired()

    def tearDown(self):
        '''
        测试结束，关闭
        :return:
        '''
        logging.info('=========tearDown============')
        time.sleep(3)
        self.driver.close_app()


