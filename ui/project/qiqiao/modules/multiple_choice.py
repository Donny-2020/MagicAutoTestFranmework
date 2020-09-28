import time
from func.read_xml import readXml
from ui.common.driver import Driver

class MultipleChoice(Driver):


    def checked(self,fild_name,*args):
        '''非下拉多项选择输入值'''
        for i in args:
            loc = readXml("multiple_choice","send").format(name=fild_name,index=i)
            self.clickElement(loc)


    def dropDown(self,fild_name,*args):
        '''下拉类型多项选择输入值'''
        loc = readXml("multiple_choice","sendValue").format(name=fild_name)
        self.clickElement(loc)
        time.sleep(0.5)
        for value in args:
            self.clickElement(readXml("multiple_choice", "selectorname").format(name=value))
        self.clickElement(readXml("multiple_choice", "packupselector").format(name=fild_name))



    def searchData(self,filed_name,value):
        '''使用多项选择字段筛选页面数据'''
        loc = readXml("multiple_choice","search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(readXml("multiple_choice","selectorname").format(name=value))
        self.clickElement(readXml("multiple_choice","packup").format(name=filed_name))
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")


    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的多项选择输入数据'''
        loc =  readXml("multiple_choice","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)