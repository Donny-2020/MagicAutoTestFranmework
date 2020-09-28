from ui.common.driver import Driver
from func.read_xml import readXml
import time
class PersonSelector(Driver):
    '''人员单选组件'''
    def searchData(self,filed_name,full_name):
        '''通过人员单选筛选页面数据'''
        name = full_name[0]
        loc = readXml("person_selector","search").format(name=filed_name)
        self.sendKeys(loc,name)
        self.clickElement(readXml("person_selector","personname").format(full_name))

    def sendValue(self,filed_name,full_name):
        '''人员单选输入值'''
        loc = readXml("person_selector","sendValue").format(name=filed_name)
        self.clickElement(loc)
        name=full_name[0]
        self.sendKeys(readXml("person_selector","input").format(name="组织选择器搜索框"),name)
        time.sleep(1)
        self.clickElement(readXml("person_selector", "fullname").format(name=filed_name, fullname=full_name))
        self.clickElement(readXml("person_selector","conf_btn").format(name=filed_name))