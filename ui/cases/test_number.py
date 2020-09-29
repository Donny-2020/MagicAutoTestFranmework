import time
from func.read_yaml import readYaml
from ui.project import qiqiao
from selenium import webdriver
from func.read_xml import readXml
import unittest

class TestNumber(unittest.TestCase):
    '''测试数字组件属性'''

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        url = readYaml("qa.yaml", "qa", "number")
        usename = readYaml("qa.yaml","qa","username")
        password = readYaml("qa.yaml","qa","password")
        qiqiao.public(self.driver).loginRuntime(url,usename,password)


    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()


    def test_required(self):
        '''测试数字组件必填'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.number(self.driver).sendValue("整数100到200",120)
        time.sleep(0.5)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "不能为空")

    def test_onlyone(self):
        '''测试数字组件唯一'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.number(self.driver).sendValue("必填唯一",100)
        qiqiao.number(self.driver).sendValue("整数100到200", 120)
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//p[@class='el-message__content']")
        self.assertEqual(msg,"[必填唯一]值必须唯一")

    def test_limit_size(self):
        '''测试数字组件限制范围'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.number(self.driver).sendValue("必填唯一", 100)
        qiqiao.number(self.driver).sendValue("整数100到200",20)
        time.sleep(0.5)
        qiqiao.public(self.driver).clickSubmit()
        msg = qiqiao.public(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "整数100到200的值必须在100和200之间")

    def test_default_value(self):
        '''测试数字组件默认值'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        default = qiqiao.public(self.driver).getAttribute(readXml("number","sendValue").format(name="默认100"),"title")
        self.assertEqual(default,"100")