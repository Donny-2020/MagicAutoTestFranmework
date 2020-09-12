from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.date_element import DateElement

class Date(Driver):

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToDate(self,fild_name,value):
        '''日期输入值'''
        loc = DateElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchDataByDate(self,filed_name,value):
        '''使用日期字段筛选页面数据'''
        loc = DateElement().searchDataLoc.format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement("//button[@data-mark='筛选条件搜索按钮']")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToDateInSubForm(self,sub_form,filed_name,value):
        '''子表单的日期输入数据'''
        loc =  DateElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)