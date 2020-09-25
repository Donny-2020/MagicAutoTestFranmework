from ui.common.driver import Driver
class Address(Driver):
    '''地址选择器组件'''
    def searchData(self,file_name,province,city,region):
        '''使用地址选择字段筛选页面数据'''
        loc = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div/div/span".format(name=file_name)
        self.clickElement(loc)
        province_loc = "xpath=>//div[@class='el-cascader-menus el-popper {0}']//span[text()='{1}']".format(file_name,province)
        city_loc = "xpath=>//div[@class='el-cascader-menus el-popper {0}']//span[text()='{1}']".format(file_name,city)
        region_loc = "xpath=>//div[@class='el-cascader-menus el-popper {0}']//span[text()='{1}']".format(file_name,region)
        self.clickElement(province_loc)
        self.clickElement(city_loc)
        self.clickElement(region_loc)
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")