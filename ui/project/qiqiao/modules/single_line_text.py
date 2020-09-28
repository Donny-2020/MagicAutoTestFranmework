from ui.common.driver import Driver
from func.read_xml import readXml

class SingleLineText(Driver):

    def sendValue(self,fild_name,value):
        '''单行文本输入值'''
        loc = readXml("single_line_text","sendValue").format(name=fild_name)
        self.sendKeys(loc,value)

    def searchData(self,filed_name,value):
        '''使用单行文本字段筛选页面数据'''
        loc = readXml("single_line_text","search").format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")

    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的单行文本输入数据'''
        loc = readXml("single_line_text","subForm")
        self.sendKeys(loc,value)


