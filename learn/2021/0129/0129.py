# -*- coding: utf-8 -*-

s = "(){}[]"


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        ilist = []
        jlist = []
        while (i < j):
            if (ilist != []):
                if (self.ismatch(ilist[0], s[j])):
                    j = j - 1
                    del ilist[0]
                    continue
                if (self.ismatch(ilist[0], s[i])):
                    i = i + 1
                    del ilist[0]
                    continue
            else:
                ilist.append(s[i])
                i=i+1
                continue
            # if (jlist != []):
            #     if (self.ismatch(s[j], jlist[0])):
            #         j = j - 1
            #         del jlist[0]
            #         continue
            #     if (self.ismatch(s[i], jlist[0])):
            #         i = i + 1
            #         del jlist[0]
            #         continue

    def ismatch(self, s1, s2):
        if (s1 == "{" and s2 == "}"):
            return True
        if (s1 == "(" and s2 == ")"):
            return True
        if (s1 == "[" and s2 == "]"):
            return True
        return False
