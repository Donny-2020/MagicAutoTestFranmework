import time

from func.read_yaml import readYaml
from ui.project import qiqiao
from selenium import webdriver
from func.read_xml import readXml
import unittest


class TestSingleLineText(unittest.TestCase):
    '''测试单行文本基础属性'''

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        url = readYaml("qa.yaml","qa","singlelinetext")
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
        '''测试单行文本必填'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        error_msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(error_msg,"不能为空")

    def test_onlyone(self):
        '''测试单行文本唯一校验'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("必填_唯一","测试")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//p[@class='el-message__content']")
        self.assertEqual(msg,"[必填_唯一]值必须唯一")

    def test_length_limit(self):
        '''测试单行文本长度限制'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("必填_唯一", "测试")
        qiqiao.singleLineText(self.driver).sendValue("字符2到10","道")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg,"字符长度必须在2和10之间")

    def test_english_length_limit(self):
        '''测试单行文本输入英文并限制长度'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("必填_唯一", "测试")
        qiqiao.singleLineText(self.driver).sendValue("英文5到10","Donn")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "字符长度必须在5和10之间")

    def test_input_number_or_english(self):
        '''测试单行文本输入英文或数字'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("必填_唯一", "测试")
        qiqiao.singleLineText(self.driver).sendValue("数字或英文2到10", "道一")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "请输入数字或英文")

    def test_default_value(self):
        '''测试单行文本默认值'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        default = qiqiao.public(self.driver).getAttribute(readXml("single_line_text","sendValue").format(name="默认"),"title")
        self.assertEqual(default,"道一七巧测试")

    def test_data_linkage(self):
        '''测试单行文本数据联动'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("必填_唯一", "测试")
        time.sleep(1)
        link_value = qiqiao.public(self.driver).getAttribute(readXml("single_line_text", "sendValue").format(name="数据联动"),
                                                          "title")
        self.assertEqual(link_value, "20")

    def test_zzzz(self):
        '''退出浏览器'''
        self.driver.quit()