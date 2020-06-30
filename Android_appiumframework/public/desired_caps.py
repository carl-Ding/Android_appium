# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-28
"""

'''
driver 配置封装
'''
import  yaml,os
import logging.config
from appium import webdriver

#读取log.conf  文件中的日志配置
CON_LOG = '../config/log.conf'
print(CON_LOG)
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    #打开 并读取caps.yaml文件，这里用with方法
    with open('../config/caps.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file)
    #参数化需要打开运行设备的一些信息
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    #设定文件的根目录地址
    base_path = os.path.dirname(os.path.dirname(__file__))
    #设定app(kaoyan.apk)的路径
    app_path = os.path.join(base_path,'app')
    app_name = os.path.join(app_path,data['appname'])
    desired_caps['app'] = app_name
    #启动app时，清除app里面原有的数据
    desired_caps['noReset'] = data['noReset']
    #使用unicodekeyboard输入法，因为账号可能涉及到中文
    desired_caps['unicodekeyboard'] = data['unicodeKeyboard']
    #重置输入法到初始状态
    desired_caps['resetKeyboard'] =data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    #打印log信息
    logging.info('========start run  app===========')
    #启动
    driver = webdriver.Remote('http://'+str(data['ip']) +':' +str(data['port']) + '/wd/hub',desired_caps)
    # driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    #设置等待时间
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    appium_desired()








