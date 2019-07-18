# -*- coding: utf-8 -*-

# Python's built-in bisect() module is available for binary search in a sorted Sequence

from bisect import bisect
list = [3,30,-1,2,29,4]
sorted_list =  sorted(list)

search_key = 4
if bisect(sorted_list,search_key):
    print "{0} Key Found!!!".format(search_key)
else:
    print "{0} Key Not Found!!".format(search_key)