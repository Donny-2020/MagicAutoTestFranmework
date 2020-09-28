from ui.common.driver import Driver
from func.read_xml import readXml

class MultilineText(Driver):
    def sendValue(self,fild_name,value):
        '''多行文本输入值'''
        loc = readXml("multiline_text","sendValue").format(name=fild_name)
        self.clear(loc)
        self.sendKeys(loc,value)

    def searchData(self,filed_name,value):
        '''使用多行文本字段筛选页面数据'''
        loc = readXml("multiline_text","search").format(name=filed_name)
        self.clear(loc)
        self.sendKeys(loc,value)

    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的多行文本输入数据'''
        loc =  readXml("multiline_text","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)
