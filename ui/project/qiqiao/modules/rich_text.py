from ui.common.driver import Driver
from func.read_xml import readXml

class RichText(Driver):

    def sendValue(self,value):
        '''富文本输入值'''
        self.switchToFrame("xpath=>//iframe[@class='tox-edit-area__iframe']")
        loc="xpath=>//body[@id='tinymce']/p"
        self.sendKeys(loc,value)
        self.switchFrameOut()