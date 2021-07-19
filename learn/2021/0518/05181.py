# -*- coding: utf-8 -*-
import os, re, time

fpath = "C:\\Users\\19144\\Desktop\\图库\\"
fpath1 = "C:\\Users\\19144\\Desktop\\图库1\\"


def func4():
    for i, j, k in os.walk(fpath):
        for sstr in j:
            for i1, j1, k1 in os.walk(fpath + sstr):
                for jstr in k1:
                    oldf = i1 + '\\' + jstr
                    newf1 = fpath1 + "综合\\" +sstr[2:]+jstr

                    os.rename(oldf, newf1)

            os.removedirs(fpath + sstr)


def func3(name):
    if not os.path.exists(fpath1 + "分类类型\\" + name):
        os.mkdir(fpath1 + "分类类型\\" + name)
    for i, j, k in os.walk(fpath):
        sstr = i
        hh = re.split(name, sstr)
        if (len(hh) > 1):
            for i1, j1, k1 in os.walk(sstr):
                for jstr in k1:
                    jj = re.split('\.', jstr)
                    oldf = i1 + '\\' + jstr
                    newf1 = fpath1 + "分类类型\\" + name + "\\" + name + '{}'.format(int(jj[0])) + "." + jj[1]
                    i = 1
                    while (os.path.exists(newf1)):
                        newf1 = fpath1 + "分类类型\\" + name + "\\" + name + '{}'.format(int(jj[0]) + i) + "." + jj[1]
                        i = i + 1
                    os.rename(oldf, newf1)
            print(sstr)
            os.removedirs(sstr)


def func2(name):
    if not os.path.exists(fpath1 + "明星\\" + name):
        os.mkdir(fpath1 + "明星\\" + name)
    for i, j, k in os.walk(fpath):
        sstr = i
        hh = re.split(name, sstr)
        if (len(hh) > 1):
            for i1, j1, k1 in os.walk(sstr):
                for jstr in k1:
                    jj = re.split('\.', jstr)
                    oldf = i1 + '\\' + jstr
                    newf1 = fpath1 + "明星\\" + name + "\\" + name + '{}'.format(int(jj[0])) + "." + jj[1]
                    i = 1
                    while (os.path.exists(newf1)):
                        newf1 = fpath1 + "明星\\" + name + "\\" + name + '{}'.format(int(jj[0]) + i) + "." + jj[1]
                        i = i + 1
                    os.rename(oldf, newf1)
            print(sstr)
            os.removedirs(sstr)


def func1():
    for i, j, k in os.walk(fpath):
        sstr = i
        hh = re.split("校花美女", sstr)
        if (len(hh) > 1):
            for i1, j1, k1 in os.walk(sstr):
                for jstr in k1:
                    jj = re.split('\.', jstr)
                    oldf = i1 + '\\' + jstr
                    kk = re.split('@', hh[1])
                    if (len(kk) > 1):
                        ll = re.split(' ', kk[1])
                        if (jj[0] == '1'):
                            newf1 = fpath1 + '\\' + kk[1] + "." + jj[1]
                        else:
                            newf1 = fpath1 + ll[0] + '{}'.format(int(jj[0]) - 1) + "." + jj[1]
                            i = 1
                            while (os.path.exists(newf1)):
                                newf1 = fpath1 + ll[0] + '{}'.format(int(jj[0]) - 1 + i) + "." + jj[1]
                                i = i + 1
                        os.rename(oldf, newf1)
            os.removedirs(sstr)


if __name__ == "__main__":
    func4()
