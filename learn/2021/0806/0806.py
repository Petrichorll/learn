import re
import datetime
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
ukk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while(i < 99):
    j=0
    while(j<12):
        if(yyl[i]>0.5*j and yyl[i]<0.5*(j+1)):
            ukk[j]=ukk[j]+1
        j=j+1
    i = i+1
print(ukk)


plt.bar(range(len(yyl)), yyl)
plt.show()
