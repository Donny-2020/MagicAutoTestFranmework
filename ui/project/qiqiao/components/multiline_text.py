from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.multiline_text_element import MultilineTextElement

class MultilineText(Driver):
    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''多行文本输入值'''
        loc = MultilineTextElement().sendValueLoc.format(name=fild_name)
        self.clear(loc)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,value):
        '''使用多行文本字段筛选页面数据'''
        loc = MultilineTextElement().searchDataLoc.format(name=filed_name)
        self.clear(loc)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的多行文本输入数据'''
        loc =  MultilineTextElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)
