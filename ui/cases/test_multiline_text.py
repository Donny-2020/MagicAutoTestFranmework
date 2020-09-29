import time
from func.read_yaml import readYaml
from ui.project import qiqiao
from selenium import webdriver
from func.read_xml import readXml
import unittest


class TestMultilineText(unittest.TestCase):
    '''测试多行文本组件'''
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        url = readYaml("qa.yaml","qa","multilinetext")
        usename = readYaml("qa.yaml","qa","username")
        password = readYaml("qa.yaml","qa","password")
        qiqiao.public(self.driver).loginRuntime(url,usename,password)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    def test_required(self):
        '''测试多行文本必填'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        time.sleep(0.5)
        qiqiao.public(self.driver).clickSubmit()
        msg  = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg,"不能为空")

    def test_length_limit(self):
        '''测试多行文本长度限制'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.multilineText(self.driver).sendValue("必填_提示","必填")
        qiqiao.multilineText(self.driver).sendValue("长度10到15","测试长度限制")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg,"字符长度必须在10和15之间")


    def test_default(self):
        '''测试多行文本默认值'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        msg  = qiqiao.public(self.driver).getAttribute(readXml("multiline_text","sendValue").format(name="默认值"),"title")
        self.assertEqual(msg,"道一云七巧测试")

    def test_data_linkage(self):
        '''测试多行文本数据联动'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.multilineText(self.driver).sendValue("必填_提示","多文本")
        time.sleep(1)
        link_value = qiqiao.public(self.driver).getAttribute(readXml("multiline_text", "sendValue").format(name="数据联动"),
                                                          "title")
        self.assertEqual(link_value, "20")
