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
    if m < 2 or n < 2: # Trivial case
        return False
    elif m == n:
        # Find smallest power of two larger than n
        k = int(math.ceil(math.log(n, 2)))
        l = int(math.pow(2, k))
        # Solve problem for square matrix with dummy
        # zero columns and rows appended to the end
        return squareCase(l, matrix)
    elif m > n:
        return nonSquareCase(m, n, matrix)
    else:
        transposedMatrix = transposeMatrix(m, n, matrix)
        return nonSquareCase(n, m, transposedMatrix)

# Requires that n is a power of 2
def squareCase(n, matrix):
    # Recursive base case
    if n < 2:
        return False

    # n / 2 will be a integer because n is a power of 2
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
    # Top matrix is where we look for (1, 0) and
    # Bottom matrix is where we look for (0, 1) pattern
    topMatrix = transposeMatrix(rows, cols, leftMatrix)
    bottomMatrix = transposeMatrix(rows, cols, rightMatrix)
    return splitCaseHorizontal(cols, rows, topMatrix, bottomMatrix)

# Build up column pair maps of the row closest to the boundary where entries
# differ, then iterate through and compare the maps
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

##########################################

# Used for augmenting the top matrix map for the case of m > n matrix
# Differences between addToColumnPairMap and computeColumnPairMap:
# computeColumnPairMap starts by defining a matrix to be used as a new map,
# addToColumnPairMap takes as an argument a matrix to be augmented
# in computeColumnPairMap, the values placed into topMatrixAfterFlipMap
# reference row indexes of topMatrixAfterFlip
# in addToColumnPairMa, the values placed into topMatrixAfterFlipMap
# reference row indexes of the original matrix input to rectExists1001
#
# ask mike: could we use naming convention "local row index" vs "global row index" when
# referring to a row of topMatrix? local row index being row index within topMatrixAfterFlip,
# global row index being row index within original matrix input to rectExists1001
def addToColumnPairMap(rows, cols, matrix, columnPairMap, currentIndex):
    #columnPairMap = createMatrix(cols, cols)
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
                        # given the index of the current top matrix in the list of
                        # square matrices(currentIndex) and the current row of the flipped
                        # top matrix being examined (i), put into the column pair map the row
                        # of the full matrix, not just the top matrix, at which a difference
                        # between column indexes was found.
                        columnPairMap[a][b] = ((currentIndex + 1) * cols) - (i + 1)
                        # show Mike on paper how this works when we go over this part
            if len(zeroSet) >= 2:
                newListOfSets.append(zeroSet)
            if len(oneSet) >= 2:
                newListOfSets.append(oneSet)
        listOfSets = newListOfSets
        i += 1
    return columnPairMap

# Assumes that m > n
# differences between splitCaseHorizontal and splitCaseHorizontal_nonSquareCase
# splitCaseHorizontal_nonSquareCase takes two additional inputs: "currentIndex" which is used in addToColumnPairMap
# to calculate global row index from local row index, and "fullMatrix" (aka the original matrix input to rectExists1001).
# We reference the original full matrix instead of the partial top matrix in the last step.
# we also return an additional value: the augmented topMatrixAfterFlipMap
def splitCaseHorizontal_nonSquareCase(rows, cols, topMatrix, bottomMatrix, previousTopMap, currentIndex, fullMatrix):
    # Bottom matrix is where we look for (0, 1) pattern and
    # top matrix is where we look for (1, 0)
    topMatrixAfterFlip = flipMatrixOverBottomEdge(rows, cols, topMatrix)
    # Add to existing top matrix column pair map
    topMatrixAfterFlipMap = addToColumnPairMap(rows, cols, topMatrixAfterFlip, previousTopMap, currentIndex)
    # Compute new bottom matrix column pair map
    bottomMatrixMap = computeColumnPairMap(rows, cols, bottomMatrix)
    # Compare top and bottom maps
    for i in range(cols):
        for j in range(i + 1, cols):
            tRow = topMatrixAfterFlipMap[i][j]
            bRow = bottomMatrixMap[i][j]
            if tRow != -1 and bRow != -1 \
              and fullMatrix[tRow][i] == 1 and fullMatrix[tRow][j] == 0 \
              and bottomMatrix[bRow][i] == 0 and bottomMatrix[bRow][j] == 1:
               return True, topMatrixAfterFlipMap
    return False, topMatrixAfterFlipMap

# Assumes that m > n
def nonSquareCase(m, n, matrix):
    # Number of square matrices
    d = int(math.ceil(m / n))
    # Create a list of square matrices and check if they contain the 1001 patten
    listOfSquareMatrices = []
    for i in range(d):
        squareMatrix = block(i * n, 0, n, n, matrix)
        if squareCase(n, squareMatrix):
            return True
        else:
            listOfSquareMatrices.append(squareMatrix)
    # Check horizontal split cases
    topColumnPairMap = createMatrix(n, n)
    for i in range(len(listOfSquareMatrices) - 1):
        splitCaseFound, topColumnPairMap = splitCaseHorizontal_nonSquareCase(n, n, listOfSquareMatrices[i], listOfSquareMatrices[i+1], topColumnPairMap, i, matrix)
        if splitCaseFound:
            return True
    return False
