#coding=utf-8
'''
Created on 2018年8月3日

@author: Jerry
'''
import unittest
import pytest
from selenium import webdriver
from time import sleep
from nose_parameterized import parameterized


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://127.0.0.1:8000/"
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def user_login(self, username, password):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("inputUsername").send_keys(username)
        driver.find_element_by_id("inputPassword").send_keys(password)
        driver.find_element_by_id("Login").click()

    @parameterized.expand([
        ("user_null", '', "123", "请输入帐号"),
        ("pawd_null", "user", '', "请输入密码"),
        ("login_error", "error", "error", "帐号或密码错误"),
        ("login_success", "admin", "admin123456", "admin你好"),
    ])
    def test_login(self, name, username, password, assert_text):
        self.user_login(username, password)
        if name == "login_success":
            sleep(2)
            tips = self.driver.find_element_by_id("user").text
            self.assertEqual(tips, assert_text)
        else:
            tips = self.driver.find_element_by_id("tips").text
            self.assertEqual(tips, assert_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)