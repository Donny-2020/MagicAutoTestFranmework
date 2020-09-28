from ui.common.driver import Driver
from func.read_xml import readXml
from retrying import retry
class SubForm(Driver):
    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickAddOneData(self,form_name):
        '''点击子表单，添加一行按钮'''
        loc = readXml("subform","add_one_line").format(name=form_name)
        # loc = "xpath=>//div[@data-mark='{name}']//span[text()='添加一行']".format(name=form_name)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickAddButton(self,form_name):
        '''点击子表单，添加按钮'''
        loc = readXml("subform","add_btn").format(name=form_name)
        # loc = "xpath=>//div[@data-mark='{name}']//span[text()='添加']".format(name=form_name)
        self.clickElement(loc)

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def clickSaveButton(self,subform,button_name):
        '''点击子表单中的按钮'''
        loc = readXml("subform","save_btn").format(sub=subform,button=button_name)
        # loc = "xpath=>//div[@data-mark='子表弹层_{sub}']//span[text()='{button}']".format(sub=subform,button=button_name)
        self.clickElement(loc)


    def clickEditButton(self):
        '''点击子表单的编辑按钮'''
        # loc ="xpath=>//tr[@class='el-table__row row_子表单_0']/td[1]"
        self.moveToElement(readXml("subform","drop"))
        # loc2="xpath=>//tr[@class='el-table__row row_子表单_0 hover-row']//span[@class='iconfont iconbianji primary_color']"
        element = self.getElement(readXml("subform","edit_btn"))
        self.js("arguments[0].click()",element)

    def clickDeleteButton(self):
        '''点击子表单的删除按钮'''
        # loc ="xpath=>//tr[@class='el-table__row row_子表单_0']/td[1]"
        self.moveToElement(readXml("subform","drop"))
        # loc2="xpath=>//tr[@class='el-table__row row_子表单_0 hover-row']//span[@class='iconfont iconyewusheji-shanchu primary_color']"
        element = self.getElement(readXml("subform","delete_btn"))
        self.js("arguments[0].click()",element)