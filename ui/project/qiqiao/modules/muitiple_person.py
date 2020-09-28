from func.read_xml import readXml
from ui.common.driver import Driver
import time


class MultiplePerson(Driver):
    '''人员多选组件'''

    def searchData(self, filed_name, name, full_name):
        '''通过人员多选筛选页面数据'''
        loc = readXml("multiple_person", "search").format(name=filed_name)
        self.sendKeys(loc, name)
        self.clickElement(readXml("multiple_person", "personname").format(full_name))

    def sendValue(self, filed_name, *args):
        '''人员多选输入值'''
        loc = readXml("multiple_person", "sendValue").format(name=filed_name)
        self.clickElement(loc)
        for fullname in args:
            name=fullname[0]
            self.clickElement(readXml("multiple_person", "input").format(name="组织选择器搜索框"))
            self.sendKeys(readXml("multiple_person", "input").format(name="组织选择器搜索框"), name)
            time.sleep(0.5)
            self.clickElement(readXml("multiple_person", "fullname").format(name=filed_name,fullname=fullname))
        self.clickElement(readXml("multiple_person", "conf_btn").format(name=filed_name))


