from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.date_element import DateElement

class Date(Driver):

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''日期输入值'''
        loc = DateElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,start,end):
        '''使用日期字段筛选页面数据'''
        start_loc = DateElement().searchDataLocStart.format(name=filed_name)
        self.sendKeys(start_loc,start)
        end_loc = DateElement().searchDataLocEnd.format(name=filed_name)
        self.sendKeys(end_loc,end)
        self.clickElement("xpath=>//div[@data-mark='{name}' and @searhstatus='true']/label".format(name=filed_name))


    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的日期输入数据'''
        loc =  DateElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)