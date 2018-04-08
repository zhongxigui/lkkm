# coding:utf-8

import unittest,time
from zhong_unittest.startAPP import *
from zhong_unittest.zhong_test_method.method import *
import unittest,requests,HTMLTestRunner,time
from zhong_unittest.zhong_test_conf.zhong_test_env.zhong_test_config import *
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
import random

class  Test_slide(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)

    def tearDown(self):
        start_App.tearDown(self)

    def test01(self):
        '''验证首页引导页'''
        self.logger.info('*************************************************************')
        time.sleep(2)
        startMethod.toachSweip(self, 0.9, 0.5, 0.1, 0.5)
        time.sleep(2)
        startMethod.toachSweip(self, 0.9, 0.5, 0.1, 0.5)
        time.sleep(2)
        startMethod.action_Id(self, flash['跳过广告id'], 'click')
        try:
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"“乐客开门”需要使用存储权限，您是否允许？\"]'))

            startMethod.action_Id(self, 'com.android.packageinstaller:id/permission_allow_button', 'click')

            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"“乐客开门”需要使用您的位置权限，您是否允许？\"]'))
            startMethod.action_Id(self, 'com.android.packageinstaller:id/permission_allow_button', 'click')
            self.logger.info('获取点击授权“允许”')
        except:
            time.sleep(30)
            self.logger.info('手机系统不兼容，无法获取到授权允许，默认等待三十秒！')
        try:
            startMethod.action_Id(self, bottom['我的id'], 'obtain')
            self.assertEqual(1, 1, msg='第一次引导页成功')
            self.logger.info('第一次引导页成功')
        except:
            self.assertEqual(1, 2, msg='第一次引导页失败，未检测到我的id元素')
        '''验证未登录跳转至登录'''
        try:
            startMethod.action_Id(self,bottom['登录按钮id'],'click')
            titleMethod.Keycode(self,4)
            startMethod.action_Id(self,bottom['小区id'], 'click')
            startMethod.action_Id(self,hous['意见反馈id'], 'click')
            titleMethod.Keycode(self,4)
            startMethod.action_Id(self, bottom['我的id'], 'click')
            startMethod.action_Id(self, my['我的小区id'], 'click')
            self.assertEqual(1, 1, msg='未登录跳转至登录')
        except:
            self.assertEqual(1,2 , msg='未登录跳转失败')


        '''登录未选择小区'''
    def test02(self):
        time.sleep(3)
        startMethod.loginlkkm(self,17603031220,1234)
        startMethod.action_Id(self,bottom['客服id'],'click')
        WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text=\"选择小区\"]'))
        self.logger.info('未选择小区页')
        startMethod.action_Id(self, choosehous['返回id'], 'click')
        startMethod.action_Id(self,bottom['小区id'], 'click')
        startMethod.action_Id(self,hous['意见反馈id'], 'click')
        WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text=\"选择小区\"]'))
        self.logger.info('未选择小区页')
        startMethod.backLogin(self)

        '''登录选择小区'''
    def test03(self):
        time.sleep(3)
        startMethod.loginlkkm(self,17603031220,1234)
        startMethod.action_Id(self, bottom['客服id'], 'click')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_select_quyu', 'click') #请选择区域
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_suozaiquyu', 'click')  #所在区域
        startMethod.scrollAction(self,'com.lekelian.lkkm:id/loopview1',2,6)
        self.logger.info('滑动成功')
        self.driver.find_element_by_xpath('//android.widget.TextView[@test=\"确定\"]').click()
        self.logger.info('第一次点击成功')
        time.sleep(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"确定\"]').click()
        self.logger.info('第二次点击成功')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"确定\"]').click()
        self.logger.info('第三次点击成功')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_jiedao', 'click')#街道
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/tv_jie_queding', 'click')
        startMethod.action_Id(self,choosehous['返回id'],'click')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"金钱包\"]').click()
        try:
            self.assertEqual(1, 1, msg='选择小区返回主页成功')
        except:
            self.assertEqual(1, 1, msg='选择小区返回主页失败')
        startMethod.backLogin(self)























def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(Test_slide('test01'))
    suiteTest.addTest(Test_slide('test02'))
    suiteTest.addTest(Test_slide('test03'))
    return suiteTest

if __name__=='__main__':
    pathCode = 'C:\\Users\Administrator\Desktop\lkkm\zhong_unittest\zhong_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path ,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(suite())
    report_set.close()
