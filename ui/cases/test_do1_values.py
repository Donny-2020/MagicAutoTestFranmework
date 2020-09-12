import unittest,time
from ui.project import qiqiao
from selenium import webdriver

class Do1Values(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="D:\Donny\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")


    def tearDown(self) -> None:
        pass
    def test_001(self):
        # qiqiao.public(self.driver).loginRuntime()
        # qiqiao.public(self.driver).openAppPage()
        # qiqiao.public(self.driver).clickApp("版本发布验收测试")
        # qiqiao.public(self.driver).clickButtonInForm("添加",0)
        # qiqiao.subForm(self.driver).clickAddOneData("子表单")
        # qiqiao.subForm(self.driver).clickAddButton("子表单")
        # qiqiao.singleLineText(self.driver).sendValueInSubForm("子表单","单行文本","自动化测试数据")
        print("OA系统测试")

