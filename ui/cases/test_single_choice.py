import time

from func.read_yaml import readYaml
from ui.project import qiqiao
from selenium import webdriver
from func.read_xml import readXml
import unittest

class TestSingleChoice(unittest.TestCase):
    '''测试单项选择组件'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        url = readYaml("qa.yaml","qa","singlechoice")
        usename = readYaml("qa.yaml","qa","username")
        password = readYaml("qa.yaml","qa","password")
        qiqiao.public(cls.driver).loginRuntime(url,usename,password)


    def tearDown(self) -> None:
        try:
            time.sleep(1)
            self.driver.refresh()
        except Exception:
            pass

    def test_required(self):
        '''测试单项选择必填'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        error_msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(error_msg,"不能为空")

    def test_data_default(self):
        '''测试单项选择默认值'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        default_loc = "xpath=>//div[@data-mark='默认中国']/div//label[@class='el-radio is-checked']/span[2]"
        default = qiqiao.public(self.driver).getText(default_loc)
        self.assertEqual(default,"中国")


    def test_linke_option(self):
        '''测试单项选择关联选项'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleChoice(self.driver).dropDown("下拉","华为")
        html = self.driver.page_source
        self.assertIn("mate10",html)