# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""

import unittest

import HTMLTestRunner
import  time
import logging
import sys

#直接运行封装成bat的文件，否则会出现导入错误
path  = 'E:\\Progect\\Android_appiumframework\\'
sys.path.append(path)

'''
这个文件，只执行以下两个步骤：
1.执行用例
2.保存报告
'''
#测试用例文件路径
test_dir = '../test_case'
#测试报告文件路径
report_dir = '../report/'

#获取当前时间
now = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

#生成测试报告文件格式
report_name = report_dir + now +'test_report.html'

#加载测试用例
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

#生成并运行测试用例
with open(report_name,'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=" xxx项目移动APP Test Report", description=" Andriod app Test Report")
    logging.info('start run testcase')
    runner.run(discover)
