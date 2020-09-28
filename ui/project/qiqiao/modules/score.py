import time
from func.read_xml import readXml
from ui.common.driver import Driver
class Score(Driver):
    '''评分组件'''
    def searchData(self,filed_name,value):
        '''使用评分字段筛选页面数据'''
        loc = readXml("score","search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(readXml("score","scorenumber").format(name=value))
        self.clickElement(readXml("score","packup").format(name=filed_name))