# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""

import logging
import random
import unittest
from public.myunit import StartEnd
from businessView.registerView import RegisterView

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('=======test_user_register========')
        #定义变量，调用registerView 对象，传入参数self.driver
        r = RegisterView(self.driver)

        #使用random函数来定义username,password,email
        username = 'carl' + str(random.randint(1000, 9999))
        password = 'abc' + str(random.randint(1000, 9999))
        email = 'qwe' + str(random.randint(1000, 9999)) + '@qq.com'

        #追加断言，来判断，是注册成功还是失败
        self.assertTrue(r.register_action(username,password,email))

if __name__ == '__main__':
    unittest.main()




