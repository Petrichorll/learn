# -*- coding: utf-8 -*-

from single_link_list import Node


class Stack(object):  # 栈
    def __init__(self, node=None):
        if (node):
            self.__count = 1
        else:
            self.__count = 0
        self.__head = node

    def is_empty(self):  # 返回栈是否为空
        return self.__head is None

    def length(self):  # 返回栈里的元素个数
        return self.__count

    def travel(self):  # 遍历整个栈   测试用
        cur = self.__head
        print("| ", end="")
        while (cur):
            print(cur.elem, end=" | ")
            cur = cur.next
        print("\n", end="")

    def push(self, item):  # 向栈里添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node
        self.__count = self.__count + 1

    def pop(self):  # 删除栈的第一个值,返回已删除结点的值。
        if (self.is_empty()):
            return None
        ret = self.__head.elem
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return ret

    def top(self):  # 返回第一个节点的值
        if (self.is_empty()):
            return None
        return self.__head.elem


if __name__ == "__main__":
    listt = Stack()

    print("判断是否为空：")
    print(listt.is_empty())
    print(listt.top())

    print("入栈：")
    listt.push(9)
    print(listt.length())
    listt.travel()
    print(listt.top())

    print("入栈：")
    listt.push(8)
    listt.push(7)
    listt.push(6)
    listt.push(5)
    print(listt.length())
    listt.travel()

    print(listt.top())

    print("出栈：")
    listt.pop()
    listt.pop()
    listt.pop()

    print(listt.length())
    listt.travel()

    print(listt.top())

    listt.pop()
    listt.pop()
    listt.pop()
    listt.pop()
    listt.pop()
    listt.pop()

    print(listt.length())
    listt.travel()

    print(listt.top())

    a = Node(7)
    listt = Stack(a)

    print(listt.length())
    listt.travel()

    print(listt.top())
