# -*- coding: utf-8 -*-


# 工单类
class WorkOrder(object):
    def __init__(self, id='9527', type='图片', machineauditresults='-', manualauditresults='-', illegallabel='-',
                 operationtime='-', inchargeperson='-', orderstate='-', documentssource='-', filename='-'):
        self.workorder_id = id  # 工单ID
        self.workorder_type = type  # 工单类型
        self.workorder_machineauditresults = machineauditresults  # 工单机器审核结果
        self.workorder_manualauditresults = manualauditresults  # 工单人工审核结果
        self.workorder_illegallabel = illegallabel  # 工单违规标签
        self.workorder_operationtime = operationtime  # 工单最后一次操作时间

        # 20210127添加
        self.workorder_filename = filename  # 文件名
        self.workorder_inchargeperson = inchargeperson  # 当前负责人
        self.workorder_orderstate = orderstate  # 工单状态
        self.workorder_documentssource = documentssource  # 文件来源

    def printallmembers(self):
        print(self.workorder_id)
        print(self.workorder_type)
        print(self.workorder_machineauditresults)
        print(self.workorder_manualauditresults)
        print(self.workorder_illegallabel)
        print(self.workorder_operationtime)
        print(self.workorder_filename)
        print(self.workorder_inchargeperson)
        print(self.workorder_orderstate)
        print(self.workorder_documentssource)

    def getmemberslist(self):
        ret = []
        ret.append(self.workorder_filename)
        ret.append(self.workorder_type)
        ret.append(self.workorder_operationtime)
        ret.append(self.workorder_id)
        ret.append(self.workorder_machineauditresults)
        ret.append(self.workorder_manualauditresults)
        ret.append(self.workorder_illegallabel)
        ret.append(self.workorder_inchargeperson)
        ret.append(self.workorder_orderstate)
        ret.append(self.workorder_documentssource)

        return ret

    def change_id(self, id):
        self.workorder_id = id
