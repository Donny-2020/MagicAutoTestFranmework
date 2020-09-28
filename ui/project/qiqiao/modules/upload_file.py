import os
from ui.common.driver import Driver
from func.read_xml import readXml
class UploadFile(Driver):
    '''文件上传组件'''

    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def uploadFile(self,filed_name,file):
        '''上传文件'''
        loc=readXml("upload_file","sendValue").format(name=filed_name)
        # loc="xpath=>//div[@data-mark='{name}']//div[@class='canDrag_wrapper']".format(name=filed_name)
        self.clickElement(loc)
        path = "D:\Projects\MagicAutoTestFranmework\\ui\data\img\{file_name}".format(file_name=file)
        os.system("D:\Projects\MagicAutoTestFranmework\\ui\data\exe\\uploadpic.exe %s"%path)