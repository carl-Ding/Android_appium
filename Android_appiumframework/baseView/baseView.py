# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-28
"""

class BaseView(object):
    '''
    封装一些基类
    '''
    def __init__(self,driver):
        self.driver = driver

    #元素定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    #一组元素定位
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    #获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    #滑动
    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)  #duration 滑动持续时间
