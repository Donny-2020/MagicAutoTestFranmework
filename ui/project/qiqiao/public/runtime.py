
from ui.project.qiqiao.element.public import LoginElement,RuntimeElement
from retrying import retry
from ui.project.qiqiao.components.single_line_text import SingleLineText
from ui.project.qiqiao.components.sub_form import SubForm



class Runtime(SingleLineText,SubForm):
    loc_obj = LoginElement()
    runtime_loc_obj = RuntimeElement()


    # @retry(stop_max_attempt_number=3,wait_fixed=2)
    def loginRuntime(self,username,password):
        '''登录PC端运行平台'''

        self.openUrl("https://tqy.do1.net.cn/qa-runtime")
        self.clickElement(self.loc_obj.accountLoginLoc)
        self.sendKeys(self.loc_obj.sendUsernameLoc,username)
        self.sendKeys(self.loc_obj.sendPasswordLoc,password)
        self.clickElement(self.loc_obj.submitLoc)

    # @retry(stop_max_attempt_number=3, wait_fixed=2)
    def openAppPage(self):
        '''打开应用页面'''
        self.clickElement(self.runtime_loc_obj.clickAppLoc)

    # @retry(stop_max_attempt_number=3, wait_fixed=2)
    def clickApp(self,appname):
        '''根据应用名称，打开应用'''
        loc = self.runtime_loc_obj.appLoc.format(app=appname)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=2)
    def clickLeftMenu(self,menu_name):
        '''根据菜单名称，点击左侧菜单'''
        loc = self.runtime_loc_obj.clickLeftMenu.format(menu=menu_name)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=2)
    def clickButtonInTitle(self,button_name):
        '''根据按钮名称，点击表头按钮'''
        loc = self.runtime_loc_obj.clickTitleButtonLoc.format(button=button_name)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=2)
    def clickButtonInForm(self,button_name,row_num):
        '''点击表单数据行，操作区按钮'''
        loc = self.runtime_loc_obj.clickButtonInFormLoc.format(button=button_name,row=row_num)
        self.getElements(loc)[2].click()

