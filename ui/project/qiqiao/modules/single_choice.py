import time
from ui.common.driver import Driver
from func.read_xml import readXml

class SingleChoice(Driver):

    def sendValue(self,fild_name,num):
        '''单项选择组件输入值'''
        loc = readXml("single_choice","sendValue").format(name=fild_name,index=num)
        self.clickElement(loc)

    def dropDown(self, filed_name,value):
        '''下拉类型输入值'''
        loc = readXml("single_choice","dropdown").format(name=filed_name)
        self.clickElement(loc)
        self.clickElement(readXml("single_choice","dropvalue").format(name=value))

    def searchData(self,filed_name,value):
        '''使用单项选择字段筛选页面数据'''
        loc = readXml("single_choice","search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(readXml("single_choice","value").format(name=value))
        self.clickElement(readXml("single_choice","packup").format(name=filed_name))


    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的单项选择输入数据'''
        loc =  readXml("single_choice","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)