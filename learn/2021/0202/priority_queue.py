# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import queue_c, stack, time


class Node(object):  # 节点
    def __init__(self, elem):
        self.elem = elem
        self.father = None
        self.left = None
        self.right = None


class PriorityQueue(object):  # 基于堆的优先队列
    def __init__(self, list=None):
        self.__count = 0
        if (list == None):
            self.__root = None
        else:
            node = Node(list[0])
            self.__root = node
            q = queue_c.Queue()
            q.enqueue(node)
            self.__count += 1
            i = 0
            while (i < len(list) - 1):
                i = i + 1
                node = Node(list[i])

                if (q.peek().left == None):
                    q.peek().left = node
                    node.father = q.peek()
                    self.__sift_up(q.peek().left)
                    self.__count += 1
                    q.enqueue(node)
                    continue
                if (q.peek().right == None):
                    q.peek().right = node
                    node.father = q.peek()
                    self.__sift_up(q.peek().right)
                    self.__count += 1
                    q.enqueue(node)
                    continue
                q.dequeue()
                i = i - 1

    def is_empty(self):  # 返回队列是否为空
        return self.__root is None

    def size(self):  # 返回队列里的元素个数
        return self.__count

    def travel(self):  # 遍历整个队列   测试用
        if (self.__root == None):
            print(None, end=" | ")
            return
        q = queue_c.Queue()
        q.enqueue(self.__root)
        while (q.is_empty() == False):
            print(q.peek().elem, end=" | ")
            if (q.peek().left == None):
                pass
            else:
                q.enqueue(q.peek().left)
            if (q.peek().right == None):
                pass
            else:
                q.enqueue(q.peek().right)
            q.dequeue()

    def __find_last_index(self):  # 一层一层找到第一个叶子节点有空的节点，并返回它
        if (self.__head is None):
            return None, 0

        q = queue_c.Queue()
        q.enqueue(self.__root)
        while (q.is_empty() == False):
            if (q.peek().left is None):
                return q.peek()
            else:
                q.enqueue(q.peek().left)
            if (q.peek().right is None):
                return q.peek()
            else:
                q.enqueue(q.peek().right)
            q.dequeue()

    def __find_last_node(self, root):  # 找到最后一层最右边的节点，并返回它
        pass

    def __sift_up(self, tmp):  # 上浮
        while (tmp.father):
            if (tmp.elem > tmp.father.elem):
                return
            tmp.elem, tmp.father.elem = tmp.father.elem, tmp.elem
            tmp = tmp.father

    def enqueue(self, item):  # 向队列里添加元素
        node = Node(item)
        if (self.is_empty()):
            self.__head = node
            self.__count = self.__count + 1
            return
        tmp = self.__find_last_index()
        if (tmp.left is None):
            tmp.left = node
            node.father = tmp
            tmp = tmp.left
        else:
            tmp.right = node
            node.father = tmp
            tmp = tmp.right

        self.__sift_up(tmp)
        self.__count += 1

    def dequeue(self):  # 删除队列的第一个值,返回已删除结点的值。
        if (self.is_empty()):
            return None
        tmp = self.__root
        lasttmp = self.__find_last_index()

        return tmp.elem

    def peek(self):  # 返回第一个节点的值
        if (self.is_empty()):
            return None
        return self.__head.elem


if __name__ == "__main__":
    treee = PriorityQueue([8, 12, 11, 7, 5, 6, 10, 9, 2, 3, 4])

    # treee.cg()
    print("层序遍历==========", end="\n| ")
    treee.travel()
    print("\n")

    print(treee.size())
