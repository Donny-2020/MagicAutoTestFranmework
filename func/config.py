from func.read_yaml import readYaml
class login():
    def __init__(self):
        dic = readYaml("qiqiao.yaml")
        for key in dic:
            if dic[key]['turn']==True:
                self.url = dic[key]['url']
                self.username = dic[key]['username']
                self.password = dic[key]['password']
            else:
                continue

class report():
    def __init__(self,name,key):
        self.case_path=readYaml("report.yaml",name,key,"case_path")
        self.report_file_name= readYaml("report.yaml",name,key,"report_file_name")
        self.log_file_name= readYaml("report.yaml",name,key,"log_file_name")
        self.output_path= readYaml("report.yaml",name,key,"output_path")
        self.title= readYaml("report.yaml",name,key,"title")
        self.description= readYaml("report.yaml",name,key,"description")
        self.thread_count= readYaml("report.yaml",name,key,"thread_count")
        self.thread_start_wait= readYaml("report.yaml",name,key,"thread_start_wait")
        self.sequential_execution= readYaml("report.yaml",name,key,"sequential_execution")
        self.lang= readYaml("report.yaml",name,key,"lang")