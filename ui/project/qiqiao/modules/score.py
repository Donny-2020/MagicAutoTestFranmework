import time

from ui.common.driver import Driver
class Score(Driver):
    '''评分组件'''
    def searchData(self,filed_name,value):
        '''使用评分字段筛选页面数据'''
        loc = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input".format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement("xpath=>//div[@title='{name}']".format(name=value))
        self.clickElement("xpath=>//div[@data-mark='{name}']/label".format(name=filed_name))