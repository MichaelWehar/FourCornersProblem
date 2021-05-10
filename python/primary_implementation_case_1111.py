# Created on 5/21/20
# Author: Ari Liloia and Michael Wehar

# m - row    - y
# n - column - x

def rectExists(m, n, matrix):
    # This set will store pairs of column indexes
    columnPairs = set()
    # Traverse through the matrix row by row
    for i in range(m):
        currentRow = []
        # Traverse through current row's elements to find all 1's (or true entries)
        for j in range(n):
            if matrix[i][j] == True:
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
                    return True
                else:
                    columnPairs.add(currentPair)
    return False
