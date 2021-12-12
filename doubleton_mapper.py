#!/usr/bin/env python
# coding: utf-8
import sys
#get all lines from stdin
for line in sys.stdin:
#remove leading and trailing whitespace
    line = line.strip()
    #split the line into items
    items = line.split()
    #output ((item1,item2),1) in tab-delimited format
    for item in items:
        current_index=items.index(item)+1
        while(current_index<len(items)):
            print('(%s,%s)\t%s' % (item,items[current_index],1))
            current_index+=1





