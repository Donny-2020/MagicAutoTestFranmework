from ui.common.driver import Driver
from func.read_xml import readXml

class Date(Driver):

    def sendValue(self,fild_name,value):
        '''日期输入值'''
        loc = readXml("date","sendValue").format(name=fild_name)
        self.sendKeys(loc,value)

    def searchData(self,filed_name,start,end):
        '''使用日期字段筛选页面数据'''
        start_loc = readXml("date","startTime").format(name=filed_name)
        self.sendKeys(start_loc,start)
        end_loc = readXml("date","endTime").format(name=filed_name)
        self.sendKeys(end_loc,end)
        self.clickElement(readXml("date","packup").format(name=filed_name))


    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的日期输入数据'''
        loc =  readXml("date","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)