# -*- coding: utf-8 -*-

import xlrd, xlwt, workorder, time
from xlutils.copy import copy
# from openpyxl import load_workbook

import os

filename = 'C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\data\\'


def writedata(xlsname, *args):
    data = xlrd.open_workbook(filename + xlsname)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    # print("nrows %d, ncols %d" % (nrows, ncols))

    data1 = xlwt.Workbook(filename + xlsname)
    worksheet = data1.add_sheet('My Worksheet')
    while (nrows):
        hh = table.row_values(nrows - 1, start_colx=0, end_colx=None)
        # print(hh)
        for i in range(ncols):
            worksheet.write(nrows, i, hh[i])
        nrows = nrows - 1
    count = 0
    for i in args:
        worksheet.write(nrows, count, i)
        count = count + 1

    for i in range(0, len(args)):
        worksheet.col(i).width = 6333
    data1.save(filename + xlsname)


def getimf(xlsname, count):
    data = xlrd.open_workbook(filename + xlsname)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    ret = table.row_values(count, start_colx=0, end_colx=None)
    return ret


def additionaldata(xlsname, count, wod):
    data = xlrd.open_workbook(filename + xlsname)
    worksheet = data.sheets()[0]
    nrows = worksheet.nrows
    leeen = ncols = 3

    # print(nrows,ncols)

    data1 = xlwt.Workbook(filename + xlsname)
    worksheet1 = data1.add_sheet('My Worksheet')

    while (nrows):
        hh = worksheet.row_values(nrows - 1, start_colx=0, end_colx=None)
        if (count == nrows):
            colcount = 0
            for i in range(ncols):
                worksheet1.write(nrows - 1, colcount, hh[i])
                colcount = colcount + 1
            args = []
            args.append(wod.workorder_id)
            args.append(wod.workorder_machineauditresults)
            args.append(wod.workorder_manualauditresults)
            args.append(wod.workorder_illegallabel)
            for dstr in args:
                worksheet1.write(nrows - 1, colcount, dstr)
                colcount = colcount + 1

            leeen = ncols + len(args)
        # print(hh)
        else:
            onerow = worksheet.row_values(count, start_colx=0, end_colx=None)
            for i in range(len(onerow)):
                worksheet1.write(nrows - 1, i, hh[i])
        nrows = nrows - 1

    for i in range(0, leeen):
        worksheet1.col(i).width = 6333
    data1.save(filename + xlsname)


def changetime(xlsname, gnrows, timestr):  # 修改第三列操作时间，gnrows表示行数:[1,max]
    data = xlrd.open_workbook(filename + xlsname)
    worksheet = data.sheets()[0]
    nrows = worksheet.nrows
    ncols = worksheet.ncols

    data1 = xlwt.Workbook(filename + xlsname)
    worksheet1 = data1.add_sheet('My Worksheet')

    while (nrows):
        hh = worksheet.row_values(nrows - 1, start_colx=0, end_colx=None)

        for i in range(ncols):
            if (nrows == gnrows and i == 2):
                worksheet1.write(nrows - 1, i, timestr)
                continue
            worksheet1.write(nrows - 1, i, hh[i])

        nrows = nrows - 1

    for i in range(0, ncols):
        worksheet1.col(i).width = 6333
    data1.save(filename + xlsname)


if __name__ == "__main__":
    #('workorderdata1.xls', 2, "2020-11-22 11:22:33")
    # wod=workorder.WorkOrder(id="333", machineauditresults="444", illegallabel="555")
    # additionaldata1('workorderdata2.xlsx', 1, wod)
    print(abs(2-3))
