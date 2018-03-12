# author__ = 'wang'
# -*- coding: utf-8 -*-

import unittest
import requests


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        print "start..."


# 运营后台登录
#     def test_background_login(self):
#         post_url = "https://console-zzhw.thy360.com/py/v4/admin/auth/login"
#         data = {
#             "username": "joedu",
#             "password": "root@01"
#         }
#         response = requests.post(post_url, json=data)
#         print (response.text)
#         # 获取token
#         token = response.json()['token']
#         print token
#         # 打印响应吗
#         print response.status_code
#         # 比较结果
#         self.assertEqual(response.status_code, 200)
#         return token

    def test_get_coupon_list(self):
        url = "https://console-devtest-zzhw.thy360.com/py/v4/admin/config/coupon/?limit=20&page=1"
        token = "b6530c2a-21cd-11e8-9810-525400aeec81"
        response = requests.get(url, token)
        print response.status_code
        print response.text
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyTestSuite("test_get_coupon_list"))
    # suit.addTest(MyTestSuite(""))
    runner = unittest.TextTestRunner()
    runner.run(suit)







