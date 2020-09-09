class LoginElement():
    def __init__(self):
        self.accountLoginLoc = "id=>account_login" #账号登录元素标识
        self.sendUsernameLoc = "id=>gerenban_username" #输入用户名元素标识
        self.sendPasswordLoc = "id=>gerenban_pass" #输入密码元素标识
        self.submitLoc = "id=>btn_login" #登录按钮元素标识

class RuntimeElement():
    def __init__(self):
        self.clickAppLoc = "xpath=>//a[@data-mark='header_menu_应用']" #应用首页元素标识
        self.appLoc = "xpath=>//div[@data-mark='{app}']"    #点击应用元素标识

        self.clickLeftMenu = "xpath=>//span[@title='{menu}']/.." #左侧菜单元素标识
        self.clickTitleButtonLoc = "xpath=>//div[@data-mark='{button}']/button" #表头按钮元素标识
        self.clickButtonInFormLoc = "xpath=>//span[@data-mark='{button}_{row}' and @class='normal']" #表行按钮元素标识