import requests,re

from requests.models import DecodeError

i=37
while(i<1000):
    i=i+1
    
    fh="SSPD-{0:03d}".format(i)
    print(fh)

    reb = requests.get("https://xslist.org/search?query={}&lg=en".format(fh))
    rstr = reb.content.decode()

    h=re.findall("href=\"h.+l\">",rstr)
    if(h):
        rrstr=h[0]
        rrstr=re.sub("href=\"","",rrstr)
        rrstr=re.sub("\">","",rrstr)
        

        reb = requests.get(rrstr)
        rstr = reb.content.decode() 
        

        e=re.findall("{}.+?\d\d".format(fh),rstr)
        if(e):
            if(re.findall("ailbre",e[0]) or re.findall("risoner",e[0])):
                print(fh)
                foo=open(r"C:\Users/19144/Desktop/02020.txt","a")
                foo.writelines(fh+"\n")
                foo.close()
