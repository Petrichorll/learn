# -*- coding: utf-8 -*-

class Node(object):  # 节点
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


class BinaryTree(object):  # 单链表
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):  # 链表是否为空
        return self.__head is None
