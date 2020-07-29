# Created on 7/1/20
# Author: Ari Liloia and Michael Wehar

# Imports
import math

########################
# (1) Helper Functions #
########################

# Creates an m by n matrix with all entries equal to the default value
def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(int(n))] for _ in range(int(m))]

# Returns a new matrix that is the transpose of the original matrix
def transposeMatrix(rows, cols, matrix):
    # Create an empty n by m matrix
    transposedMatrix = createMatrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            # Copies data from original matrix to transposed matrix
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix

# Returns a new matrix that is the reflection of the original matrix over
# its bottom edge
def flipMatrixOverBottomEdge(rows, cols, matrix):
    # Create an empty n by m matrix
    flippedMatrix = createMatrix(rows, cols)
    for i in range(rows):
        flippedMatrix[i] = matrix[rows - i - 1]
    return flippedMatrix

# Creates a new matrix that is a specific block from the original matrix
# The block starts at row r and column c and extends for a specified
# number of rows and columns
def block(r, c, rows, cols, matrix):
    blockMatrix = createMatrix(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            if (r + i) < len(matrix) and (c + j) < len(matrix[0]):
                blockMatrix[i][j] = matrix[r + i][c + j]
            else:
                blockMatrix[i][j] = 0
    return blockMatrix

#################
# (2) Algorithm #
#################

def rectExists1001(m, n, matrix):
    # Trivial case
    if m < 2 or n < 2:
        return False
    # Non-trivial cases
    if m == n:
        # Find smallest power of two larger than n
        k = int(math.ceil(math.log(n, 2)))
        l = int(math.pow(2, k))
        # Solve problem for square matrix with dummy
        # zero columns and rows appended to the end
        return squareCase(l, matrix)
    # case 1: square matrix
        # initialize top mapping array
        # initialize bottom mapping array
        #
    return False

# Requires that n is a power of 2
def squareCase(n, matrix):
    # Recursive base case
    if n < 2:
        return False

    #halfOfN = int(n / 2) # Divides evenly because n is a power of 2
    halfOfN = int(n / 2)

    # Horizontal Split
    topMatrix = block(0, 0, halfOfN, n, matrix)
    bottomMatrix = block(halfOfN, 0, halfOfN, n, matrix)
    # Top and Bottom Vertical Splits
    topLeftMatrix = block(0, 0, halfOfN, halfOfN, topMatrix)

    topRightMatrix = block(0, halfOfN, halfOfN, halfOfN, topMatrix)
    bottomLeftMatrix = block(0, 0, halfOfN, halfOfN, bottomMatrix)
    bottomRightMatrix = block(0, halfOfN, halfOfN, halfOfN, bottomMatrix)

    # Recursive step - 4 square cases and 3 split cases
    # def splitCase(rows, cols, topMatrix_beforeFlip, bottomMatrix_beforeFlip, boundaryOrientation):
    return squareCase(halfOfN, topLeftMatrix) or squareCase(halfOfN, topRightMatrix) \
        or squareCase(halfOfN, bottomLeftMatrix) or squareCase(halfOfN, bottomRightMatrix) \
        or splitCaseVertical(halfOfN, halfOfN, topLeftMatrix, topRightMatrix) \
        or splitCaseVertical(halfOfN, halfOfN, bottomLeftMatrix, bottomRightMatrix) \
        or splitCaseHorizontal(halfOfN, n, topMatrix, bottomMatrix)

# Given an array "row" of length "cols" consisting of 0's and 1's and a set of
# column indexes "columnSet", we split columnSet into two sets zeroSet, oneSet
# zeroSet contains indexes with 0 in row
# oneSet contains indexes with 1 in row
def splitColumnSet(row, columnSet):
    # initialize empty sets
    zeroSet = set()
    oneSet = set()
    # iterate through indexes specified in columnSet
    for i in columnSet:
        # add indexes containing 0 to zeroSet and indexes containing 1 to oneSet
        if row[i] == 0:
            zeroSet.add(i)
        elif row[i] == 1:
            oneSet.add(i)
    return zeroSet, oneSet

# Reads through the matrix from left to right, top to bottom
# For each pair of columns, we identify the first row where they differ in value
def computeColumnPairMap(rows, cols, matrix):
    columnPairMap = createMatrix(cols, cols)
    # Initialize the list of sets so that it contains one set with
    # all of the column indexes
    listOfSets = [set(range(cols))]
    # Go through each row
    i = 0
    while i < rows and len(listOfSets) > 0:
        newListOfSets = []
        for columnSet in listOfSets:
            zeroSet, oneSet = splitColumnSet(matrix[i], columnSet)
            if len(zeroSet) > 0 and len(oneSet) > 0:
                for x in zeroSet:
                    for y in oneSet:
                        a = min(x, y)
                        b = max(x, y)
                        columnPairMap[a][b] = i
            if len(zeroSet) >= 2:
                newListOfSets.append(zeroSet)
            if len(oneSet) >= 2:
                newListOfSets.append(oneSet)
        listOfSets = newListOfSets
        i += 1
    return columnPairMap

# Transpose the top and bottom matrices so that they can be processed as if
# the boundary between them was oriented horizontally
def splitCaseVertical(rows, cols, leftMatrix, rightMatrix):
    # Bottom matrix is where we look for (0, 1) pattern and
    # top matrix is where we look for (1, 0)
    topMatrixTranspose = transposeMatrix(rows, cols, leftMatrix)
    #topMatrixFinal = flipMatrixOverBottomEdge(rows, cols, topMatrixTranspose)
    bottomMatrixTranspose = transposeMatrix(rows, cols, rightMatrix)

    return splitCaseHorizontal(cols, rows, topMatrixTranspose, bottomMatrixTranspose)

# Build up maps of the row closest to the boundary where indices differ,
# then iterate through and compare the maps.
def splitCaseHorizontal(rows, cols, topMatrix, bottomMatrix):
    # Bottom matrix is where we look for (0, 1) pattern and
    # top matrix is where we look for (1, 0)
    topMatrixAfterFlip = flipMatrixOverBottomEdge(rows, cols, topMatrix)
    # Compute column pair maps
    topMatrixAfterFlipMap = computeColumnPairMap(rows, cols, topMatrixAfterFlip)
    bottomMatrixMap = computeColumnPairMap(rows, cols, bottomMatrix)
    # Compare top and bottom maps
    for i in range(cols):
        for j in range(i + 1, cols):
            tRow = topMatrixAfterFlipMap[i][j]
            bRow = bottomMatrixMap[i][j]
            if tRow != -1 and bRow != -1 \
              and topMatrixAfterFlip[tRow][i] == 1 and topMatrixAfterFlip[tRow][j] == 0 \
              and bottomMatrix[bRow][i] == 0 and bottomMatrix[bRow][j] == 1:
               return True
    return False
