# -*- coding: utf-8 -*-

class SortList(object):
    def __init__(self, yList=[]):
        self.mlist = yList
        self.mlength = len(yList)

    def lenth(self):
        return self.mlength

    def travel(self):
        print(self.mlist)

    def bubbleSort(self):
        i = self.mlength
        while (i):
            j = 0
            while (j < i - 1):
                if (self.mlist[j + 1] < self.mlist[j]):
                    a = self.mlist[j + 1]
                    self.mlist[j + 1] = self.mlist[j]
                    self.mlist[j] = a
                j = j + 1
            i = i - 1

    def selectionSort(self):
        i = 0
        while (i < self.mlength):
            j = i + 1
            while (j < self.mlength):
                if (self.mlist[i] > self.mlist[j]):
                    a = self.mlist[i]
                    self.mlist[i] = self.mlist[j]
                    self.mlist[j] = a
                j = j + 1
            i = i + 1

    def insertionSort(self):
        i = 0
        while (i < self.mlength - 1):
            j = i + 1
            while (j > 0):
                if (self.mlist[j - 1] > self.mlist[j]):
                    a = self.mlist[j - 1]
                    self.mlist[j - 1] = self.mlist[j]
                    self.mlist[j] = a
                j = j - 1
            i = i + 1



if __name__ == "__main__":
    # import os
    # os.system("CLS")

    l = [4, 3, 5, 2, 9, 6, 1, 8]
    b = SortList(l)
    b.travel()
    print(b.lenth())
    b.insertionSort()
    b.travel()

    # from single_link_list import SingleLinkList

    # class Sort(SingleLinkList):
    #     def __init__(self, obj):
    #         SingleLinkList.__init__(self)
    #         self.count = 0
    #         if (type(obj) == list):
    #             for indvd in obj:
    #                 self.append(indvd)
    #                 # self.__tail=self.__tail.next
    #                 self.count = self.count + 1

    #     def lenth(self):
    #         return self.count

    #     # 冒泡排序
    #     def bubbleSort(self):
    #         SingleLinkList.__init__(self)
    #         if (self.length() <= 1):
    #             return
    #         tnode = self.get_head()
    #         mnode = self.get_head()
    #         while(tnode.next):
    #             tnode = tnode.next
    #         while(tnode != self.get_head()):
    #             if(mnode.elem < mnode.next.elem):
    #                 a = mnode.elem
    #                 mnode.elem = mnode.next.elem
    #                 mnode.next.elem = a
    #             if(mnode.next == tnode):
    #                 tnode=mnode
    #                 mnode = self.get_head()
    #                 continue
    #             mnode = mnode.next

    # if __name__ == "__main__":
    #     l = [4, 3, 5]
    #     h = 5
    #     b = Sort(l)
    #     b.travel()
    #     print(b.lenth())
    #     b.bubbleSort()
    #     b.travel()
