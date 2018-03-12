# -*- coding: utf-8 -*-
import unittest
import requests
import time
import sys
from Public.creatReport import test_creat_report
from Public.sendEmail import send_email
from Public.logger import Log_message
reload(sys)
sys.setdefaultencoding('utf-8')

_author_ = 'fannie'
data_ = '2018/3/7 14:43'


class MyTestSuite(unittest.TestCase):
    Log_message = Log_message()
    def setUp(self):
        """
        建立数据库的链接，以及初始化一些数据
        :return:
        """
        print "start..."

    def test_get_coupon_list(self):
        self.Log_message.info("获取优惠券列表用例------start--------")
        url = "https://console-devtest-zzhw.thy360.com/py/v4/admin/config/coupon/?limit=20&page=1"
        self.Log_message.info("请求的URL地址是："+url)
        headers = {"token ": "b6530c2a-21cd-11e8-9810-525400aeec81"}
        response = requests.get(url, headers=headers, verify=False)
        code = response.status_code
        self.Log_message.info("接口的状态是：%s" %code)
        text = response.text
        self.Log_message.info("接口返回的值是：%s" %text)
        self.assertEqual(response.status_code, 200)

    # def create_coupon(self):
    #     url = "https://console-devtest-zzhw.thy360.com/py/v4/admin/config/coupon/"
    #     headers = {"token": "b6530c2a-21cd-11e8-9810-525400aeec81"}
    #     data = {"type": 1,
    #             "thresholdUnit": 1,
    #             "scope": 0,
    #             "fetch_type": 0,
    #             "title": "自动化测试6",
    #             "threshold": 100,
    #             "start": "2018-03-13 15:55:00",
    #             "denomination": 200,
    #             "end": "2018-03-29 13:25:00",
    #             "count": 200,
    #             "user_range": 1,
    #             "cluster": []
    #             }
    #     response = requests.post(url, headers=headers, json=data, verify=False)
    #     print response.status_code
    #     print response.text
    #     self.assertEqual(response.status_code, 201)
    #     coupon_id = response.json()['data']['id']
    #     print coupon_id
    #     return coupon_id

    def give_coupon(self):
        self.Log_message.info("赠送优惠券------start--------")
        url = "https://console-devtest-zzhw.thy360.com/py/v4/admin/config/coupon/give/"
        self.Log_message.info("请求的URL地址是：" + url)
        headers = {"token": "b6530c2a-21cd-11e8-9810-525400aeec81"}
        # coupon_id = MyTestSuite.create_coupon(self)
        data = {"coupon": "114",
                "sheet": 1,
                "tels": ["15507546429"]}
        response = requests.post(url, headers=headers, json=data, verify=False)
        code = response.status_code
        self.Log_message.info("接口的状态是：%s" % code)
        text = response.text
        self.Log_message.info("接口的状态是：%s" % text)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """
        清除在数据库中产生的数据
        :return:
        """
        pass


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyTestSuite("test_get_coupon_list"))
    # suit.addTest(MyTestSuite("create_coupon"))
    suit.addTest(MyTestSuite("give_coupon"))
    nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_name = test_creat_report(nowtime, suit)
    send_email(file_name)



