import HTMLReport,unittest
import os,time
from func.send_email import send_email_by_qq

time_now = time.strftime("%Y-%m-%d", time.localtime())
path_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = path_file+"\\report\\"+time_now
file_path = path_file+"\\report\\"+time_now+"\\UI测试报告.html"
case_path = path_file+"\\cases"
if not os.path.exists(path):
    os.makedirs(path)
if os.path.exists(path):
    pass
discover = unittest.defaultTestLoader.discover(case_path, pattern='test_number.py', top_level_dir=None)
if __name__=="__main__":
    runner = HTMLReport.TestRunner(
                     report_file_name="UI自动化测试报告",
                     log_file_name="日志文件",
                     output_path=path ,
                     title= "ui测试报告",
                     description= "七巧自动化回归测试",
                     thread_count=3,
                     thread_start_wait= 0,
                     sequential_execution=False,
                     lang="cn"
    )
    runner.run(discover)
    # send_email_by_qq("785182159@qq.com",file_path)