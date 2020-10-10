import os
import time

# from func.read_yaml import readYaml
# from ui.project import qiqiao
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
# url = readYaml("prod.yaml", "prod", "pc_business")
# usename = readYaml("prod.yaml", "prod", "username")
# password = readYaml("prod.yaml", "prod", "password")
# # cls.driver = webdriver.Chrome(executable_path="D:\Projects\MagicAutoTestFranmework\\ui\driver\chromedriver.exe")
# qiqiao.public(driver).loginRuntime(url, usename, password)
# # # qiqiao.public(driver).openAppPage()
# # # qiqiao.public(driver).clickApp("自动化应用（勿删）")
# # qiqiao.public(driver).clickLeftMenu("主表")
# # qiqiao.public(driver).clickButtonInTitle("添加")
# # qiqiao.singleLineText(driver).sendValue("单行文本","自动化测试")
# # qiqiao.multilineText(driver).sendValue("多行文本","多行文本测试")
# # qiqiao.number(driver).sendValue("数字",12)
# # qiqiao.singleChoice(driver).sendValue("单项选择",1)
# # qiqiao.singleChoice(driver).dropDown("单项下拉","北京")
# # qiqiao.multipleChoice(driver).checked("多项选择",1,2)
# # qiqiao.multipleChoice(driver).dropDown("多项下拉","宝马X3","宝马X5","奔驰S600","奥迪A6")
# # qiqiao.date(driver).sendValue("日期","2020-09-28")
# # qiqiao.time(driver).sendValue("时间","07:15")
# # qiqiao.dateTime(driver).sendValue("日期时间","2020-09-28 00:00")
# # qiqiao.personSelector(driver).sendValue("人员单选","刁惠云")
# # qiqiao.multiplePerson(driver).sendValue("人员多选","刁惠云","罗琳月")
# qiqiao.public(driver).clickButtonInForm("详情",1)
# # time.sleep(5)
# qiqiao.richText(driver).sendValue("测试")

# file = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time()))+".png"
# tt = file.split("_")
# up_time = tt[0]+" "+tt[1]
# print(up_time)
# print("2020-09-30 17:21")

# os.system('taskkill /f /im %s' % 'chromedriver.exe')
path_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path_file)