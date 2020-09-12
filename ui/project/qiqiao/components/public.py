from ui.project.qiqiao.element.public_element import LoginElement,RuntimeElement
from retrying import retry
from ui.common.driver import Driver
from func.config import login

class Public(Driver):
    loc_obj = LoginElement()
    runtime_loc_obj = RuntimeElement()


    @retry(stop_max_attempt_number=3,wait_fixed=3000)
    def loginRuntime(self):
        '''登录PC端运行平台'''

        self.openUrl(login().url)
        self.clickElement(self.loc_obj.accountLoginLoc)
        self.sendKeys(self.loc_obj.sendUsernameLoc,login().username)
        self.sendKeys(self.loc_obj.sendPasswordLoc,login().password)
        self.clickElement(self.loc_obj.submitLoc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def openAppPage(self):
        '''打开应用页面'''
        self.clickElement(self.runtime_loc_obj.clickAppLoc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickApp(self,appname):
        '''根据应用名称，打开应用'''
        loc = self.runtime_loc_obj.appLoc.format(app=appname)
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickLeftMenu(self,menu_name):
        '''根据菜单名称，点击左侧菜单'''
        loc = self.runtime_loc_obj.clickLeftMenu.format(menu=menu_name)
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickButtonInTitle(self,button_name):
        '''根据按钮名称，点击表头按钮'''
        loc = self.runtime_loc_obj.clickTitleButtonLoc.format(button=button_name)
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickButtonInForm(self,button_name,row_num):
        '''点击表单数据行，操作区按钮'''
        loc = self.runtime_loc_obj.clickButtonInFormLoc.format(button=button_name,row=row_num)
        self.getElements(loc)[2].click()

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickSearchBtn(self):
        '''点击搜索按钮'''
        loc ="xpath=>//button[@data-mark='筛选条件搜索按钮']"
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickResetBtn(self):
        '''点击重置按钮'''
        loc = "xpath=>//button[@data-mark='筛选条件重置按钮']"
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickExpand(self):
        '''点击展开按钮'''
        loc = "xpath=>//span[@class='expand']"
        self.clickElement(loc)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def openProcessPage(self):
        '''点击流程页面'''
        loc = "xpath=>//a[@data-mark='header_menu_流程']"
        self.clickElement(loc)


    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def openProcess(self,name):
        '''点击流程页面'''
        loc = "xpath=>//p[@title='{}']/..".format(name)
        self.clickElement(loc)