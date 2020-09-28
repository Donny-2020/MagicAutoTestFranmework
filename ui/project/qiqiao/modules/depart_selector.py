from ui.common.driver import Driver
from func.read_xml import readXml
class DepartSelector(Driver):
    '''部门单选'''
    def searchData(self,file_name,search,full_name):
        '''使用部门单选字段筛选页面数据'''
        loc = readXml("depart_selector","search").format(name=file_name)
        self.sendKeys(loc,search)
        self.clickElement(readXml("depart_selector","departname").format(full_name))
