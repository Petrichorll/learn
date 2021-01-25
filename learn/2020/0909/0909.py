# -*- coding: utf-8 -*-


import re
import base64

f = open("《最强蜗牛》iOS官方15.mht", "r", encoding="utf-8")
conut = 84000
i = 0
k = 0
yy = []
for str in f.readlines():
    #h = re.match('Content-Location.*dat', str)
    h = re.match('Content-Type:image/jpeg', str)
    if (h):
        print(h)
        print(str)
        k = k + 1

    if (k == 6):
        yy.append(str)
        i = 1

    if conut < 0:
        break
    conut = conut - 1

print(yy)
print(len(yy))
zz = []
for uu in range(4, len(yy)-2):
    zz.append(yy[uu])

print(zz)

data = b""
for str in zz:
    temp = base64.b64decode(str)
    data = data + temp

with open("c.gif", "wb") as f:
    f.write(data)










# r=f.readlines()
# print(r[999])
# print(r[1000])

# with open('avatar.jpg', 'rb') as f:
#     r = f.read()
#     print(r)
