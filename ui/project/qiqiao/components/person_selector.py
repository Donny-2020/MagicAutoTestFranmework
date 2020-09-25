from ui.common.driver import Driver
class PersonSelector(Driver):
    '''人员单选组件'''
    def searchData(self,filed_name,name,full_name):
        '''通过人员单选筛选页面数据'''
        loc = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input".format(name=filed_name)
        self.sendKeys(loc,name)
        self.clickElement("xpath=>//div[@title='{}' and @class='text_ellipsis']".format(full_name))