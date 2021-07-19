# -*- coding: utf-8 -*-

import re

file = "C:\\Users\\19144\\Desktop\\xs\\keai.txt"

f = open(file, 'r', encoding='utf-8')

t = "C:\\Users\\19144\\Desktop\\xs\\keai\\"
tn = "kaishi.txt"

for sstr in f.readlines():
    h = open(t + tn, 'a', encoding='utf-8')
    if (re.match("\d+.+", sstr)):
        print(sstr)
        tn = sstr.strip() + ".txt"
        h.close()
        h = open(t + tn, 'a', encoding='utf-8')
        h.writelines(sstr)
        h.close()
        continue
    h.writelines(sstr)
    h.close()
f.close()
