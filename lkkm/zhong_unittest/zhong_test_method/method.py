# coding:utf-8
from selenium import webdriver
import time
import random
import os
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd #读取
from xlutils.copy import copy #复制写入

import logging
from zhong_unittest.zhong_test_log.zhong_test_logmethod import *
from zhong_unittest.zhong_test_conf.zhong_test_env.zhong_test_config import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class startMethod(object):
    '''封装ID获取元素'''
    def action_Id(self,id,text):
        if text=='obtain':
            pro = '获取元素：'
            self.logger.info(u'>>>%s%s' % (pro, id))
            return self.driver.find_element_by_id(id)
        else:
            if text=='click':
                pro = '点击控件：'
                self.logger.info(u'>>>%s%s' % (pro, id))
                return self.driver.find_element_by_id(id).click()
            else:
                pro = '输入内容为：'
                self.logger.info(u'>>>定位控件%s,%s%s' % (id,pro,text))
                return self.driver.find_element_by_id(id).set_text(text)

    '''封装登录app方法'''
    def loginlkkm(self, a, b):
        self.driver.find_element_by_id(bottom['请选择小区id']).click()
        self.driver.find_element_by_id(login['账号id']).set_text(a)
        self.logger.info('输入账号为{}'.format(a))
        self.driver.find_element_by_id(login['获取验证码id']).click()
        self.logger.info('点击获取验证码')
        self.driver.find_element_by_id(login['输入验证码id']).set_text(b)
        self.logger.info('输入验证码为{}'.format(b))
        self.driver.find_element_by_id(login['登录id']).click()
        self.logger.info('点击登录按钮')
        self.driver.find_element_by_id(login['跳过id']).click()
        self.logger.info('点击跳过按钮')
        try:
            WebDriverWait(self, 20).until(
                lambda driver: startMethod.action_Id(self, bottom['我的id'], 'obtain'))  # 验证页面是否正常跳转成功
            self.logger.info('登录成功')
        except:
            self.logger.info('登录失败')

    '''封装退出app方法'''
    def backLogin(self):
        while True:
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
                self.driver.find_element_by_id(flash['页面返回id']).click()
                time.sleep(1)
                self.logger.info('获取到返回按钮，点击返回')
            except:
                break
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(bottom['我的id']))
        try:
            startMethod.action_Id(self, bottom['我的id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(my['设置id']))
        except:
            self.assertEqual(1, 2, msg='网络异常')
        try:
            self.driver.find_element_by_id(my['设置id']).click()
            WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_id(setting['退出登录id']))
            self.driver.find_element_by_id(setting['退出登录id']).click()
        except:
            self.assertEqual(1, 2, msg='网络异常')
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"确定要退出当前账户吗？\"]'))
            self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"确定\"]').click()
        except:
            self.assertEqual(1, 2, msg='网络异常')

    '''封装一个滑动toach的方法'''
    def toachSweip(self, x, y, x1, y1):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=1000).move_to(x=x1, y=y1).release().perform()

    '''封装一个控件滑动'''
    def scrollAction(self,id,n,m):  #n滑动次数，m 是控件高度内，存在的多少个数字间隔
        a=self.driver.find_element_by_id(id)
        actionPosition=a.location #控件初始坐标坐标，得到dict{x:宽，y：高}
        actionSize=a.size  #获取控件的宽度和高度，得到dict{height:高度，width：宽度}，这个是控件的
        px=self.driver.get_window_size()['width']#获取屏幕宽度
        py=self.driver.get_window_size()['height']#获取屏幕高度
        start1=actionPosition['x']/px  #定位控件相对x坐标
        start2=actionPosition['y']/py  #定位控件相对y坐标
        jj=actionSize['height']//m/py #获取每次滑动的间隔相对坐标
        for  i in  range(n):
            action=TouchAction(self.driver)
            action.press(x=start1,y=start2).wait(ms=1000).move_to(x=start1,y=(start2-jj)).release()
            action.perform()

class titleMethod(object):
    '''excelb表格读取'''
    def duQu_Exlce(self,Sheet,a,b):
        exlce_Name = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\lkkm\zhong_unittest\zhong_exlce_case\denglu_excel.xls')  # 打开excel文件格式为xlsx有的是xls
        table = exlce_Name.sheet_by_name(Sheet)
        cell_a1 = table.cell(a,b).value  # a代表行——从零开始   b代表列 从零开始
        return cell_a1
        self.logger.info(u'>>>获取excel表格内容：{}'.format(cell_a1))

    '''封装手机KeyCode方法'''
    def Keycode(self,a):
        os.popen('adb shell input keyevent '+ str(a))

    '''封装获取toast弹框'''
    def find_toast(self,message):
        logging.info("查找toast值---'%s'" %(message))
        try:
            toast_Code = ('xpath','.//*[contains(@text,"%s")]'.format(message))
            WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_Code))

            self.logger.info('获取到toast:{}'.format(message))
        except:
            self.logger.error('未获取到toast:{}'.format(message))


    '''等待定位元素'''
    def wait_time(self,resourceid,waitTime=None):
        try:
            if waitTime==None:
                waitTime=10
            WebDriverWait(waitTime).until(lambda driver:driver.find_element_by_id(resourceid))
            self.logger.info(u'>>>检测到{},页面未跳转成功'.format(resourceid))
        except Exception as f:
            print(f)
            self.logger.info(u'>>>未检测到{},页面跳转成功'.format(resourceid))

#     '''重复点击按钮id'''
# def repeat(self,id,m):
#     a = 0
#     while m > a :
#         c=self.driver.find_element_by_id(id)
#         c.click
#         a = a +1
#         time.sleep(2)















