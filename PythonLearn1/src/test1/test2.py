#coding=utf-8
import unittest
import pytest
from selenium import webdriver
from time import sleep

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

    def atest_login_01(self):
        self.user_login("", '123')
        tips = self.driver.find_element_by_id("tips").text
        self.assertEqual(tips, '请输入帐号')

    def atest_login_02(self):
        self.user_login("user", "")
        tips = self.driver.find_element_by_id("tips").text
        self.assertEqual(tips, '请输入密码')

    def atest_login_03(self):
        self.user_login("error", "error")
        tips = self.driver.find_element_by_id("tips").text
        self.assertEqual(tips, '帐号或密码错误')

    def atest_login_04(self):
        self.user_login("admin", "admin123456")
        sleep(2)
        tips = self.driver.find_element_by_id("user").text
        self.assertEqual(tips, 'admin你好')


if __name__ == '__main__':
    unittest.main()