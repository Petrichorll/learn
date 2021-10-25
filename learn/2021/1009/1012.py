# import re
# f=open("C://Users/19144/Desktop/ID.txt","r")
# h=open("C://Users/19144/Desktop/messageids1012.txt","r")

# hl=[]
# fl=[]
# for sstr in f.readlines():
#     sstr=sstr.strip()
#     fl.append(sstr)

# for sstr in h.readlines():
#     sstr=sstr.strip()
#     r=re.sub("\| ","",sstr)
#     sstr=re.sub(" \|","",r)
#     hl.append(sstr)
# count=0

# uu=open("C://Users/19144/Desktop/ID1.txt","w")

# for sstr in hl:
#     if sstr not in fl:
#         uu.writelines(sstr+"\n")
#         count=count+1

# uu.writelines("==================\n")
# print(count)

# for sstr in fl:
#     if sstr not in hl:
#         uu.writelines(sstr+"\n")
#         count=count+1

# print(count)


a1="{\"requestId\":\"${iid}0${__time(,)}\",\"data\":["
a2="{\"id\":\"${__time(,)}"
a22="${iid}\",\"msg\":\"${mmsg}饭"
a222="\",\"from\":\"壹通道\",\"type\":\"全局\",\"patt\":null,\"account\":\"${acc}\"},"
a3="]}"
ret=a1
i=0
while(i<100):
    aa="{0:02d}".format(i)
    ret=ret+a2+aa+a22+aa+a222
    i=i+1

print(ret)
f=open("C://Users/19144/Desktop/4657.txt","w")
f.writelines(ret)