# coding:utf-8
import  unittest,requests,HTMLTestRunner,time,os
from appium import webdriver
PATH = lambda  p:os.path.abspath(
       os.path.join(os.path.dirname(__file__),p)
)
print(PATH)

def allCase():
    #待执行用例的目录
    case_dir=r'../zhong_test_case'
    #构造测试集合
    #suite=unittest.TestSuite()
    #获取到一个list集合
    allTest = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #pattern————匹配脚本名称规则，test*.py是匹配所有test开头的所有脚本
    #top_level_dir 这个是顶层目录的名称 ，一般为空就可以了
    # for test_suite in allTest:
    #     for test_case in test_suite:
    #         suite.addTests(test_case)
    return  allTest
#pathCode = 'C:\\Users\\\Desktop\python01\\_unittest\_test_result\\'
#cuitime=time.s('%Y%m%d%H%M%S',time.localtime())
#report_path = pathCode++'.html'
#report_set = open(report_path, 'wb')
#runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
if __name__=="__main__":
    pathCode = 'C:\\Users\\Administrator\Desktop\lkkm\\zhong_unittest\\zhong_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(allCase())
    report_set.close()
