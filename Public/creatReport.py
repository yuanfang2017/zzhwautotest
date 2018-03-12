# -*- coding: utf-8 -*-
import os
from HTMLTestRunner import HTMLTestRunner

_author_ = 'fannie'
_data_ = '2018/3/7 16:34'


"""
封装创建报告的模板
"""


def test_creat_report(now_time, suit):

    # 获取当前项目的路径
    report_path = os.path.dirname(os.path.dirname(__file__))
    # 获取当前运行模本的路径名
    test = os.path.basename(os.path.realpath(__file__))
    test_name = test.split('.')[0]
    print ("test:" + test)
    print("report_path:" + report_path)
    print ("test_name:" + test_name)
    file_path = os.path.join(report_path, 'report/')
    print ("file_path:" + file_path)
    file_name = file_path + test_name + "_" + now_time + u".html"
    print ("file_name:" + file_name)
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"接口自动化测试报告", description=u"接口自动化测试用例详细情况")
    runner.run(suit)
    fp.close()
    return file_name




