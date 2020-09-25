import time

from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.multiple_choice_element import MultipleChoiceElement

class MultipleChoice(Driver):

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''多项选择输入值'''
        loc = MultipleChoiceElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,value):
        '''使用多项选择字段筛选页面数据'''
        loc = MultipleChoiceElement().searchDataLoc.format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement("xpath=>//div[@title='{name}']".format(name=value))
        self.clickElement("xpath=>//div[@data-mark='{name}']/label".format(name=filed_name))
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的多项选择输入数据'''
        loc =  MultipleChoiceElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)