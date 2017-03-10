# -*- coding: utf-8 -*-

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

rate()
