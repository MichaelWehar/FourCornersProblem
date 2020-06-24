# Created on Thu May 21 11:11:10 2020
# Author: Ari Liloia
import sys
import os
sys.path.insert(1, '../helper_functions')

from matrix_reader import MatrixReader


# Algorithm implementation
def lemma2Min(m, n, matrix):
    # This dictonary will map bijections (keys) to row indices (values)

    isDict = {}
    # Traverse through the matrix col by col

    for i in range(m):
        closest = 0
        if (matrix[i][0] == 1):
            closest = 1
        for x in range(1, len(matrix[i])):
            if (matrix[i] == 1):
                isDict[(i*m)+x] = closest
                closest = i+1

    #print("")
    #for i in range(m):
    #    print(matrix[i])

    print(isDict)


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
                    #if the key corresponding to a bijection is already in the dictionary,
                    #use the corresponding value and the current row index to get the height
                    #of the submatrix
                    matrixHeight = i - (columnPairs.get(currentPair)) + 1
                    matrixWidth = nextElement - firstElement + 1
                    return matrixHeight*matrixWidth
                else:
                    columnPairs[currentPair] = i
                    #columnPairs.add(currentPair)
    return 0

#Run all test cases in same file
print('--')
for entry in os.listdir('../test_matrices'):
    print(entry)
    m, n, testMatrix = MatrixReader.read('../test_matrices/' + entry)
    print('matrixSize: ' + str(lemma2Min(m, n, testMatrix)))
    print('--')
