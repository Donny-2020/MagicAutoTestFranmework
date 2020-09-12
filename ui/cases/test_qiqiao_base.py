from ui.project import qiqiao
from selenium import webdriver
import time
import unittest
class QiqiaoBase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="D:\Donny\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        qiqiao.public(self.driver).loginRuntime()
    def tearDown(self) -> None:
        self.driver.quit()


    def test_open_process(self):
        '''打开流程页面'''
        qiqiao.public(self.driver).openProcessPage()
        time.sleep(0.5)
        url = qiqiao.public(self.driver).getUrl()
        rel_url = "https://tqy.do1.net.cn/qa-runtime/?corp_id=wwf0d1682926a0822d#/process/processList"
        self.assertEqual(url,rel_url)


    def test_initiate_process(self):
        '''测试发起流程'''
        qiqiao.public(self.driver).openProcessPage()
        qiqiao.public(self.driver).openProcess("基础表流程")
        qiqiao.singleLineText(self.driver).sendValue("单行文本","测试发起流程")