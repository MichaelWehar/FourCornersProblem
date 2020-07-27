# Created on 7/1/20
# Author: Ari Liloia and Michael Wehar

# Imports
import math

########################
# (1) Helper Functions #
########################

def createEmptyArray(n):
    return [0 for _ in range(n)]

# Creates an m by n matrix with all entries equal to the default value
def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(int(n))] for _ in range(int(m))]

# Returns a new matrix that is the reflection of the original matrix over
# its bottom edge
def flipMatrixOverBottomEdge(matrix, rows, cols):
    # Create an empty n by m matrix
    flippedMatrix = createMatrix(rows, cols)
    for i in range(rows):
        flippedMatrix[i] = matrix[rows-i-1]
    #print("matrix flipped over bottom edge")
    return flippedMatrix

# Returns a new matrix that is the transpose of the original matrix
def transposeMatrix(matrix, rows, cols):
    # Create an empty n by m matrix
    transposedMatrix = createMatrix(cols,rows)
    for i in range(rows):
        for j in range(cols):
            # Copies data from original matrix to transposed matrix
            transposedMatrix[j][i] = matrix[i][j]
    #print("matrix transposed")
    return transposedMatrix

# Returns a new matrix that is the rotation of the original matrix
# 90 degrees clockwise
def rotateMatrixRight(matrix, rows, cols):
    # Create an empty n by m matrix
    rotatedMatrix = createMatrix(cols,rows)
    for i in range(rows):
        for j in range(cols):
            # Copies data from original matrix to transposed matrix
            rotatedMatrix[j][i] = matrix[rows-i-1][j]
    return rotatedMatrix

# Returns a new matrix that is the rotation of the original matrix
# 90 degrees counterclockwise
def rotateMatrixLeft(matrix, rows, cols):
    # call rotateMatrixRight three times
    tempMatrix1 = rotateMatrixRight(matrix,rows,cols)
    tempMatrix2 = rotateMatrixRight(tempMatrix1,cols,rows)
    rotatedMatrix = rotateMatrixRight(tempMatrix2,rows,cols)
    #print("matrix rotated left")
    return rotatedMatrix

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

    halfOfN = int(n / 2) # Divides evenly because n is a power of 2

    # Horizontal Split
    topMatrix = block(0, 0, halfOfN, n, matrix)
    bottomMatrix = block(halfOfN, 0, halfOfN, n, matrix)

    # Top and Bottom Vertical Splits
    topLeftMatrix = block(0, 0, halfOfN, halfOfN, topMatrix)
    topRightMatrix = block(0, halfOfN, halfOfN, halfOfN, topMatrix)
    bottomLeftMatrix = block(0, 0, halfOfN, halfOfN, bottomMatrix)
    bottomRightMatrix = block(0, halfOfN, halfOfN, halfOfN, bottomMatrix)

    # Transpose of Vertical Cases
    #transposeTopLeftMatrix = transposeMatrix(halfOfN, halfOfN, topLeftMatrix)
    #transposeTopRightMatrix = transposeMatrix(halfOfN, halfOfN, topRightMatrix)
    #transposeBottomLeftMatrix = transposeMatrix(halfOfN, halfOfN, bottomLeftMatrix)
    #transposeBottomRightMatrix = transposeMatrix(halfOfN, halfOfN, bottomRightMatrix)

    # Recursive step - 4 square cases and 3 split cases
    # def splitCase(rows, cols, topMatrix_beforeFlip, bottomMatrix_beforeFlip, boundaryOrientation):
    return squareCase(halfOfN, topLeftMatrix) or squareCase(halfOfN, topRightMatrix) \
        or squareCase(halfOfN, bottomLeftMatrix) or squareCase(halfOfN, bottomRightMatrix) \
        or splitCase(halfOfN, halfOfN, topLeftMatrix, topRightMatrix, 'vertical') \
        or splitCase(halfOfN, halfOfN, bottomLeftMatrix, bottomRightMatrix, 'vertical') \
        or splitCase(halfOfN, n, topMatrix, bottomMatrix, 'horizontal')

# given an array "row" with length cols and a set "columnSet" that can contain
# the numbers 0 through cols exclusive, return a set of all the numbers in "columnSet"
# that correspond to indices of "row" containing 0 (zeroSet) and 1 (oneSet)
def splitIndices(row, columnSet):
    # initialize empty sets
    zeroSet = set()
    oneSet = set()
    # iterate through indices specified in columnSet
    for i in columnSet:
        # add indices containing 0 to zeroSet and indices containing 1 to oneSet
        if row[i] == 0:
            zeroSet.add(i)
        elif row[i] == 1:
            oneSet.add(i)
    return zeroSet, oneSet

def computeColumnPairMap(matrix, rows, cols):
    # takes in a matrix of size (rows, cols)
    # reads through the matrix from "top to bottom, left to right"
    columnPairMap = createMatrix(cols, cols)
    #print(columnPairMap)
    # Initialize the list of sets so that it contains one set containing
    # all column indices
    listOfSets = [set(range(cols))]
    # Go through each row
    i = 0
    while i < rows and len(listOfSets) > 0:
        newListOfSets = []
        for columnSet in listOfSets:
            zeroSet, oneSet = splitIndices(matrix[i], columnSet)
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
    #print("one column pair map returned")
    return columnPairMap


def splitCase(rows, cols, topMatrix_beforeFlip, bottomMatrix_beforeFlip, boundaryOrientation):
    # note: bottom matrix is where we look for (0,1) pattern, top matrix is where we look for (1,0)

    if boundaryOrientation == 'horizontal':
        topMatrix = flipMatrixOverBottomEdge(topMatrix_beforeFlip,rows,cols)
        bottomMatrix = bottomMatrix_beforeFlip
    elif boundaryOrientation == 'vertical':
        topMatrix = rotateMatrixLeft(topMatrix_beforeFlip,rows,cols)
        bottomMatrix = transposeMatrix(bottomMatrix_beforeFlip,rows,cols)

    topMatrixMap = computeColumnPairMap(topMatrix, rows, cols)
    #print(topMatrix)
    #print(bottomMatrix)
    bottomMatrixMap = computeColumnPairMap(bottomMatrix, rows, cols)
    #print("topmatrixmap")
    #print(topMatrixMap)
    #print("bottomamatrixmap")
    #print(bottomMatrixMap)
    # Compare top and bottom maps
    for i in range(cols):
        for j in range(i + 1, cols):
            topRow = topMatrixMap[i][j]
            bottomRow = bottomMatrixMap[i][j]
            if topRow != -1 and bottomRow != -1 and topMatrix[topRow][i] == 1 and topMatrix[topRow][j] == 0:
                #print("true")
                return True
    #print("false")
    return False
