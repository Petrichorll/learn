# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

from single_link_list import Node


class Queue(object):  # 队列
    def __init__(self, node=None):
        if (node):
            self.__count = 1
        else:
            self.__count = 0
        self.__head = node
        self.__tail = node  # 尾指针

    def is_empty(self):  # 返回队列是否为空
        return self.__head is None

    def length(self):  # 返回队列里的元素个数
        return self.__count

    def travel(self):  # 遍历整个队列   测试用
        cur = self.__head
        print("| ", end="")
        while (cur):
            print(cur.elem, end=" | ")
            cur = cur.next
        print("\n", end="")

    def enqueue(self, item):  # 向队列里添加元素
        node = Node(item)
        if (self.is_empty()):
            self.__head = node
            self.__tail = node
            self.__count = self.__count + 1
            return
        self.__tail.next = node
        self.__tail = node
        self.__count = self.__count + 1

    def dequeue(self):  # 删除队列的第一个值,返回已删除结点的值。
        if (self.is_empty()):
            return None
        ret = self.__head.elem
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return ret

    def peek(self):  # 返回第一个节点的值
        if (self.is_empty()):
            return None
        return self.__head.elem


if __name__ == "__main__":
    listt = Queue()

    print("判断是否为空：")
    print(listt.is_empty())
    print(listt.peek())

    print("入队列：")
    listt.enqueue(9)
    print(listt.length())
    listt.travel()
    print(listt.peek())

    print("入队列：")
    listt.enqueue(8)
    listt.enqueue(7)
    listt.enqueue(6)
    listt.enqueue(5)
    print(listt.length())
    listt.travel()

    print(listt.peek())

    print("出队列：")
    listt.dequeue()
    listt.dequeue()
    listt.dequeue()

    print(listt.length())
    listt.travel()

    print(listt.peek())

    listt.dequeue()
    listt.dequeue()
    listt.dequeue()
    listt.dequeue()
    listt.dequeue()
    listt.dequeue()

    print(listt.length())
    listt.travel()

    print(listt.peek())

    a = Node(7)
    listt = Queue(a)

    print(listt.length())
    listt.travel()

    print(listt.peek())
