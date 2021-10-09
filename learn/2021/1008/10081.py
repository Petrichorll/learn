import requests
import re
from time import sleep

i = 4467
while(1):
    i = i+1
    print(i)
    papa = "https://xslist.org/zh/model/{}.html".format(i)
    reb = requests.get(papa)
    if(reb.status_code == 404):
        continue
    rstr = reb.content.decode()
    if(re.findall("ailbre", rstr)):
        tt = re.findall(
            "..........................................ailbre", rstr)
        op = 0
        while(op < len(tt)):
            fh = tt[op]
            foo = open(r"C:\Users/19144/Desktop/02021.txt", "a")
            foo.writelines(str(i)+","+fh+"\n")
            foo.close()
            op = op+1
    elif(re.findall("Escaped Prisoner", rstr)):
        tt = re.findall(
            "..........................................risoner", rstr)
        op = 0
        while(op < len(tt)):
            fh = tt[op]
            foo = open(r"C:\Users/19144/Desktop/02021.txt", "a")
            foo.writelines(str(i)+","+fh+"\n")
            foo.close()
            op=op+1
    else:
        pass
