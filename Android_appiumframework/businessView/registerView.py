# -*- coding: utf-8 -*-
"""
@ auth : carl_DJ
@ time : 2020-6-29
"""
import logging
from public.desired_caps import appium_desired
from public.common_func import Common,By,NoSuchElementException
import random

class RegisterView(Common):
    '''
    注册页面操作
    头像，用户名，密码，邮箱
    学校，专业，
    '''

    #登录界面注册按钮
    register_text = (By.ID,'com.tal.kaoyan:id/login_register_text')

    #注册页面基本元素
    register_username = (By.ID,'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID,'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID,'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID,'com.tal.kaoyan:id/activity_register_register_btn')

    #添加头像
    reg_userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_img = (By.ID,'com.tal.kaoyan:id/item_image')
    save_Btn = (By.ID,'com.tal.kaoyan:id/save')

    #完善信息列表元素
    perfectinfomation_school = (By.ID,'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    #院校信息元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    #专业信息元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    #个人中心元素
    myself_btn= (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_name = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')


    def register_action(self,register_name,register_password,register_email):
        '''
        注册页面，上传头像，输入用户名，密码，邮箱
        :param register_name:
        :param register_password:
        :param register_email:
        :return:
        '''
        #点击取消更新，跳过 按钮
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('==========register_action===========')
        #登录页面，点击注册按钮
        self.driver.find_element(*self.register_text).click()

        #注册页面，先上传头像
        logging.info('update  userhaeader')
        self.driver.find_element(*self.reg_userheader).click()
        self.driver.find_elements(*self.item_img)[3].click()
        self.driver.find_element(*self.save_Btn).click()


        #设置用户名
        logging.info('register username is %s' %register_name)
        self.driver.find_element(*self.register_username).send_keys(register_name)

        #设置密码
        logging.info('register password is %s' % register_password)
        self.driver.find_element(*self.register_password).send_keys(register_password)

        #输入邮箱
        logging.info('register email is %s' % register_email)
        self.driver.find_element(*self.register_email).send_keys(register_email)

        #点击立即注册按钮
        logging.info('click register button')
        self.driver.find_element(*self.register_btn)

        #判断是否进入到完善信息页面，注册太频繁会被拦截
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error("register fail !")
            self.getScreenShot('register fail')
            return False
        else:
            self.add_register_info()

            #注册结果判断
            if self.check_registerStatus():
                return True
            else:
                return False


    def  add_register_info(self):
        '''
        院校选择页面，选择院校、专业
        :return:
        '''
        logging.info('============add_register_info================')
        #院校选择
        logging.info('select shool')
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.forum_title)[2].click()
        self.driver.find_elements(*self.university)[1].click()

        #选择专业
        logging.info('select major')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_group_title)[2].click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()

        self.driver.find_element(*self.perfectinfomation_goBtn).click()


    def check_registerStatus(self):
        '''
        检查是否注册成功
        :return:
        '''
        logging.info('==========check_registerStatus============')
        self.check_market_ad()
        try:
            self.driver.find_element(*self.myself_btn).click()
            self.driver.find_element(*self.usercenter_name)
        except NoSuchElementException:
            logging.error("register Fail !")
            self.getScreenShot('register Fail')
            return False
        else:
            logging.info("register success !")
            self.getScreenShot('register success')
            return True

if __name__ == '__main__':
    driver =appium_desired()
    resigert = RegisterView(driver)

    username = 'carl' +str(random.randint(1000,9999))
    password = 'abc' +str(random.randint(1000,9999))
    email = 'qwe'+str(random.randint(1000,9999))+'@qq.com'
    resigert.register_action(username,password,email)








