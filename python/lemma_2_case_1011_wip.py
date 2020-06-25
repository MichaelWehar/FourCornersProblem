# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

# Main Function

# Create the nextOneRight map with row-wise traversal
def createNextRightMap(m, n, matrix):
    # Create the nextOneRight map with row-wise traversal
    #need to initialize this array, otherwise
    #we get "list assignment index out of range" error
    nextOneRight = [None for _ in range(m * n)]
    for i in range(m):
        foundOneYet = False
        #we won't be able to map the first 1 we find in a row until
        #we find its closest neighbor to the right
        prevEntry = [None for _ in range(2)]
        #prevEntry needs to be inside the first for loop so it can't be
        #something from the above row. also needs to be initialized so we can
        #index into it
        for j in range(n):
            nextOneRight[i * n + j] = -1
            if matrix[i][j] == True:
                if foundOneYet:
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    nextOneRight[prevRowIndex * n + prevColIndex] = j
                    prevEntry = [i, j]
                else:
                    #if this is the first one we find, don't add anything
                    #to the mapping yet
                    foundOneYet = True
                    prevEntry = [i, j]
    return nextOneRight

# Create the nextOneDown map with col-wise traversal
def createNextDownMap(m, n, matrix):
    nextOneDown = [None for _ in range(m * n)]
    for j in range(n):
        foundOneYet = False
        prevEntry = [None, None]
        for i in range(m):
            nextOneDown[i * n + j] = -1
            if matrix[i][j] == True:
                if foundOneYet:
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    nextOneDown[prevRowIndex * n + prevColIndex] = i
                    prevEntry = [i, j]
                else:
                    foundOneYet = True
                    prevEntry = [i, j]
    return nextOneDown


def lemma2Exists(m, n, matrix):

    # Map any location of a 1 such as (i, j) to the next location of a 1
    # to the right or down
    nextOneRight = createNextRightMap(m, n, matrix)
    nextOneDown = createNextDownMap(m, n, matrix)

    # Search for 1011 submatrix
    for topRow in range(m):
        for leftCol in range(n):
            if matrix[topRow][leftCol] == True:
                bottomRow = nextOneDown[topRow * n + leftCol]
                if bottomRow != -1 and matrix[bottomRow][leftCol] == True:
                    rightCol = nextOneRight[bottomRow * n + leftCol]
                    if rightCol != -1 and matrix[bottomRow][rightCol] == True and matrix[topRow][rightCol] == False:
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


#maybe beter
