import time

from ui.common.driver import Driver
from retrying import retry
from ui.project.qiqiao.element.single_choice_element import SingleChoiceElement

class SingleChoice(Driver):

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValue(self,fild_name,num):
        '''单项选择组件输入值'''
        loc = SingleChoiceElement().sendValueLoc .format(name=fild_name,index=num)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def dropDown(self, filed_name,value):
        '''下拉类型输入值'''
        loc = SingleChoiceElement().dropDownLoc.format(name=filed_name)
        self.clickElement(loc)
        self.clickElement("xpath=>//li[@data-mark='{name}']".format(name=value))

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def searchData(self,filed_name,value):
        '''使用单项选择字段筛选页面数据'''
        loc = SingleChoiceElement().searchDataLoc.format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement("xpath=>//div[@title='{name}']".format(name=value))
        self.clickElement("xpath=>//div[@data-mark='{name}']/label".format(name=filed_name))


    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的单项选择输入数据'''
        loc =  SingleChoiceElement().subFormLoc.format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)