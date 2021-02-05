# -*- coding: utf-8 -*-

import queue_c, stack, time


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
            q = queue_c.Queue()
            q.enqueue(node)

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

    def DLR_travel_d(self, root=1):  # 先序(根左右)遍历二叉树。递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root
        if (root == None):
            return
        print(root.elem, end=" | ")
        self.DLR_travel_d(root.left)
        self.DLR_travel_d(root.right)

    def DLR_travel_fd(self, root=1):  # 先序(根左右)遍历二叉树。非递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root

        t = root
        stmp = stack.Stack()
        stmp.push(t)

        while (not stmp.is_empty()):
            while (t is not None):
                stmp.push(t)
                print(t.elem, end=" | ")
                t = t.left
            t = stmp.top()
            stmp.pop()
            t = t.right

    def LDR_travel_d(self, root=1):  # 中序(左根右)遍历二叉树。递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root
        if (root == None):
            return
        self.LDR_travel_d(root.left)
        print(root.elem, end=" | ")
        self.LDR_travel_d(root.right)

    def LDR_travel_fd(self, root=1):  # 中序(左根右)遍历二叉树。非递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root

        t = root
        stmp = stack.Stack()
        stmp.push(t)

        while (not stmp.is_empty()):
            while (t is not None):
                stmp.push(t)
                t = t.left
            t = stmp.top()
            stmp.pop()
            if (not stmp.is_empty()):
                print(t.elem, end=" | ")
            t = t.right

    def LRD_travel_d(self, root=1):  # 后序(左右根)遍历二叉树。递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root
        if (root == None):
            return
        self.LRD_travel_d(root.left)
        self.LRD_travel_d(root.right)
        print(root.elem, end=" | ")

    def LRD_travel_fd(self, root=1):  # 后序(左右根)遍历二叉树。非递归。
        if (None == self.__root and root == 1):
            print(None)
            return
        if (root == 1):
            root = self.__root

        t = root
        stmp = stack.Stack()
        stag = stack.Stack()
        stmp.push(t)
        stag.push(0)
        while (not stmp.is_empty()):
            t = stmp.top()
            if (stag.top() == 0):
                stag.pop()
                stag.push(1)
                if (t.right is not None):
                    stmp.push(t.right)
                    stag.push(0)
                if (t.left is not None):
                    stmp.push(t.left)
                    stag.push(0)
            else:
                print(stmp.top().elem, end=" | ")
                stmp.pop()
                stag.pop()

    def cg(self):
        # node = self.__root
        # node = node.left
        # node.left = None
        #
        # node = self.__root
        # node = node.right
        # node.left = None
        #
        # self.__root=None
        self.__root.right = None
        self.__root.left.right = None
        self.__root.left.left.right = None


if __name__ == "__main__":
    treee = BinaryTree([8, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12])

    #treee.cg()
    print("层序遍历==========", end="\n| ")
    treee.travel()

    print("\n前序遍历递归==========", end="\n| ")
    treee.DLR_travel_d()
    print("\n前序遍历非递归==========", end="\n| ")
    treee.DLR_travel_fd()

    print("\n中序遍历递归==========", end="\n| ")
    treee.LDR_travel_d()
    print("\n中前序遍历非递归==========", end="\n| ")
    treee.LDR_travel_fd()

    print("\n后序遍历递归==========", end="\n| ")
    treee.LRD_travel_d()
    print("\n后序遍历非递归==========", end="\n| ")
    treee.LRD_travel_fd()
