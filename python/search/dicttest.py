import sys
import os
sys.path.insert(1, '../helper_functions')
#when doing modules from a different directory .. gotta specify

from matrix_reader import MatrixReader

test = {}
test[(0,0)] = (100,30)
test[(1,2)] = (20,350)
#print(test)

#print(test.get((0,0)))

#print("---")

isDict = {}
matrix = [[1,0,1,1,0],[0,1,1,0,1],[1,0,0,0,1],[0,1,0,1,0],[0,0,0,0,0]]
m = 5
n = 5
    # Traverse through the matrix col by col

for i in range(m):
    closest = 0
    print(i)
    print(matrix[i])
    for x in range(len(matrix[i])):
        #if we find one
        if(matrix[i][x] == 1):
            #if we havent found one yet
            if (closest == 0):
                #the most recent one we find is this one
                closest = x+1
            #if we've already found one
            else:
                #put the last one in the dictionary
                isDict[(i*m)+x+1] = closest
                #make this one the newest one
                closest = x+1








"""

for i in range(m):
    closest = 0
    print(i)
    print(matrix[i])
    for x in range(len(matrix[i])):
        #if we find one
        if(matrix[i][x] == 1):
            #if we havent found one yet
            if (closest == 0):
                #the most recent one we find is this one
                closest = x+1
            #if we've already found one
            else:
                #put the last one in the dictionary
                isDict[(i*m)+x+1] = closest
                #make this one the newest one
                closest = x+1
"""



print(isDict)
