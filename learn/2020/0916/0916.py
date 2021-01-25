# -*- coding: utf-8 -*-

import xlsxwriter

import xlrd
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#写数据
def save_excel(data,oldWb,oldWbs):
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)
    rowIndex = oldWbs.nrows
    data.sort()
    init=0
    for i in data:
        if(i!=init and i[0]!='学校'):
            newWs.write(rowIndex, 0, "")
            newWs.write(rowIndex, 1, "")
            newWs.write(rowIndex, 2, "")
            newWs.write(rowIndex, 3, "")
            newWs.write(rowIndex, 4, "")
            newWs.write(rowIndex, 5, i[0])
            newWs.write(rowIndex, 6, i[1])
            newWs.write(rowIndex, 7, i[2])
            newWs.write(rowIndex, 8, i[3])
            newWb.save('/Users/sheya/Documents/yy/init_bak.xls')
            print "finished"
            rowIndex += 1
            init=i
if __name__ == '__main__':
    data01=xlrd.open_workbook('/Users/sheya/Documents/yy/details01.xls')
    data02=xlrd.open_workbook('/Users/sheya/Documents/yy/details02.xls')
    data03=xlrd.open_workbook('/Users/sheya/Documents/yy/details03.xls')
    data04=xlrd.open_workbook('/Users/sheya/Documents/yy/init_bak.xls')
    #根据索引顺序获取工作表
    table01=data01.sheet_by_index(0)
    table02=data02.sheet_by_index(0)
    table03=data03.sheet_by_index(0)
    table04=data04.sheet_by_index(0)
    #获取行数和列数
    nrows1=table01.nrows
    nrows2=table02.nrows
    nrows3=table03.nrows
    nrows4=table04.nrows
    lst01=[]
    lst02=[]
    lst03=[]
    lst04=[]
    #获取表中数据
    for i in range(0,nrows1):
        school=table03.cell_value(i,0)
        grade = table03.cell_value(i, 1)
        clazz=table03.cell_value(i,2)
        name = table03.cell_value(i, 3)
        rowdata = [school,grade,clazz,name]
        lst01.append(rowdata)
    for i in range(0,nrows2):
        school=table03.cell_value(i,0)
        grade = table03.cell_value(i, 1)
        clazz=table03.cell_value(i,2)
        name = table03.cell_value(i, 3)
        rowdata = [school,grade,clazz,name]
        lst02.append(rowdata)
    for i in range(0,nrows3):
        school=table03.cell_value(i,0)
        grade = table03.cell_value(i, 1)
        clazz=table03.cell_value(i,2)
        name = table03.cell_value(i, 3)
        rowdata = [school,grade,clazz,name]
        lst03.append(rowdata)
    for i in range(0,nrows4):
        school=table04.cell_value(i,5)
        grade=table04.cell_value(i,6)
        clazz=table04.cell_value(i,7)
        rowdata=[school,grade,clazz]
        lst04.append(rowdata)
    data=[]
    for i in lst04:
        for j in lst01:
            data.append(j)
        for j in lst02:
            data.append(j)
        for j in lst03:
            data.append(j)
    save_excel(data,data04,table04)
