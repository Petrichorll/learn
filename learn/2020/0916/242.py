# -*- coding: utf-8 -*-

import random
# print(random.randint(1, 1))
# print(4%2)

# i=0
# while (i < 24):
#     print(i)
#     i=i+1


# def writedata(xlsname, *args):
#     print(xlsname)
#     print(len(args))
#
#
# writedata(4,5,6,7)

# a=[11,12,13,14,15]
# q=a[1:3]
# print(q)
# print(id(a),id(q))


# def fun(x,y=3,n=4,z=5):
#     print(x)
#     print(y)
#     print(n)
#     print("=============")
#     name=[3,4,5,6,7,8]
#     name[4]=100
#     print(name)
#     return
#
# fun(2,12,z=7)

from datetime import datetime, timedelta


from dateutil.relativedelta import relativedelta


# 获得当前时间
# now_time = datetime.now()
# print(now_time, "当前时间")


def delay_time(years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    time_str = datetime.now()
    # if type(time_str) == str:
    #     time_str = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    ret = time_str + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)
    hh = str(ret)
    hh = hh[:-7]
    return hh


ret2 = delay_time(minutes=-1)
print(ret2)
