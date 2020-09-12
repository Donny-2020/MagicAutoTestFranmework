from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.rich_text_element import RichTextElement

class RichText(Driver):

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToRichText(self,fild_name,value):
        '''富文本输入值'''
        loc = RichTextElement().sendValueLoc.format(name=fild_name)
        self.sendKeys(loc,value)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    # def searchDataByRichText(self,filed_name,value):
    #     '''使用时间字段筛选页面数据'''
    #     loc = RichTextElement().searchDataLoc.format(name=filed_name)
    #     self.sendKeys(loc,value)
    #     self.clickElement("//button[@data-mark='筛选条件搜索按钮']")
    #
    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueToRichTextInSubForm(self,sub_form,filed_name,value):
        '''子表单的时间输入数据'''
        loc =  RichTextElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)