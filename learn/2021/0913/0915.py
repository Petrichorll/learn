# import re,random
# from time import sleep
# account_choice = ["中国银行", "建设银行", "工商银行", "农业银行"]
tt=0
f = open(r"C:\Users\19144\Desktop\887.csv", "r", encoding="utf-8")
for sstr in f.readlines():
    if(sstr=="test\n" or sstr=="null\n"):
        continue
    a=eval(sstr)
    tt=tt+len(a)
print(tt)
# for sstr in f.readlines():
#     hh=re.sub("\n","",sstr)
#     tstr = random.choice(account_choice)
#     nstr=hh+","+tstr+"\n"
#     h.writelines(nstr)
    