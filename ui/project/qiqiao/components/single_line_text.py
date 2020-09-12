from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.single_line_text_element import SingleLineTextElement

class SingleLineText(Driver):

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,value):
        '''单行文本输入值'''
        loc = SingleLineTextElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,value):
        '''使用单行文本字段筛选页面数据'''
        loc = SingleLineTextElement().searchDataLoc.format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement("//button[@data-mark='筛选条件搜索按钮']")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的单行文本输入数据'''
        loc =  SingleLineTextElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)
