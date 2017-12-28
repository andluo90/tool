# -*- coding: utf-8 -*-

from smtplib import SMTP_SSL,SMTPException
from email.header import Header
from email.mime.text import MIMEText


def rate(a=752.35,b=24,c=5.12,d=36.47):
    """
    等额本息实际利率计算
    :param a: 贷款总额
    :param b: 分期总数
    :param c: 每期手续费
    :param d: 每月还款本息
    """
    e = []
    g = 0
    for i in range(1,b+1):
        if i==1:
            f = c/a*100
            e.append((a,f))
        else:
            a = a-(d-c)
            f = c/a*100
            e.append((a,f))
        print(("第%d期实际贷款本金：%f，实际利率：%f" %(i,a,f)))
        g+=f
        if i in range(12,600,12):
            print("【第%d年实际年利率：%f】" %(i/12,g))


def 发送邮件(subject, text,to="1455234749@qq.com"):
    "send an email by QQ"

    mailInfo = {
        "from": "1455234749@qq.com",
        "to": to,
        "hostname": "smtp.qq.com",
        "username": "1455234749@qq.com",
        "password": "######",
        "mailsubject": subject,
    }

    try:
        smtp = SMTP_SSL(mailInfo["hostname"])
        # smtp.set_debuglevel(1)
        # smtp.ehlo(mailInfo["hostname"])
        smtp.login(mailInfo["username"], mailInfo["password"])

        msg = MIMEText(text, "plain", "UTF-8")
        msg["Subject"] = Header(mailInfo["mailsubject"], "UTF-8")
        msg["from"] = mailInfo["from"]
        msg["to"] = mailInfo["to"]
        smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())

        smtp.quit()
    except SMTPException:
        print('Send email exception')
    else:
        print("Send Success!!!")

def 简单工资计算(a=0000,b=196.01,c=106.50,d=0,e=22):
    "a:税前工资,b:社保扣款,C:公积金扣款,d:请假小时数,e:出勤天数"
    a1 = a
    h = round(a1/e/8,2)
    a = a - b - c-3500-h*d
	
    if 0 < a <= 1500:
        a = a * 0.03 - 0
    elif 1500 < a <= 4500:
        a = a * 0.1 - 105
    elif 4500 < a <= 9000:
        a = a * 0.2 - 555
    elif 9000 < a <=35000:
        a = a * 0.25 - 1005
    elif 35000 < a <= 55000:
        a = a * 0.3 - 2755
    elif 55000 < a <=80000:
        a = a * 0.35 - 5505
    elif 80000 < a:
        a = a * 0.45 - 13505
    print("税后工资: %0.2f" %(a1-round(a,2)-b-c-h*d))
    print("个人所得税: %0.2f" %a)
    if d:
        print("请假扣钱：%0.2f" %(h*d))
