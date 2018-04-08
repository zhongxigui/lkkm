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


    def test03(self):
        time.sleep(3)
        startMethod.loginlkkm(self,17603031220,1234)
        startMethod.action_Id(self, bottom['客服id'], 'click')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_select_quyu', 'click') #请选择区域
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_suozaiquyu', 'click')  #所在区域
        startMethod.scrollAction(self,'com.lekelian.lkkm:id/loopview1',3,7)
        self.logger.info('滑动成功')
        titleMethod.repeat(self,'com.lekelian.lkkm:id/tv_sheng_queding',3)
        a =self.driver.find_element_by_id('com.lekelian.lkkm:id/tv_sheng_queding')
        a.click
        time.sleep(5)
        self.logger.info('第一次成功')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/tv_sheng_queding', 'click')
        time.sleep(5)
        a.click
        self.logger.info('第二次成功')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/tv_sheng_queding', 'click')
        a.click
        self.logger.info('第三次成功')
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/view_jiedao', 'click')
        titleMethod.repeat(self, 'com.lekelian.lkkm:id/tv_sheng_queding', 1)
        startMethod.action_Id(self, 'com.lekelian.lkkm:id/item_neardy_onclick', 'click')
        startMethod.backLogin(self)

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_slide('test01'))
    suiteTest.addTest(Test_slide('test02'))
    suiteTest.addTest(Test_slide('test03'))
    return suiteTest

if __name__ == '__main__':
    pathCode = 'C:\\Users\Administrator\Desktop\lkkm\zhong_unittest\zhong_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + '.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set, title=u'自动化测试报告', description=u'用例执行情况：')
    runner.run(suite())
    report_set.close()