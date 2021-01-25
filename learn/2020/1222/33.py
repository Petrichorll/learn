# -*- coding: utf-8 -*-
import re


def xiugai():
    fpath = "C:\\Users\\19144\\Desktop\\xs\\明海风云.txt"
    fpath1 = "C:\\Users\\19144\\Desktop\\xs\\明海风云1.txt"

    f = open(fpath, 'r')
    h = open(fpath1, 'a')
    i = 1
    for sstr in f.readlines():
        if (re.findall("###.+###", sstr)):
            hh = re.split("###", sstr)
            ll = re.split("\d+", hh[1])
            if (len(ll) == 1):
                jj = ' 无题'
            elif (ll[1] == ''):
                jj = ' 无题'
            else:
                jj = ll[1]
            if (re.findall(".+新", jj)):
                jj = jj[:-1]
            if (jj == '' or jj == ' ' or jj == '  '):
                jj = ' 无题'
            uu = "第" + str(i) + "章 " + jj
            i = i + 1
            h.writelines(uu)
            continue

        h.writelines(sstr)

    f.close()
    h.close()


def page():
    f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\page.csv", 'a')
    i=921
    while(i<929):
        f.writelines(str(i)+'\n')
        i=i+1

    f.close()

if __name__ == '__main__':
    page()

