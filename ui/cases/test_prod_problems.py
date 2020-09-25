from ui.project import qiqiao
from selenium import webdriver
import time
import unittest
class QiqiaoProblem(unittest.TestCase):
    '''七巧生产补丁问题验证'''
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="D:\Donny\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        qiqiao.public(self.driver).loginRuntime()
    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_data(self):
        print("多线程测试")