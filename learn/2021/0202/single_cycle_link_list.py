# -*- coding: utf-8 -*-
# 单向循环链表

from single_link_list import Node


class SingleLinkList(object):  # 单向循环链表
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):  # 链表是否为空
        return self.__head is None

    def length(self):  # 链表的长度
        ret = 0
        cur = self.__head
        while (cur):
            cur = cur.next
            ret = ret + 1
        return ret

    def travel(self):  # 遍历整个链表
        print("==开始遍历列表===================")
        cur = self.__head
        while (cur):
            print(cur.elem)
            cur = cur.next
        print("==结束遍历列表===================")

    def head_add(self, item):  # 头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):  # 尾部添加元素
        node = Node(item)
        if (self.is_empty()):
            self.__head = node
            return
        cur = self.__head
        while (cur.next != None):
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):  # 指定位置添加元素，pos从0开始计算
        if (pos <= 0):
            self.head_add(item)
            return
        if (pos > self.length() - 1):
            self.append(item)
            return
        pre = self.__head
        conut = 0
        while (conut < (pos - 1)):
            pre = pre.next
            conut = conut + 1
        node = Node(item)
        node.next = pre.next
        pre.next = node

    def remove(self, item):  # 删除节点item,从左到右第1个,返回已删除结点的位置。
        cur = self.__head
        pre = None
        pos = 0
        while (cur):
            if (cur.elem == item):
                if (pre == None):
                    self.__head = cur.next
                    return pos
                pre.next = cur.next
                return pos
            pre = cur
            cur = cur.next
            pos = pos + 1
        return None

    def sreach(self, item):  # 查找节点是否存在，返回真假
        cur = self.__head
        while (cur):
            if (cur.elem == item):
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    listt = SingleLinkList()
    listt.head_add(8)
    print(listt.is_empty())
    listt.append("222")
    listt.append([5, 5, 2, 4])
    listt.append(3 + 3)

    listt.head_add(0)
    listt.travel()

    listt.insert(-5, 666)
    listt.travel()

    print(listt.remove(5646))
    listt.travel()
