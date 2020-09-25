from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.time_element import TimeElement

class Time(Driver):

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''时间输入值'''
        loc = TimeElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,start_time,end_time):
        '''使用时间字段筛选页面数据'''
        start_loc = TimeElement().searchDataLocStart.format(name=filed_name)
        self.sendKeys(start_loc,start_time)
        end_loc = TimeElement().searchDataLocEnd.format(name=filed_name)
        self.sendKeys(end_loc,end_time)
        self.clickElement("xpath=>//div[@data-mark='{name}']/label".format(name=filed_name))
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToTimeInSubForm(self,sub_form,filed_name,value):
        '''子表单的时间输入数据'''
        loc =  TimeElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)