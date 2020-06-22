# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

def rectExists(m, n, matrix):
    # Step 1. Preprocessing step to convert each row into a set of column indexes
    # and each column into a set of row indexes.
    # Use rowSet as variable for rows sets and colSet as variable for column sets.

    # Step 2. We traverse through 1's in our matrix.  We do this row-wise.
    # That means we go through each row and each column index within it's row set.
    # for each rowIndex in range(0, m)
    #   for each colIndex in rowSet[rowIndex]
    #       nextRowIndex = the next row index after rowIndex in colSet[rowIndex] (i.e. min{ z in colSet[rowIndex] | z > rowIndex })
    #       nextColIndex = the next column index after colIndex in colSet[nextRowIndex] (i.e. min{ z in colSet[nextRowIndex] | z > colIndex })
    #       if matrix[rowIndex][nextColIndex] is a 1
    #           return True
    # return False

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
