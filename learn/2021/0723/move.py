import os

fpath=r"C:\Users\19144\Desktop\result"

cc=1


for i,j,k in os.walk(fpath):
    print(len(k))