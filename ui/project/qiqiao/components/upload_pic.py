from ui.common.driver import Driver
from retrying import retry
import os
class UploadPic(Driver):
    '''上传图片组件'''
    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def uploadPicture(self,filed_name,file_name):
        loc = "xpath=>//div[@data-mark='{name}']/div/div/div/div[@class='el-upload el-upload--picture-card']".format(name=filed_name)
        self.clickElement(loc)
        path = "D:\Projects\MagicAutoTestFranmework\\ui\data\img\{file_name}".format(file_name=file_name)
        os.system("D:\Projects\MagicAutoTestFranmework\\ui\data\exe\\uploadpic.exe %s"%path)
