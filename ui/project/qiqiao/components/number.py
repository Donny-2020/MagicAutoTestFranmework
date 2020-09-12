from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.number_element import NumberElement

class Number(Driver):

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''数字组件输入值'''
        loc = NumberElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,value):
        '''使用数字字段筛选页面数据'''
        loc = NumberElement().searchDataLoc.format(name=filed_name)
        self.sendKeys(loc,value)


    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的数字输入数据'''
        loc =  NumberElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)