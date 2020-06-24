# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

def lemma2Exists(m, n, matrix):

    # Step 1. Preprocessing step to convert each row into a set of column indexes
    # and each column into a set of row indexes.
    # Use rowSet as variable for rows sets and colSet as variable for column sets.

    #Preprocessing step to convert each row into a set of column indices
    # and each column into a set of row indices.
    #ColIndicesInRow = [set() for _ in range(m)]
    #RowIndicesInCol = [set() for _ in range(n)]

    colIndicesInRow = [[] for _ in range(m)]
    rowIndicesInCol = [[] for _ in range(n)]
    colIndicesInRow_zeros = [[] for _ in range(m)]
    rowIndicesInCol_zeros = [[] for _ in range(n)]



    for i in range(m):
        for j in range(n):
            if(matrix[i][j] == True):
                colIndicesInRow[i].append(j)
                rowIndicesInCol[j].append(i)
                colIndicesInRow_zeros[i].append(j)
                rowIndicesInCol_zeros[j].append(i)
            else:
                colIndicesInRow_zeros[i].append(0)
                rowIndicesInCol_zeros[j].append(0)







    # Step 2. We traverse through 1's in our matrix.  We do this row-wise.
    # That means we go through each row and each column index within it's row set.
    # for each rowIndex in range(0, m)
    for rowIndex in range(m):
    #   for each colIndex in rowSet[rowIndex]
        for colIndex in range(len(colIndicesInRow[rowIndex])):
    #       nextRowIndex = the next row index after rowIndex in colSet[rowIndex] (i.e. min{ z in colSet[rowIndex] | z > rowIndex })
            nextRowIndex = min(colIndicesInRow_zeros[rowIndex][colIndex:])
    #       nextColIndex = the next column index after colIndex in colSet[nextRowIndex] (i.e. min{ z in colSet[nextRowIndex] | z > colIndex })
            nextColIndex = min(rowIndicesInCol_zeros[nextRowIndex][colIndex:])
    #       if matrix[rowIndex][nextColIndex] is a 1
    #       AND if matrix[nextRowIndex][nextColIndex] = 0
    #           return True
    # return False
            if (matrix[rowIndex][nextColIndex] == True):
               return True
    return False

# Discussion 1 : What is the algorithm
# For each 1 in the matrix, we draw an L vertically (top-down) and then horizontally (left-right).
# Finally, check that that top right corner is a 0.
#
# Pick
# 1
# .
# .
# 0*
# .
# .
# 1..0*..1

# Discussion 2 : Important property that makes this work:
# If one of these exist:
# 1...0
# .   .
# .   .
# .   .
# 1...1
#
# Then, one of these exist:
# 1.....0
# 0     .
# .     .
# .     .
# .     .
# 0     .
# 10...01
# That is, a submatrix matching the corner pattern with 0's on the left side and on the bottom
# 10*1 is the pattern for left side and bottom




#random notes
#a way in python to check if something exists, like a bucket - might
#be good for times when we want to know where boundaries are,
#better to start at left bottom corner? maybe a little less convoluted


#a way to find the minimum as described in the pseudocode:
#during preprocessing step, for each row or column that we tun into a list of column or row indices,
#create a 1D array where buckets that don't have 1s are 0s and buckets that do have 1s have their index.
#that way we can use the built in python min function and slice
