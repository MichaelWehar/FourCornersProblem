#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:11:10 2020

@author: Ari Liloia
"""




m = 5
n = 5


mtx_empty = [[False, False, False, False, False],
             [False, False, False, False, False],
             [False, False, False, False, False],
             [False, False, False, False, False],
             [False, False, False, False, False]]

test2 = mtx_empty 
test2[0][0] = True
test2[0][4] = True
test2[4][1] = True
test2[4][0] = True

print(test2)
#bijection
#4 cols
#(0,4): (0*4)+4 = 4
#(1,0):     (1*4)+0 = 4
#this is prob why we start at an index 1 greater
#but why is it working w this code




def rect_exists(matrix, m, n):
    solnmtx = [False for _ in range(m*n)]
    for i in range(m):
        oneRow= []
        for j in range(n):
            if(matrix[i][j]==True):
                oneRow.append(j)
        while(len(oneRow)>1):
            oneElement = oneRow.pop(0)
            for remaining in range(len(oneRow)):
                print((oneElement*n)+oneRow[remaining])
                if(solnmtx[(oneElement*n)+oneRow[remaining]] == True):
                    #print(str(oneElement) + " " + str(oneRow[remaining]))
                    
                    return True
                else:
                    solnmtx[(oneElement*n)+oneRow[remaining]] = True
    return False

print(rect_exists(test2,m,n))
            
    
            