from ui.common.driver import Driver
from func.read_xml import readXml
class PersonSelector(Driver):
    '''人员单选组件'''
    def searchData(self,filed_name,name,full_name):
        '''通过人员单选筛选页面数据'''
        loc = readXml("person_selector","search").format(name=filed_name)
        self.sendKeys(loc,name)
        self.clickElement(readXml("person_selector","personname").format(full_name))