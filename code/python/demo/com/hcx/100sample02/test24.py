#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：两个乒乓球队进行比赛，各出三人，甲队为a,b,c三人，乙队为x,y,z三人，以抽签决定比赛名单，有向
队员打听比赛的名单，a说他不和x比，c说他不和x，z比，请编程招待三个赛手的名单。
"""
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc -- %s' % (chr(i), chr(j), chr(k)))