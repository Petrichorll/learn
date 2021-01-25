# -*- coding: utf-8 -*-


import os,random

files_path2 = "C:/Users/19144/PycharmProjects/学习/test_demo/data/PendingDocuments/test2/"



for i, j, k in os.walk(files_path2):
    print(k)
    print(random.choice(k))