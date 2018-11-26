# coding:utf-8
import unittest,time
from zhong_unittest.startAPP import *
from zhong_unittest.zhong_test_method.method import *
import unittest,requests,HTMLTestRunner,time
from zhong_unittest.zhong_test_conf.zhong_test_env.zhong_test_config import *
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
import random

class Test_loginn(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    def test01(self):
        '''重复声波开门'''
        self.logger.info('************')
        startMethod.action_Id(self,bottom['请选择小区id'], 'click')
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',3,2))#输入正确手机号码
        startMethod.action_Id(self,login['获取验证码id'], 'click')  # 点击获取验证码
        time.sleep(3)
        startMethod.action_Id(self,login['输入验证码id'],titleMethod.duQu_Exlce(self,'登录',3,3))#输入验证码
        startMethod.action_Id(self,login['登录id'],'click')#点击登录
        startMethod.action_Id(self,login['跳过id'], 'click')
        time.sleep(3)
        startMethod.action_Id(self,bottom['开门id'],'click')
        time.sleep(1)
        startMethod.action_Id(self,bottom['请选择小区id'],'click')
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator("text(\"金钱包406\")").click()
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        self.logger.info('点击确定了')
        time.sleep(3)
        #startMethod.action_Id(self.bottom['开门按钮id'],'click')
        n=3
        i=0
        while i < n:

            self.driver.find_element_by_android_uiautomator(
                 'new UiSelector().resourceId("com.lekelian.lkkm:id/view_key_touch")').click()
            v=4
            l=0
            while l < v:
                VOL=titleMethod.Keycode(self, 25)
                l= l+1



            time.sleep(5)
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.lekelian.lkkm:id/btn_close")').click()
            i=i+1
            self.logger.info('结束')


        #startMethod.action_Id(self.bottom['关闭声音按钮'],'click')


def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(Test_loginn('test01'))
    #suiteTest.addTest(Test_login('test02'))
    #suiteTest.addTest(Test_login('test03'))
    return suiteTest

if __name__=='__main__':
    pathCode = 'C:\\Users\Administrator\Desktop\lkkm\zhong_unittest\zhong_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path ,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(suite())
    report_set.close()

