# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

########################
# (1) Helper Functions #
########################

# Creates an m by n matrix with all entries equal to the default value
def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(n)] for _ in range(m)]

# Returns a new matrix that is the transpose of the original matrix
def transposeMatrix(m, n, matrix):
    # Create an empty n by m matrix
    transposedMatrix = createMatrix(n, m)
    for i in range(n):
        for j in range(m):
            # Copies date from original matrix to transposed matrix
            transposedMatrix[i][j] = matrix[j][i]
    return transposedMatrix

#####################
# (2) Preprocessing #
#####################

# Returns a map that sends each location (i, j) whose entry is one to
# the next column index where there is a one.
def createNextOneRightMap(m, n, matrix):
    # Creates an m by n matrix
    nextOneRight = createMatrix(m, n)
    for i in range(m):
        # Fact: before a row is traversed, no ones have been found yet
        # We use -1 to denote this initial case
        prevColIndex = -1
        # Iterate over each column index
        for j in range(n):
            # Check if a one is encountered in row i
            if matrix[i][j] == True:
                # Check if a one has previously been encountered in row i
                if prevColIndex != -1:
                    # Map the column index of the previous one to the
                    # column index of the current one
                    nextOneRight[i][prevColIndex] = j
                # Store the column index of the current one
                prevColIndex = j
    return nextOneRight

def createNextOneDownMap(m, n, matrix):
    # The code from createNextOneRightMap can be reused on the transpose
    # of matrix to find the next one down instead of right
    transposedMatrix = transposeMatrix(m, n, matrix)
    resultMap = createNextOneRightMap(n, m, transposedMatrix)
    return transposeMatrix(n, m, resultMap)

#################
# (3) Algorithm #
#################

def rectExists1011(m, n, matrix):
    # Map any location of a one such as (i, j) to the next location
    # of a one to the right or down
    nextOneRight = createNextOneRightMap(m, n, matrix)
    nextOneDown = createNextOneDownMap(m, n, matrix)
    # Traverse through the matrix row by row
    for topRow in range(m):
        for leftCol in range(n):
            # Check if the current entry is a one
            if matrix[topRow][leftCol] == True:
                # Find the next row index with a one entry in the current column
                bottomRow = nextOneDown[topRow][leftCol]
                if bottomRow != -1:
                    # Find the next column index with a one entry in the current row
                    rightCol = nextOneRight[bottomRow][leftCol]
                    # Also, check that the top right corner entry is zero
                    if rightCol != -1 and matrix[topRow][rightCol] == False:
                        return True
    return False
