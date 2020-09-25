class TimeElement():
    def __init__(self):
        self.sendValueLoc = "xpath=>//div[@data-mark='{name}' and @class='el-form-item is-required']/div//input"
        self.searchDataLocStart = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input[1]"
        self.searchDataLocEnd = "xpath=>//div[@data-mark='{name}' and @searhstatus='true']/div//input[2]"
        self.subFormLoc = "xpath=>//div[@data-mark='子表弹层_{form}']//div[@data-mark='{feild}']//input"