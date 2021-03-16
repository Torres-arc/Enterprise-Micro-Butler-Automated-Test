# coding=utf-8
import unittest
import time

from common.APIRequest import *
from common.HTMLTestRunner_cn import HTMLTestRunner
from generate import generate
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.log import log
from common.base_page import BasePage
from tkinter import *

os.chdir(sys.path[0])


# 发送测试邮件报告
def send_email(test_report, connect, sender, password, receiver, receiver2, receiver3, title, main, test_log=None):
    # 获取报告文件：'related'43行
    f = open(test_report, 'rb')
    f1 = open(test_log, 'rb')
    test_msg = f.read()
    test_msg1 = f1.read()
    subject = title
    body = '<p>' + main + '<p>'
    msgRoot = MIMEMultipart('related')
    # 邮件标题
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    # 邮件内容
    body = MIMEText(body, 'html', 'utf-8')  # 正文
    att = MIMEText(test_msg, 'base64', 'utf-8')  # 附件
    att1 = MIMEText(test_msg1, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "企微测试报告.html.html"))
    att1['Content-Type'] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "企微测试报告日志.xlsx"))
    msgRoot.attach(att)
    msgRoot.attach(att1)
    msgRoot.attach(body)

    smtp = smtplib.SMTP()
    smtp.connect(connect)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.sendmail(sender, receiver2, msgRoot.as_string())
    smtp.sendmail(sender, receiver3, msgRoot.as_string())


# 收集测试用例
def create_my_suit(dicts):
    my_suit = unittest.TestSuite()
    paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_cases'
    for i in dicts.keys():
        discover = unittest.defaultTestLoader.discover(paths, pattern=(i + '.py'), top_level_dir=None)
        for test_suit in discover:
            for test_cases in test_suit:
                for a in test_cases:
                    if (str(a).split(' '))[0] in dicts[i]:
                        msg = (str(a).split(' '))[1]
                        module = ('.'.join((msg.split('.'))[0:2]))[1:]
                        Class = ((msg.split('.'))[2])[:-1]
                        my_suit.addTest(unittest.TestLoader().loadTestsFromName(
                            '{}.{}.{}'.format(module, Class, (str(a).split(' '))[0])))

    return my_suit


def robotMsgSender(result):
    passed = result.success_count
    error = result.error_count
    fail = result.failure_count
    skip = result.skip_count
    total = int(passed) + int(error) + int(fail) + int(skip)
    percent = '{:.2%}'.format(int(passed) / int(total))
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6b262540-2bd6-4d99-aa7b-0ad3b47a6534'
    headers = {"Content-Type": "text/plain"}
    text1 = "企微自动化测试结果摘要如下"
    text0 = ">运行版本:<font color=\"comment\"> {}</font> 目标环境:<font color=\"comment\"> {}</font>".format('3.1',
                                                                                                      'www')
    text2 = ">时间:<font color=\"comment\"> {}</font>".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    text3 = ">总测试用例数:<font color=\"comment\"> {}例</font>".format(total)
    text4 = ">用例通过数:<font color=\"comment\"> {}例</font>".format(passed)
    text5 = ">用例错误数:<font color=\"comment\"> {}例</font>".format(error)
    text6 = ">用例失败数:<font color=\"comment\"> {}例</font>".format(fail)
    text7 = ">用例跳过数:<font color=\"comment\"> {}例</font>".format(skip)
    text8 = ">用例通过率:<font color=\"comment\"> {}</font>".format(percent)
    tlist = [text1, text0, text2, text3, text4, text5, text6, text7, text8]
    content = '\n'.join(tlist)
    content1 = "企微自动化测试已完成，请前往邮箱查看结果"
    send_values1 = {
        "msgtype": "text",
        "text": {
            "content": content1,
            "mentioned_mobile_list": ["18951576962", "17135107435", "18068267173"]
        },
    }
    send_values = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        },
    }
    requests.post(url=send_url, headers=headers, json=send_values1)
    requests.post(url=send_url, headers=headers, json=send_values)


def start(dicts, status):
    log().info('Start')
    if status == 0:
        mysuit = create_my_suit(dicts)
    else:
        mysuit = dicts

    print('my', mysuit)
    runer = HTMLTestRunner(title="企微3.1测试报告", stream=open("企微测试报告.html", "wb"),
                           verbosity=2, retry=2, save_last_try=True)
    result = runer.run(mysuit)
    # BeautifulReport(mysuit).report(filename='测试报告', description='企微3.0web测试', report_dir='')
    log().info('Finish')
    # robotMsgSender(result)
    # path = os.path.dirname(os.path.abspath('企微测试报告.html') + '\\企微测试报告.html')
    # SwitchToExcel().createExcel()
    # dir = os.path.abspath(__file__) + '\\Log'
    # file_list = os.listdir('.')
    # for file in file_list:
    #     if file.startswith('企微自动化测试日志'):
    #         os.remove('企微自动化测试日志.xlsx')
    #     if file.startswith('工作簿'):
    #         src = os.path.join(os.path.abspath(os.path.dirname(__file__)), file)
    #         os.rename(src, '企微自动化测试日志.xlsx')
    # path1 = (os.path.dirname(os.path.abspath(__file__)) + '\\企微自动化测试日志.xlsx')
    # print(path1)
    # send_email(test_report=path,
    #            connect='smtp.yunyou.top',
    #            sender='yunye@wshoto.com',
    #            password='WS123321',
    #            receiver='yunshu@wshoto.com',
    #            receiver2='yunhan@wshoto.com',
    #            receiver3='yunan@wshoto.com',
    #            title='企微测试报告.html',
    #            main='发送测试邮件，报告查收附件',
    #            # test_log=path1
    #            )
    # generate()



