from ui.project import qiqiao
from selenium import webdriver
import time
import unittest
class QiqiaoProblem(unittest.TestCase):
    '''七巧主流业务测试'''

    def setUp(self) -> None:
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path="D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
        qiqiao.public(self.driver).loginRuntime()


    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    def test_add_data(self):
        '''测试添加数据'''
        qiqiao.public(self.driver).clickLeftMenu("基础表")
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.singleLineText(self.driver).sendValue("单行文本","自动化")
        qiqiao.public(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("自动化",html)



    def test_upload_pic(self):
        '''测试图片上传'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.uploadPic(self.driver).uploadPicture("图片上传","ceshi.png")
        time.sleep(1)
        qiqiao.public(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("ceshi.png",html)


    def test_upload_file(self):
        '''测试上传文件'''
        qiqiao.public(self.driver).clickButtonInTitle("添加")
        qiqiao.uploadFile(self.driver).uploadFile("文件上传","动画图片.gif")
        time.sleep(2)
        qiqiao.public(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("动画图片.gif",html)

    def test_search_by_line_text(self):
        '''通过单行文本筛选页面数据'''

        qiqiao.singleLineText(self.driver).searchData("单行文本","测试数据")
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_multiline_text(self):
        '''通过多行文本筛选页面数据'''

        qiqiao.multilineText(self.driver).searchData("多行文本","哈哈哈")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_number(self):
        '''通过数字筛选页面数据'''

        qiqiao.number(self.driver).searchData("数字",15)
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)


    def test_search_by_single_choice(self):
        '''通过单项选择筛选页面数'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.singleChoice(self.driver).searchData("单项选择","日本")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)


    def test_search_by_multiple_choice(self):
        '''通过多项选择筛选页面数据'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.multipleChoice(self.driver).searchData("多项选择","奥迪")
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1", title)

    def test_search_by_date(self):
        '''通过日期筛选页面数据'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.date(self.driver).searchData("日期","2020-09-15","2020-09-17")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)


    def test_search_by_person_selector(self):
        '''通过人员选择筛选页面数据'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.personSelector(self.driver).searchData("人员单选","刁惠云")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_time(self):
        '''通过时间筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.time(self.driver).searchData("时间","11:30","12:00")
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_datetime(self):
        '''通过日期时间筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.dateTime(self.driver).searchData("日期时间","2020-09-15 00:00 至 2020-09-16 00:00")
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_department(self):
        '''通过部门选择筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.departSelector(self.driver).searchData("部门单选","产","创新技术中心->产品研发二部")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_address(self):
        '''通过地址选择筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.address(self.driver).searchData("地址选择器","河南省","郑州市","中原区")
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_score(self):
        '''通过评分字段筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.score(self.driver).searchData("评分",5)
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("1",title)

    def test_search_by_creaperson(self):
        '''通过创建人筛选页面数据'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.personSelector(self.driver).searchData("创建人","刁","刁惠云")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("0",title)


    def test_search_by_createdate(self):
        '''通过创建日期筛选页面数据'''

        qiqiao.public(self.driver).clickExpand()
        qiqiao.date(self.driver).searchData("创建时间","2020-09-13","2020-09-14")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("0",title)

    def test_search_by_editdate(self):
        '''通过修改日期筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.date(self.driver).searchData("修改时间","2020-09-13","2020-09-14")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("0",title)

    def test_combination_search(self):
        '''测试组合筛选页面数据'''
        qiqiao.public(self.driver).clickExpand()
        qiqiao.date(self.driver).searchData("修改时间","2020-09-13","2020-09-14")
        qiqiao.personSelector(self.driver).searchData("创建人", "刁", "刁惠云")
        qiqiao.departSelector(self.driver).searchData("部门单选","产","创新技术中心->产品研发二部")
        qiqiao.public(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.public(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("0",title)


