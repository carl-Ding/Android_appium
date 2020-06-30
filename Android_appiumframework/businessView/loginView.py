# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""

import logging
from public.common_func import Common,By
from public.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):

    #登录界面元素设置
    username_input = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_input = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_btn = (By.ID,'com.tal.kaoyan:id/login_login_btn')

    #个人中心下线警告提醒确定按钮
    commitBtn = (By.ID,'com.tal.kaoyan:id/tip_commit')

    #个人中心元素
    myself_btn= (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_name = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    #退出相关设置
    setting_btn = (By.ID,'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logout_btn = (By.ID,'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')



    def login_action(self,username,password):
        '''
        页面登录操作：
        输入用户名
        输入密码信息
        点击登录按钮
        '''
        #如果有更新，或者skip按钮，则直接点击
        self.check_upgradeBtn()
        self.check_skipBtn()
        # 登录
        logging.info('=======login_action=========')
        #在用户名输入框输入信息
        logging.info('username is %s' %username)
        self.driver.find_element(*self.username_input).send_keys(username)
        #在密码输入框输入信息
        logging.info('password is %s' %password)
        self.driver.find_element(*self.password_input).send_keys(password)
        #点击登录按钮
        logging.info('click login Button')
        self.driver.find_element(*self.login_btn).click()
        logging.info("login Finished !")

    def check_account_alert(self):
        '''
        检测账户登录后是否有账户下线提示
        :return:
        '''
        logging.info('=======check_account_alert=======')
        try:
            element = self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('click commitBtn')
            element.click()

    def check_loginStatus(self):
        '''
        检测登录状态，即验证是否登录成功状态
        :return:
        '''
        logging.info('======check_loginStatus=====')
        #如果有广告界面，直接点击关闭按钮
        self.check_market_ad()
        #如果有账号下线提醒，直接点击确定按钮
        self.check_account_alert()

        #使用try...except，在登录后页面获取任意一个元素，如果获取到，则表示登录成功，否则，登录失败
        try:
            self.driver.find_element(*self.myself_btn).click()
            self.driver.find_element(*self.usercenter_name)
        except NoSuchElementException:
            logging.error('login Fail !')
            self.getScreenShot("login Fail")
            return False
        else:
            logging.info("login success !")
            #退出登录
            self.logout_action()
            return True

    def logout_action(self):
        '''
        退出登录
        :return:
        '''
        logging.info('=======logout_action========')
        self.driver.find_element(*self.setting_btn).click()
        self.driver.find_element(*self.logout_btn).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
    driver = appium_desired()
    l=LoginView(driver)
    l.login_action('自学网2018','zxw2018')
    l.check_loginStatus()









