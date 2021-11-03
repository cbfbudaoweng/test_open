# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/9/8 16:32
# @File    : test_AddContacts.py
"""
（1）实现添加联系人测试用例 （灵活使用元素定位，并添加断言）
（2）实现添加多条联系人测试用例
"""
from appium import webdriver


class TestAddContacts:
    def setup(self):
        # cps={}
        # cps["platformName"] = "android"
        # cps["deviceName"] = "127.0.0.1:7555"
        cps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": " com.tencent.wework",
            "appActivity": ".launch.WwMainActivity"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cps)

    def teardown(self):
        pass

    def test_add_contacts(self):
        pass
