# -*- coding: utf-8 -*-

from smtplib import SMTP_SSL,SMTPException
from email.header import Header
from email.mime.text import MIMEText


def 分期实际利率(a=752.35,b=24,c=5.12,d=36.47):
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
        print(("第%d期实际贷款本金：%f，实际利率：%0.2f" %(i,a,f)))
        g+=f
    print("平均每期利率： %0.2f" %(g/b))
    print("平均年利率： %0.2f" %(g/b*12))

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
    "a:税前工资,b:社保扣款,C:公积金扣款,d:请假小时数,e:当月应出勤天数"
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


def 灯光模拟考试():
    "清远灯光模拟考试"
    import random
    a = [['路边临时停车','小灯、报警灯'],['夜间在没有路灯、照明不良的条件下行驶','远光灯'],['夜间超越前方车辆','双闪灯'],['夜间通过拱桥、人行车道','双闪灯'],['夜间在照明良好的道路上行驶','近光灯'],['夜间与机动车会车','近光灯'],['夜间通过没有交通信号灯控制的路口','双闪灯'],['夜间路口左转弯','左转向灯'],['夜间路口右转弯','右转向灯'],['夜间路口直行','近光灯'],['夜间通过坡路、拱桥','双闪灯'],['夜间通过急弯、拱桥','双闪灯'],['夜间发生故障又难以移动','小灯、报警灯']]
    
    for i in range(len(a)):
        b = random.choice(a)
        print(b[0])
        c  = input('')
        print(b[1])
        print('=======\n\n')
        if c == 'q':
            print('done...')
            return
        a.remove(b)
    else:
        print('Over...')
