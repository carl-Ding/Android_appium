# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-28
"""

'''
公共方法封装
'''
from baseView.baseView import BaseView
from public.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging.config
import os,time,csv

class Common(BaseView):
    #取消升级和跳过引导按钮
    cancel_upgradeBtn = (By.ID,'android:id/button2')
    #跳过按钮
    skipBtn = (By.ID,'com.tal.kaoyan:id/tv_skip')
    #登录/注册后浮窗广告 关闭按钮
    wemedia_cancel= (By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_upgradeBtn(self):
        '''
        追加 try...except...else 语句
        如果没有定位到update button， 则直接执行except
        如果定位到update button，则执行else语句
        :return:
        '''

        logging.info('============check_updateBtn===============')

        try:
            element = self.driver.find_element(*self.cancel_upgradeBtn)
        except NoSuchElementException :
            logging.info('update element is not found!')
        else:
            logging.info('click cancel button')
            element.click()

    def check_skipBtn(self):
        '''
        追加 try...except...else 语句
        如果没有定位到skip button， 则直接执行except
        如果定位到skip button，则执行else语句
        :return:
        '''
        logging.info('============check_skipBtn===============')

        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skip element is not found!')
        else:
            logging.info('click skip button')
            element.click()

    def get_screenSize(self):
        '''
        获取屏幕尺寸
        x：宽
        y：高
        :return:
        '''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x,y

    def swipeLeft(self):
        '''
        向左滑动,
        x1:横坐标起始位置
        y1:纵坐标起始位置
        x2:横坐标终止位置
        1000：持续时间 1000ms
        :return:
        '''
        logging.info('==========swipeLeft==============')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] *0.25)
        self.swipe(x1,y1,x2,y1,1000)

    def getTime(self):
        '''
        获取当前时间，以年-月-日  时_分_秒  形式显示
        :return:
        '''
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now


    def getScreenShot(self,module):
        '''
        设置截图
        :param module:
        :return:
        '''
        time  = self.getTime()
        base_path = os.path.dirname(os.path.dirname(__file__))
        screenshot_path = os.path.join(base_path,'screenshot')
        image_file = os.path.join(screenshot_path,'%s_%s.png' %(module,time))

        # image_file = os.path.dirname(os.path.dirname(__file__)) +'/screenshot/%s_%s.png' %(module,time)

        logging.info('get %s  screenshot ' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        '''
        检测登录或者注册之后的界面浮窗广告
        :return:
        '''
        logging.info('=======check_market_ad=======')
        try:
            element = self.driver.find_element(*self.wemedia_cancel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self,csv_file,line):
        '''
        读取csv文件里的数据
        1.用到的是enumerate()方法
        2.encoding= utf-8-sig:防止读取数据是出现非法字符
           >> 直接写utf-8,打印结果为 ['\ufeffusername\t', 'password']
         utf-8与utf-8-sig两种编码格式的区别：
           >>UTF-8以字节为编码单元，它的字节顺序在所有系统中都是一样的，没有字节序的问题，也因此它实际上并不需要BOM(“ByteOrder Mark”)。
           >>但是UTF-8 with BOM即utf-8-sig需要提供BOM。
        :param csv_file:
        :param line:
        :return:
        '''
        logging.info('=======et_csv_data=========')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            #循环，索引从1开始
            for index,row in enumerate(reader,1):
                if index ==line:
                    return row


if __name__ == '__main__':
    driver  = appium_desired()
    com = Common(driver)
    # com.swipeLeft()
    # com.getScreenShot('startAPP')
    csv_file = '../data/account.csv'
    #获取文件，并读取第一行数据
    data = com.get_csv_data(csv_file,1)
    print(data)
    print(data[0])
    print(data[1])