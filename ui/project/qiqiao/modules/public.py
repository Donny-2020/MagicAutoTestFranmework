from ui.common.driver import Driver
from func.config import login
import time
from func.read_xml import readXml

class Public(Driver):

    def loginRuntime(self):
        '''登录PC端运行平台'''

        self.openUrl(login().url)
        self.clickElement(readXml("login","account"))
        self.sendKeys(readXml("login","username"),login().username)
        self.sendKeys(readXml("login","password"),login().password)
        self.clickElement(readXml("login","submit"))

    def openAppPage(self):
        '''打开应用页面'''
        element = self.getElement(readXml("runtime","apppage"))
        self.js("arguments[0].click()",element)

    def clickApp(self,appname):
        '''根据应用名称，打开应用'''
        loc = readXml("runtime","app").format(app=appname)
        self.clickElement(loc)

    def clickLeftMenu(self,menu_name):
        '''根据菜单名称，点击左侧菜单'''
        loc = readXml("runtime","leftmenu").format(menu=menu_name)
        self.clickElement(loc)

    def clickButtonInTitle(self,button_name):
        '''根据按钮名称，点击表头按钮'''
        loc = readXml("runtime","title_btn").format(button=button_name)
        self.clickElement(loc)

    def clickButtonInForm(self,button_name,row_num):
        '''点击表单数据行，操作区按钮'''
        loc = readXml("runtime","form_btn").format(button=button_name,row=row_num-1)
        self.getElements(loc)[2].click()

    def clickSearchBtn(self):
        '''点击搜索按钮'''
        loc =readXml("runtime","search_btn")
        self.clickElement(loc)

    def clickResetBtn(self):
        '''点击重置按钮'''
        loc = readXml("runtime","reset_btn")
        self.clickElement(loc)

    def clickExpand(self):
        '''点击展开按钮'''
        loc = readXml("runtime","expand")
        self.clickElement(loc)

    def openProcessPage(self):
        '''点击流程页面'''
        loc = readXml("runtime","precesspage")
        self.clickElement(loc)


    def openProcess(self,name):
        '''打开流程'''
        loc = readXml("runtime","openprecess").format(name)
        # loc = "xpath=>//p[@title='{}']/..".format(name)
        self.clickElement(loc)

    def clickSubmit(self):
        '''点击提交按钮'''
        loc = readXml("runtime","submit_btn")
        self.clickElement(loc)

    def clickDeleteInForm(self,button_name,row_num):
        '''点击表单数据行，操作区删除按钮'''
        loc = readXml("runtime","form_delete_btn").format(button_name,row_num)
        time.sleep(2)
        self.getElements(loc)[2].click()
        delete_loc = readXml("runtime","delete_confirm")
        self.clickElement(delete_loc)