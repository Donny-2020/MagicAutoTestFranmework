from ui.common.driver import Driver
from func.read_xml import readXml

class DateTime(Driver):

    def sendValue(self,fild_name,value):
        '''日期时间输入值'''
        loc = readXml("date_time","sendValue").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(readXml("date_time","label").format(name=fild_name))

    def searchData(self,filed_name,value):
        '''使用日期时间字段筛选页面数据'''
        loc = readXml("date_time","search").format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement(readXml("date_time","packup").format(name=filed_name))
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")

    def sendValueTimeInSubForm(self,sub_form,filed_name,value):
        '''子表单的日期时间输入数据'''
        loc =  readXml("date_time","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)