import re


f1=open("C://Users/19144/Desktop/YY.txt","r",encoding="utf-8")
f2=open("C://Users/19144/Desktop/YY1.txt","r",encoding="utf-8")


fl1=[]
fl2=[]
for sstr in f1.readlines():
    fl1.append(sstr)
for sstr in f2.readlines():
    for rstr in fl1:
        if(re.findall(sstr.strip(),rstr)):
            fl2.append(rstr)


h=open("C://Users/19144/Desktop/YY1.txt","w",encoding="utf-8")
for sstr in fl2:
    h.writelines(sstr)
h.close()