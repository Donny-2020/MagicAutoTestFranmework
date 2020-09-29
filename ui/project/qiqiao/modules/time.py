from ui.common.driver import Driver
from func.read_xml import readXml

class Time(Driver):

    def sendValue(self,fild_name,value):
        '''时间输入值'''
        loc = readXml("time","sendValue").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(readXml("time","label").format(name=fild_name))

    def searchData(self,filed_name,start_time,end_time):
        '''使用时间字段筛选页面数据'''
        start_loc = readXml("time","startTime").format(name=filed_name)
        self.sendKeys(start_loc,start_time)
        end_loc = readXml("time","endTime").format(name=filed_name)
        self.sendKeys(end_loc,end_time)
        self.clickElement(readXml("time","packup").format(name=filed_name))


    def sendValueToTimeInSubForm(self,sub_form,filed_name,value):
        '''子表单的时间输入数据'''
        loc =  readXml("time","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)