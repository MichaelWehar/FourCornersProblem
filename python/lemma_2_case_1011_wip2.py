# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

# Create the nextOneRight map with row-wise traversal
def createNextRightMap(m, n, matrix):
    nextOneRight = [None for _ in range(m * n)]
    for i in range(m):
        # fact: before a row is traversed, no 1s have been found yet
        foundOneYet = False
        # fact: before a row is traversed, because no 1s have been found yet,
        # the index of the previous 1 found is NULL
        prevEntry = [None, None]
        # for each element of a row:
        for j in range(n):
            nextOneRight[i * n + j] = -1
            # if a 1 is encountered in row i:
            if matrix[i][j] == True:
                # if a 1 has previously been encountered in row i:
                if foundOneYet:
                    # recall the stored index of the previous 1
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    # map the index of the current 1 to the index of the previous 1
                    nextOneRight[prevRowIndex * n + prevColIndex] = j
                    # store the index of the current 1
                    prevEntry = [i, j]
                # if the current 1 is the first to be detected during a traversal:
                else:
                    # note that a 1 has previously been encountered in row i
                    foundOneYet = True
                    # store the index of the current 1
                    prevEntry = [i, j]
    return nextOneRight

# Create the nextOneDown map with col-wise traversal
def createNextDownMap(m, n, matrix):
    nextOneDown = [None for _ in range(m * n)]
    for j in range(n):
        # fact: before a column is traversed, no 1s have been found yet
        foundOneYet = False
        # fact: before a column is traversed, because no 1s have been found yet,
        # the index of the previous 1 found is NULL
        prevEntry = [None, None]
        # for each element of a column:
        for i in range(m):
            nextOneDown[i * n + j] = -1
            # if a 1 is encountered in column i:
            if matrix[i][j] == True:
                # if a 1 has previously been encountered in column i:
                if foundOneYet:
                    # recall the stored index of the previous 1
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    # map the index of the current 1 to the index of the previous 1
                    nextOneDown[prevRowIndex * n + prevColIndex] = i
                    # store the index of the current 1
                    prevEntry = [i, j]
                # if the current 1 is the first to be detected during a traversal:
                else:
                    # note that a 1 has previously been encountered in column i
                    foundOneYet = True
                    # store the index of the current 1
                    prevEntry = [i, j]
    return nextOneDown


def lemma2Exists(m, n, matrix):

    # Map any location of a 1 such as (i, j) to the next location of a 1
    # to the right or down
    nextOneRight = createNextRightMap(m, n, matrix)
    nextOneDown = createNextDownMap(m, n, matrix)

    # Traverse through the matrix row by row
    for topRow in range(m):
        for leftCol in range(n):
            # First, traverse through the current row's elements to find all 1's (or true entries)
            # 1's found here constitute the top left corner of a possible submatrix
            if matrix[topRow][leftCol] == True:
                # Next, recall the index of the closest true entry below the upper left corner, if one exists
                # 1's found here constitute the bottom left corner of a possible submatrix
                bottomRow = nextOneDown[topRow * n + leftCol]
                if bottomRow != -1 and matrix[bottomRow][leftCol] == True:
                    # Next, recall the index of the closest true entry to the right of the bottom left corner, if one exists
                    # 1's found here constitute the bottom right corner of a possible submatrix
                    rightCol = nextOneRight[bottomRow * n + leftCol]
                    if rightCol != -1 and matrix[bottomRow][rightCol] == True and matrix[topRow][rightCol] == False:
                        # Finally, check that the top right corner of the submatrix defined by the other three indices at which
                        # 1's were found is 0 (or false)
                        return True
    return False
