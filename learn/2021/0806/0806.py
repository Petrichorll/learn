import re
import datetime
import numpy
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


f = open("C://Users/19144/Desktop/45.txt", "r", encoding="utf-8")

kkk = []
for sstr in f.readlines():
    h = re.findall("1\d:.+?\d\d\d", sstr)
    if(h):
        d1 = datetime.datetime.strptime(h[0], '%H:%M:%S.%f')
        kkk.append(d1)

i = 1

yyl = []

while(i < 100):
    d1 = (kkk[i]-kkk[i-1])
    westr = str(d1)
    ed = re.sub("0:0", "", westr)
    edf = float(ed)
    yyl.append(edf)

    # dst=d1.strftime('%H:%M:%S.%f')
    # print(dst)
    i = i+1

print(yyl)
# ukk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# i = 0
# while(i < 99):
#     j=0
#     while(j<12):
#         if(yyl[i]>0.5*j and yyl[i]<0.5*(j+1)):
#             ukk[j]=ukk[j]+1
#         j=j+1
#     i = i+1
ll = 0.5
mm = 0
ukk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# nkk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# i=0
# while(i<len(nkk)):
#     nkk[i]=ll*i+mm
#     i=i+1
i = 0
while(i < 99):
    j = 0
    while(j < 20):
        if(yyl[i] > ll*j+mm and yyl[i] < ll*(j+1)+mm):
            ukk[j] = ukk[j]+1
            break
        j = j+1
    i = i+1

print(ukk)
print(range(0, 20))
plt.bar(range(len(ukk)), ukk)
plt.show()
