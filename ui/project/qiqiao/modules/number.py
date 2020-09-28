from ui.common.driver import Driver
from func.read_xml import readXml

class Number(Driver):

    def sendValue(self,fild_name,value):
        '''数字组件输入值'''
        loc = readXml("number","sendValue").format(name=fild_name)
        self.sendKeys(loc,value)

    def searchData(self,filed_name,value):
        '''使用数字字段筛选页面数据'''
        loc = readXml("number","search").format(name=filed_name)
        self.sendKeys(loc,value)


    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的数字输入数据'''
        loc =  readXml("number","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)