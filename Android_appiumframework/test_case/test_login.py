# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""

import unittest
import logging
from public.myunit import StartEnd
from businessView.loginView import LoginView

class LoginTest(StartEnd):
    #读取csv文件的数据
    scv_file = '../data/account.csv'

    # @unittest.skip('test_login_2017')
    def test_login_2017(self):
        '''
        封装测试用例,并读取csv文件第一行数据
        username,password,email 参数化
        :return:
        '''
        logging.info("=========test_login_2017============")
        l=LoginView(self.driver)
        #读取csv文件第一行的数据
        data = l.get_csv_data(self.scv_file,1)
        #username 信息为data[0],password信息为data[1]
        l.login_action(data[0],data[1])
        #追加断言，确认是否登录成功
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('test_login_2018')
    def test_login_2018(self):
        '''
        封装测试用例,并读取csv文件第一行数据
        username,password,email 参数化
        :return:
        '''
        logging.info("=========test_login_2018============")
        l=LoginView(self.driver)
        #读取csv文件第一行的数据
        data = l.get_csv_data(self.scv_file,2)
        #username 信息为data[0],password信息为data[1]
        l.login_action(data[0],data[1])
        #追加断言，确认是否登录成功
        self.assertTrue(l.check_loginStatus())

    @unittest.skip('test_login_error')
    def test_login_error(self):
        '''
        封装测试用例,并读取csv文件第三行数据
        username,password,email 参数化
        :return:
        '''
        logging.info("=========test_login_error============")
        l=LoginView(self.driver)
        #读取csv文件第一行的数据
        data = l.get_csv_data(self.scv_file,3)
        #username 信息为data[0],password信息为data[1]
        l.login_action(data[0],data[1])
        #追加断言，确认是否登录成功
        self.assertTrue(l.check_loginStatus(), msg='login fail!')

if __name__ == '__main__':
    unittest.main()

