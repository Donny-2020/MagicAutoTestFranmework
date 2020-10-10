import os

from retrying import retry

from ui.common.driver import Driver
import time
from func.read_xml import readXml

class Public(Driver):

    def loginRuntime(self,url,username,password):
        '''登录PC端运行平台'''

        self.openUrl(url)
        self.clickElement(readXml("login","account"))
        self.sendKeys(readXml("login","username"),username)
        self.sendKeys(readXml("login","password"),password)
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
        elements = self.getElements(loc)
        if len(elements)==0:
            time.sleep(1)
            self.F5()
            self.getElements(loc)[2].click()
        else:
            elements[2].click()

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


    def submitComment(self):
        '''点击表单评论提交按钮'''
        loc = readXml("form_comment","submit")
        self.clickElement(loc)

    def commentAddAnnex(self,file_name):
        '''添加评论附件'''
        loc = readXml("form_comment","add_annex")
        self.clickElement(loc)
        time.sleep(1)
        os.system("D:\Projects\MagicAutoTestFranmework\\ui\data\exe\\uploadpic.exe %s"%file_name)



    def delete_comment(self,loc_time):
        '''根据评论时间，删除评论'''

        loc = readXml("form_comment", "up_time").format(uptime=loc_time)
        self.moveToElement(loc)
        self.clickElement(readXml("form_comment", "delete_btn").format(uptime=loc_time))
        self.clickElement(readXml("form_comment","confrim"))

    def edit_comment(self,loc_time):
        '''编辑评论'''
        loc = readXml("form_comment", "up_time").format(uptime=loc_time)
        self.moveToElement(loc)
        self.clickElement(readXml("form_comment", "edit_btn").format(uptime=loc_time))

    def editCommentPageAddAnnex(self,file_name):
        '''点击编辑页面添加附件按钮'''
        self.clickElement(readXml("form_comment", "edit_add_annex"))
        time.sleep(1)
        os.system("D:\Projects\MagicAutoTestFranmework\\ui\data\exe\\uploadpic.exe %s" % file_name)
        time.sleep(1)
        self.clickElement(readXml("form_comment","edit_confrim"))


    def editCommentPageDeleteAnnex(self):
        '''编辑页面删除附件'''

        self.clickElement(readXml("form_comment","edit_delte_annex"))
        self.clickElement(readXml("form_comment","edit_confrim"))


    def commentUploadFile(self,file_name):
        '''评论上传文件'''
        self.clickElement(readXml("form_comment","table_file"))
        self.clickElement(readXml("form_comment","upload_file"))
        time.sleep(1)
        os.system("D:\Projects\MagicAutoTestFranmework\\ui\data\exe\\uploadpic.exe %s" % file_name)
        time.sleep(1)
        self.clickElement(readXml("form_comment","upload_file_confirm"))