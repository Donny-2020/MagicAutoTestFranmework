from ui.common.driver import Driver
class DepartSelector(Driver):
    '''部门单选'''
    def searchData(self,file_name,search,full_name):
        '''使用部门单选字段筛选页面数据'''
        loc = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input".format(name=file_name)
        self.sendKeys(loc,search)
        self.clickElement("xpath=>//div[@title='{}' and @class='text_ellipsis']".format(full_name))
