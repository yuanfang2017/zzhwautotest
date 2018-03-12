# -*- coding: utf-8 -*-
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
_author_ = 'fannie'
_data_ = '2018/3/7 17:32'


def send_email(new_file):
    # f = open(new_file, 'rb')
    # mail_body = f.read()
    # f.close()
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 设置邮件的发送者和接收者
    email_sender = "automation-notification@hey900.com"
    email_sender_password = "Setup2017"
    smtp_sever = "smtp.exmail.qq.com"

    email_receiver = ["wangyuanfang@hey900.com"]
    email_cc = ["2216914706@qq.com"]
    subject = "Automation TestReport".format(now_time)
    # MIMEMultipart 这个类是多部分的邮件体
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 标题
    msg['Subject'] = subject

    # MIMEtext()用于定义邮件的正文
    # msg_file = MIMEText(new_file, 'html', 'utf-8')
    # msg_file['Content-Type'] = 'application/octet-stream'
    # msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'

    # msg.attach(msg_file)
    msg['From'] = email_sender
    msg['To'] = ",".join(email_receiver)
    msg['Cc'] = ",".join(email_cc)
    msg.preamble = 'MultiPart message.\n'

    fd = open(new_file, 'r')
    values = ''
    p_count = 0
    f_count = 0
    e_count = 0
    value = fd.readlines()
    for each in value:
        if "pass</a>" in each:
            p_count = p_count+1
        elif "td class='failCase'" in each:
            f_count = f_count+1
            values = values+each+"<br />"
        elif "td class='errorCase'" in each:
            e_count = e_count+1
            values = values+each + "<br />"
    a_count = p_count+f_count+e_count
    fd.close()


    html = """
            <head></head>
          <body>
                <h1>自动化测试报告<br /></h1>
                Dear ALL,<br />
                <br />
                以下是这次自动化测试结果: <br />
                执行测试用例总数（ALL） ：{0} <br />
                通过测试用例数（PASS）  ：{1} <br />
                <font color="#FF0000">失败测试用例数（FAIL）  ：{2}</font> <br />
                <font color="#FF0000">错误测试用例数（ERROR） ：{3}</font> <br />
                <br />
                失败测试用例列表：<br />
                {4}
                所有详细的测试结果: <a href="{5}">{6}</a><br />
                <br />
                <br />
                这是一封自动发送的邮件，并且不会回复任何邮件！请勿回复...<br />
                有任何问题请联系测试部，谢谢！<br />
                温馨提示：如果您看到的邮件是乱码，请将邮箱的查看编码格式设置为UTF-8，具体请参考不同邮箱客户端的设置。<br />
          </body>
        </html>
    """.format(a_count, p_count, f_count, e_count, values, "file:///"+os.path.abspath(new_file), os.path.abspath(new_file))
    html = MIMEText(html, 'html', _charset='utf-8')
    msg.attach(html)
    print os.path.abspath(new_file)
    smtp = smtplib.SMTP()
    smtp.connect(smtp_sever)
    smtp.starttls()
    smtp.login(email_sender, email_sender_password)
    smtp.sendmail(msg['From'], msg['Cc'], msg.as_string())
    smtp.quit()









