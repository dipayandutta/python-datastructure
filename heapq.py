# -*- coding: utf-8 -*-

import heapq

list1 = [4,6,8,10,-1]
heapq.heapify(list1)
print list1


h = []
heapq.heappush(h,(1,'code'))
heapq.heappush(h,(2,'python'))
heapq.heappush(h,(3,'machine learning'))

print h