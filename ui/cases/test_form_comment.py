from selenium.common.exceptions import NoAlertPresentException
from ui.project import qiqiao
from selenium import webdriver
import time
import unittest
from func.read_yaml import readYaml


class TestFormComment(unittest.TestCase):
    '''测试表单评论'''

    @classmethod
    def setUpClass(cls) -> None:
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        url = readYaml("prod.yaml","prod","pc_business")
        usename = readYaml("prod.yaml","prod","username")
        password = readYaml("prod.yaml","prod","password")
        cls.driver = webdriver.Chrome(executable_path="D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        qiqiao.public(cls.driver).loginRuntime(url,usename,password)


    def tearDown(self) -> None:
        try:
            time.sleep(1)
            self.driver.refresh()
        except Exception:
            pass

    def test_comment_requried(self):
        '''测试表单评论必填'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.public(self.driver).submitComment()
        msg = qiqiao.public(self.driver).getText("xpath=>//p[@class='el-message__content']")
        self.assertEqual(msg, "评论内容为必填")
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass


    def test_add_comment(self):
        '''测试添加评论'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        now = time.time()
        value = str(now) + "测试填写表单评论"
        qiqiao.richText(self.driver).sendValue(value)
        qiqiao.public(self.driver).submitComment()
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(value, html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass


    def test_upload_annex(self):
        '''测试表单评论添加附件'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.richText(self.driver).sendValue("自动化上传图片")
        filename = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))+".png"
        file_path = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename
        qiqiao.public(self.driver).getScreenshot(file_path)
        qiqiao.public(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        qiqiao.public(self.driver).submitComment()
        html = self.driver.page_source
        self.assertIn(filename, html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass

    def test_delete_comment(self):
        '''测试删除评论'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.richText(self.driver).sendValue("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time()))+".png"
        file_path = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename
        qiqiao.public(self.driver).getScreenshot(file_path)
        qiqiao.public(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.public(self.driver).submitComment()
        qiqiao.public(self.driver).F5()
        qiqiao.public(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.public(self.driver).delete_comment(loc_time)
        time.sleep(1)
        html = self.driver.page_source
        self.assertNotIn(filename, html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass


    def test_edit_comment(self):
        '''测试评论编辑页面上传附件'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.richText(self.driver).sendValue("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time()))+".png"
        file_path = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename
        qiqiao.public(self.driver).getScreenshot(file_path)
        qiqiao.public(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.public(self.driver).submitComment()
        qiqiao.public(self.driver).F5()
        qiqiao.public(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.public(self.driver).edit_comment(loc_time)
        filename1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))+".png"
        file_path1 = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename1
        qiqiao.public(self.driver).getScreenshot(file_path1)
        qiqiao.public(self.driver).editCommentPageAddAnnex(file_path1)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(filename1, html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass

    def test_edit_delete_annex(self):
        '''测试评论编辑页面删除附件'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.richText(self.driver).sendValue("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time()))+".png"
        file_path = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename
        qiqiao.public(self.driver).getScreenshot(file_path)
        qiqiao.public(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.public(self.driver).submitComment()
        qiqiao.public(self.driver).F5()
        qiqiao.public(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        qiqiao.public(self.driver).edit_comment(loc_time)
        qiqiao.public(self.driver).editCommentPageDeleteAnnex()
        time.sleep(1)
        html = self.driver.page_source
        self.assertNotIn(filename, html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass


    def test_comment_upload_file(self):
        '''测试评论上传文件'''
        qiqiao.public(self.driver).clickButtonInForm("详情", 1)
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time()))+".png"
        file_path = "D:\Projects\MagicAutoTestFranmework\\ui\screenshot\\"+filename
        qiqiao.public(self.driver).getScreenshot(file_path)
        qiqiao.public(self.driver).commentUploadFile(file_path)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(filename,html)
        try:
            qiqiao.public(self.driver).F5()
            qiqiao.public(self.driver).acceptAlert()
        except NoAlertPresentException:
            pass


    def test_zzzz(self):
        '''关闭浏览器'''
        self.driver.quit()