# Created on 7/1/20
# Author: Ari Liloia and Michael Wehar

# Imports
import math

########################
# (1) Helper Functions #
########################

# Creates an m by n matrix with all entries equal to the default value
def createMatrix(rows, cols, defaultValue = -1):
    return [[defaultValue for _ in range(cols)] for _ in range(rows)]

# Returns a new matrix that is the transpose of the original matrix
def transposeMatrix(rows, cols, matrix):
    # Create an empty cols by cols matrix
    transposedMatrix = createMatrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            # Copies data from original matrix to transposed matrix
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix

# Returns a new matrix that is the reflection of the original matrix over
# its bottom edge
def flipMatrixOverBottomEdge(rows, cols, matrix):
    # Create an empty cols by cols matrix
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

##############################
# (2) Algorithm: Square Case #
##############################

def rectExists1001(rows, cols, matrix):
    if rows < 2 or cols < 2: # Trivial case
        return False
    elif rows == cols:
        # Find smallest power of two larger than cols
        k = int(math.ceil(math.log(cols, 2)))
        l = int(math.pow(2, k))
        # Solve problem for square matrix with dummy
        # zero columns and rows appended to the end
        return squareCase(l, matrix)
    elif rows > cols:
        return nonSquareCase(rows, cols, matrix)
    else:
        transposedMatrix = transposeMatrix(rows, cols, matrix)
        return nonSquareCase(cols, rows, transposedMatrix)

# Requires that cols is a power of 2
def squareCase(cols, matrix):
    # Recursive base case
    if cols < 2:
        return False

    # cols / 2 will be a integer because cols is a power of 2
    halfOfCols = int(float(cols) / 2)

    # Horizontal Split
    topMatrix = block(0, 0, halfOfCols, cols, matrix)
    bottomMatrix = block(halfOfCols, 0, halfOfCols, cols, matrix)

    # Top and Bottom Vertical Splits
    topLeftMatrix = block(0, 0, halfOfCols, halfOfCols, topMatrix)
    topRightMatrix = block(0, halfOfCols, halfOfCols, halfOfCols, topMatrix)
    bottomLeftMatrix = block(0, 0, halfOfCols, halfOfCols, bottomMatrix)
    bottomRightMatrix = block(0, halfOfCols, halfOfCols, halfOfCols, bottomMatrix)

    # Recursive step - 4 square cases and 3 split cases
    # def splitCase(rows, cols, topMatrix_beforeFlip, bottomMatrix_beforeFlip, boundaryOrientation):
    return squareCase(halfOfCols, topLeftMatrix) or squareCase(halfOfCols, topRightMatrix) \
        or squareCase(halfOfCols, bottomLeftMatrix) or squareCase(halfOfCols, bottomRightMatrix) \
        or splitCaseVertical(halfOfCols, halfOfCols, topLeftMatrix, topRightMatrix) \
        or splitCaseVertical(halfOfCols, halfOfCols, bottomLeftMatrix, bottomRightMatrix) \
        or splitCaseHorizontal(halfOfCols, cols, topMatrix, bottomMatrix)

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
    return compareColumnPairMaps(cols, topMatrixAfterFlip, topMatrixAfterFlipMap, bottomMatrix, bottomMatrixMap)

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

# For every pair of columns, checks whether firstMatrix contains (1, 0) pattern
# and second matrix contains (0, 1) pattern
def compareColumnPairMaps(cols, firstMatrix, firstMatrixMap, secondMatrix, secondMatrixMap):
    for i in range(cols):
        for j in range(i + 1, cols):
            firstRow = firstMatrixMap[i][j]
            secondRow = secondMatrixMap[i][j]
            if firstRow != -1 and secondRow != -1 \
              and firstMatrix[firstRow][i] == 1 and firstMatrix[firstRow][j] == 0 \
              and secondMatrix[secondRow][i] == 0 and secondMatrix[secondRow][j] == 1:
               return True
    return False

##################################
# (3) Algorithm: Non-Square Case #
##################################

# Assumes that rows > cols
def nonSquareCase(rows, cols, matrix):
    # Number of square matrices
    d = int(math.ceil(float(rows) / cols))
    # Create a list of square matrices and check if they contain the 1001 patten
    listOfSquareMatrices = []
    for i in range(d):
        squareMatrix = block(i * cols, 0, cols, cols, matrix)
        if squareCase(cols, squareMatrix):
            return True
        else:
            listOfSquareMatrices.append(squareMatrix)
    # Check horizontal split cases
    aggregateMap = createMatrix(cols, cols)
    # For loop counting down from d - 1 to 0 (excluding 0)
    for i in range(d - 1, 0, -1):
        # Flip top matrix
        topMatrixAfterFlip = flipMatrixOverBottomEdge(cols, cols, listOfSquareMatrices[i - 1])
        # Compute column pair maps
        topMatrixAfterFlipMap = computeColumnPairMap(cols, cols, topMatrixAfterFlip)
        bottomMatrixMap = computeColumnPairMap(cols, cols, listOfSquareMatrices[i])
        # Combine aggregate map with new bottom map
        rowOffset = i * cols
        aggregateMap = combineColumnPairMaps(rowOffset, cols, bottomMatrixMap, aggregateMap)
        # Compare maps
        if compareColumnPairMaps(cols, topMatrixAfterFlip, topMatrixAfterFlipMap, matrix, aggregateMap):
            return True
    return False

# Combines together the column pair maps from two different matrices
# It prioritizes that values from the first matrix's map
def combineColumnPairMaps(rowOffset, cols, firstMatrixMap, secondMatrixMap):
    aggregateMap = createMatrix(cols, cols)
    for i in range(cols):
        for j in range(i + 1, cols):
            firstRow = firstMatrixMap[i][j] # One cols by cols matrix on top
            secondRow = secondMatrixMap[i][j] # Many cols by cols matrices stacked below
            if firstRow != -1:
                aggregateMap[i][j] = firstRow + rowOffset
            elif secondRow != -1:
                aggregateMap[i][j] = secondRow
    return aggregateMap
