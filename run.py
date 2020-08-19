import unittest
import time
import common.HTMLTestRunnerNew as ht

suite=unittest.TestSuite()
load=unittest.defaultTestLoader
testcases=load.discover('test_cases',pattern='test_*.py')
suite.addTest(testcases)
#strtime=time.strftime('%Y-%m-%d %H-%M-%S')
filename=r'report/reporter.html'
with open(filename,'wb') as f:
    runner=ht.HTMLTestRunner(stream=f,title='学生管理系统接口测试报告',
                             description='xxxxxxxxxxxxxxx',tester='lee')
    runner.run(suite)