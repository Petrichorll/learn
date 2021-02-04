# -*- coding: utf-8 -*-

import queue, stack, time


class Node(object):  # 节点
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


class BinaryTree(object):  # 二叉树
    def __init__(self, list=None):
        if (list == None):
            self.__root = None
        else:
            node = Node(list[0])
            self.__root = node
            q = queue.Queue()
            q.enqueue(node)
            # q.travel()
            # print(q.peek())
            i = 0
            while (i < len(list) - 1):
                i = i + 1
                node = Node(list[i])
                if (q.peek().left == None):
                    q.peek().left = node
                    q.enqueue(node)
                    continue
                if (q.peek().right == None):
                    q.peek().right = node
                    q.enqueue(node)
                    continue
                q.dequeue()
                i = i - 1

    def is_empty(self):  # 二叉树是否为空
        return self.__root is None

    def num_nodes(self):  # 求二叉树的节点个数
        pass

    def add_root(self, root):  # 将别的二叉树的根复制到当前二叉树
        if (self.__root):
            return False
        self.__root = root
        return True

    def data(self):  # 获取二叉树根储存的数据
        pass

    def left(self):  # 获取二叉树的左子树
        pass

    def right(self):  # 获取二叉树的右子树
        pass

    def travel(self):  # 层序遍历并打印出二叉树
        if (self.__root == None):
            print(None)
        q = queue.Queue()
        q.enqueue(self.__root)
        while (q.is_empty() == False):
            print(q.peek().elem)
            if (q.peek().left == None):
                pass
            else:
                q.enqueue(q.peek().left)
            if (q.peek().right == None):
                pass
            else:
                q.enqueue(q.peek().right)
            q.dequeue()

    def DLR_travel_d(self, root=1):  # 先序(根左右)遍历二叉树。递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root
        if (root == None):
            return
        print(root.elem)
        self.DLR_travel_d(root.left)
        self.DLR_travel_d(root.right)

    def DLR_travel_fd(self, root=1):  # 先序(根左右)遍历二叉树。非递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root

        stmp = stack.Stack()
        stag = stack.Stack()
        stmp.push(root)
        stag.push(0)
        while (stmp.is_empty() == False):
            print(stmp.top().elem)
            while (stmp.top().left != None and stag.top() == 0):
                stmp.push(stmp.top().left)
                stag.push(0)
            if (stmp.top().right == None):
                stmp.pop()
                stag.pop()
                stag.pop()
                stag.push(1)
            else:
                if (stag.top() == 0):
                    stmp.push(stmp.top().right)
                    stag.pop()
                    stag.push(1)
                    stag.push(0)


if __name__ == "__main__":
    treee = BinaryTree([8, 2, 3, 4, 5, 6, 7])
    treee.DLR_travel_fd()
