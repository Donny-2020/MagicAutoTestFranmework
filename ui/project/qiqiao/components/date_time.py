from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.date_time_element import DateTimeElement

class DateTime(Driver):

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToDateTime(self,fild_name,value):
        '''日期时间输入值'''
        loc = DateTimeElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchDataByDateTime(self,filed_name,value):
        '''使用日期时间字段筛选页面数据'''
        loc = DateTimeElement().searchDataLoc.format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement("//button[@data-mark='筛选条件搜索按钮']")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToDateTimeInSubForm(self,sub_form,filed_name,value):
        '''子表单的日期时间输入数据'''
        loc =  DateTimeElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)