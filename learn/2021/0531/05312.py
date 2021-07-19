# -*- coding: utf-8 -*-
import re

f=open("333.txt","r")

for sstr in f.readlines():
    sstr1=sstr.replace("\n","")
    slist= re.split(",",sstr1)
    # if(slist[2]=="02" and slist[3]=="07" and slist[4]=="12"):
    #     print(sstr1)

    if(slist[7]=="05" and slist[8]=="08"):
        print(sstr1)