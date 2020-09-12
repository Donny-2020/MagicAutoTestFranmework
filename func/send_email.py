import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to,path):
    html_file = open(path,"rb")
    data=html_file.read()
    sender_mail = '981772991@qq.com'
    sender_pass = 'uchyilsslfvmbfhf'

    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = 'Donny<981772991@qq.com>'
    msg_root['To'] = "785182159@qq.com"
    # 邮件的主题，显示在接收邮件的预览页面
    subject = '自动化测试报告'
    msg_root['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = data
    text_sub = MIMEText(text_info, 'html', 'utf-8')
    msg_root.attach(text_sub)

    # 构造附件
    txt_file = open(r'{}'.format(path), 'rb').read()
    txt = MIMEText(txt_file, 'base64', 'utf-8')
    txt["Content-Type"] = 'application/octet-stream'
    txt.add_header('Content-Disposition', 'attachment',filename="UI测试报告.html")
    msg_root.attach(txt)

    try:
        sftp_obj =smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


if __name__ == '__main__':

    to = '785182159@qq.com'
    send_email_by_qq(to)