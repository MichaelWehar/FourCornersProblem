# Created on Thu May 21 11:11:10 2020
# Author: Ari Liloia

# Helper functions
def createEmptyArray(n):
    return [False for _ in range(n)]

def createEmptyMatrix(m, n):
    return [createEmptyArray(n) for _ in range(m)]

m = 5
n = 5

emptyMatrix = createEmptyMatrix(5, 5)
testMatrix = emptyMatrix
testMatrix[0][0] = True
testMatrix[0][4] = True
testMatrix[4][4] = True
testMatrix[4][0] = True

print(testMatrix)
# bijection
# 4 cols
# (0,4): (0 * 4) + 4 = 4
# (1,0): (1 * 4) + 0 = 4
# this is prob why we start at an index 1 greater
# but why is it working w this code

def rectExists(matrix, m, n):
    # This array will assign data to each pair of columns
    columnPairs = createEmptyArray(n * n)
    # Traverse through the matrix row by row
    for i in range(m):
        currentRow = []
        # Traverse through current row's elements to find all 1's (or true entries)
        for j in range(n):
            if(matrix[i][j] == True):
                currentRow.append(j)
        # Efficiently traverse through pairs of column indexes with 1's (or true entries)
        while(len(currentRow) > 1):
            # Pop removes the first element from a list
            firstElement = currentRow.pop(0)
            # Iterate through other entries containing 1 (or true)
            # while checking if they have already been recorded
            for nextIndex in range(len(currentRow)):
                nextElement = currentRow[nextIndex]
                # print((firstElement * n) + nextElement)
                if(columnPairs[(firstElement * n) + nextElement] == True):
                    # print(str(firstElement) + " " + str(nextElement))
                    return True
                else:
                    columnPairs[(firstElement * n) + nextElement] = True
    return False

print(rectExists(testMatrix, m, n))
