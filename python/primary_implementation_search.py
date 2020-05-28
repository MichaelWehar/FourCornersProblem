# Created on Thu May 21 11:11:10 2020
# Author: Ari Liloia
import sys
import os
sys.path.insert(1, 'helper_functions')

from matrix_reader import MatrixReader


# Algorithm implementation
def rectSize(m, n, matrix):
    # This set will store pairs of column indexes
    columnPairs = {}
    # Traverse through the matrix row by row
    for i in range(m):
        currentRow = []
        # Traverse through current row's elements to find all 1's (or true entries)
        for j in range(n):
            if(matrix[i][j] == True):
                currentRow.append(j)
        # Efficiently traverse through pairs of column indexes with 1's (or true entries)
        # First, iterate over all possible entries containing 1 (or true)
        for firstIndex in range(len(currentRow)):
            firstElement = currentRow[firstIndex]
            # Next, iterate over all possible next entries containing 1 (or true)
            for nextIndex in range(firstIndex + 1, len(currentRow)):
                nextElement = currentRow[nextIndex]
                # print((firstElement * n) + nextElement)
                # Encode a pair (firstElement, nextElement) as (firstElement * n) + nextElement
                currentPair = (firstElement * n) + nextElement
                if(currentPair in columnPairs):

                    # print(str(firstElement) + " " + str(nextElement))
                    matrixHeight = i - (columnPairs.get(currentPair)) + 1
                    matrixWidth = nextElement - firstElement + 1 
                    return matrixHeight*matrixWidth
                else:
                    columnPairs[currentPair] = i
                    #columnPairs.add(currentPair)
    return 0

#Run all test cases in same file
print('--')
for entry in os.listdir('test_matrices'):
    print(entry)
    m, n, testMatrix = MatrixReader.read('test_matrices/' + entry)
    print('matrixSize ' + str(rectSize(m, n, testMatrix)))
    print('--')
