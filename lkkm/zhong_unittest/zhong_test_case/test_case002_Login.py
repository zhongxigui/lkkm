# coding:utf-8

from zhong_unittest.startAPP import *
from zhong_unittest.zhong_test_method.method import *
import unittest,requests,HTMLTestRunner,time
from zhong_unittest.zhong_test_conf.zhong_test_env.zhong_test_config import *

class Test_login(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)

    def test01(self):
        '''输入空的验证码'''
        self.logger.info('************')
        startMethod.action_Id(self,bottom['请选择小区id'], 'click')
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',2,2))#输入正确手机号码
        startMethod.action_Id(self,login['获取验证码id'], 'click')  # 点击获取验证码
        startMethod.action_Id(self, login['输入验证码id'], titleMethod.duQu_Exlce(self, '登录', 2, 3))  # 输入空验证码
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        try:
            WebDriverWait(self, 2).until(lambda driver: self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1, 1, msg='验证码为空，输入密码，不可登录，符合预期')
        except:
            self.assertEqual(1, 2, msg='验证码为空，输入密码，可以登陆，不符合预期')

    def test02(self):
        '''不输入点击【获取验证码】'''
        startMethod.action_Id(self,bottom['请选择小区id'], 'click')
        titleMethod.find_toast(self,'请先登录')
        startMethod.action_Id(self, login['获取验证码id'], 'click')
        titleMethod.find_toast(self,' 电话号码不能为空')



    def test03(self):
        '''输入正确手机号码，正确密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self,bottom['请选择小区id'], 'click')
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',1,2))#输入正确手机号码
        startMethod.action_Id(self,login['获取验证码id'], 'click')  # 点击获取验证码
        startMethod.action_Id(self,login['输入验证码id'],titleMethod.duQu_Exlce(self,'登录',1,3))#输入验证码
        startMethod.action_Id(self,login['登录id'],'click')#点击登录
        startMethod.action_Id(self,login['跳过id'], 'click')
        time.sleep(3)
        titleMethod.take_screenShot(self,'jietu')
        try:
            WebDriverWait(self, 2).until(lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"请选择小区\"]'))
            self.assertEqual(1, 1, msg='输入正确手机号码，正确验证码，可以登陆，符合预期')
        except:
            self.assertEqual(1, 2, msg='输入正确手机号码，正确密码，不可登录，不符合预期')
        startMethod.backLogin(self)


def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(Test_login('test01'))
    suiteTest.addTest(Test_login('test02'))
    suiteTest.addTest(Test_login('test03'))
    return suiteTest

if __name__=='__main__':
    pathCode = 'C:\\Users\Administrator\Desktop\lkkm\zhong_unittest\zhong_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path ,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(suite())
    report_set.close()


