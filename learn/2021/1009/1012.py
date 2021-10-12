import re
f=open("C://Users/19144/Desktop/ID.txt","r")
h=open("C://Users/19144/Desktop/messageids1012.txt","r")

hl=[]
fl=[]
for sstr in f.readlines():
    sstr=sstr.strip()
    fl.append(sstr)

for sstr in h.readlines():
    sstr=sstr.strip()
    r=re.sub("\| ","",sstr)
    sstr=re.sub(" \|","",r)
    hl.append(sstr)
count=0

uu=open("C://Users/19144/Desktop/ID1.txt","w")

for sstr in hl:
    if sstr not in fl:
        uu.writelines(sstr+"\n")
        count=count+1

uu.writelines("==================\n")
print(count)

for sstr in fl:
    if sstr not in hl:
        uu.writelines(sstr+"\n")
        count=count+1

print(count)