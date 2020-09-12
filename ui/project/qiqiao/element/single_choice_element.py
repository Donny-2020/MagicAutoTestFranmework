class SingleChoiceElement():
    def __init__(self):
        self.sendValueLoc = "xpath=>//div[@data-mark='{name}' and @class='el-form-item']//div/label[{index}]/span[@class='el-radio__input']"
        self.searchDataLoc = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input"
        self.dropDownLoc = "xpath=>//div[@data-mark='{name}' and @class='el-form-item']/div//input"
        self.subFormLoc = "xpath=>//div[@data-mark='子表弹层_{form}']//div[@data-mark='{feild}']//input"