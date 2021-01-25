# -*- coding: utf-8 -*-


# 工单类
class WorkOrder(object):
    def __init__(self, id='9527', type='图片', machineauditresults='-', manualauditresults='-', illegallabel='-',
                 operationtime='-'):
        self.workorder_id = id  # 工单ID
        self.workorder_type = type  # 工单类型
        self.workorder_machineauditresults = machineauditresults  # 工单机器审核结果
        self.workorder_manualauditresults = manualauditresults  # 工单人工审核结果
        self.workorder_illegallabel = illegallabel  # 工单违规标签
        self.workorder_operationtime = operationtime  # 工单最后一次操作时间

    def change_id(self, id):
        self.workorder_id = id
