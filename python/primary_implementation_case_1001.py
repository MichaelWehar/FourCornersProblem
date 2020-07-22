# Created on 7/1/20
# Author: Ari Liloia and Michael Wehar

# Imports
import math

########################
# (1) Helper Functions #
########################

# this function takes a matrix, its orientation in relation to its corresponding matrix
# (topMatrix or bottomMatrix), the orientation of its boundary (vertical or horizontal)
# n (the number of column indices in the initial set, before the first round of split being called)
# one columnSet (one of the returns from a previous call to this function) and the row
# index of the matrix to examine.
# it returns zeroSet and oneSet, which (?) contain the column indices that differ (badly worded)
def split(matrix, matrixOrientation, boundaryOrientation, n, columnSet, rowIndex):
    # matrixOrientation: is the matrix topMatrix or bottomMatrix?
    # boundaryOrientation: is the boundary betwen the matrices horizontal or vertical?
    # if the boundary orientation is vertical, "topMatrix" is the submatrix on the right.

    zeroSet = set()
    oneSet = set()

    for i in columnSet:
        if boundaryOrientation == 'horizontal' and matrixOrientation == 'bottom':
            if matrix[rowIndex][i] == 0:
                zeroSet.add(i)
            elif matrix[rowIndex][i] == 1:
                oneSet.add(i)
        elif boundaryOrientation == 'horizontal' and matrixOrientation == 'top':
            if matrix[int(n/2)-rowIndex-1][i] == 0:
                zeroSet.add(i)
            elif matrix[int(n/2)-rowIndex-1][i] == 1:
                oneSet.add(i)
        elif boundaryOrientation == 'vertical' and matrixOrientation == 'bottom':
            if matrix[i][n-rowIndex-1] == 0:
                zeroSet.add(i)
            elif matrix[i][n-rowIndex-1] == 1:
                oneSet.add(i)
        elif boundaryOrientation == 'vertical' and matrixOrientation == 'top':
            if matrix[i][rowIndex] == 0:
                zeroSet.add(i)
            elif matrix[i][rowIndex] == 1:
                oneSet.add(i)

    return zeroSet, oneSet

# Creates an m by n matrix with all entries equal to the default value
def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(int(n))] for _ in range(int(m))]

# Returns a new matrix that is the transpose of the original matrix
def transposeMatrix(m, n, matrix):
    # Create an empty n by m matrix
    transposedMatrix = createMatrix(n, m)
    for i in range(n):
        for j in range(m):
            # Copies date from original matrix to transposed matrix
            transposedMatrix[i][j] = matrix[j][i]
    return transposedMatrix

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
    # Computing dimensions of four smaller matrices

    # Recursive base case
    if n < 2:
        return False

    halfOfN = int(n / 2) # Divides evenly because n is a power of 2
    # Horizontal Split
    topMatrix = block(0, 0, halfOfN, n, matrix)
    bottomMatrix = block(halfOfN, 0, halfOfN, n, matrix)
    # Top Vertical Split
    topLeftMatrix = block(0, 0, halfOfN, halfOfN, topMatrix)
    topRightMatrix = block(0, halfOfN, halfOfN, halfOfN, topMatrix)
    # Bottom Vertical Split
    bottomLeftMatrix = block(0, 0, halfOfN, halfOfN, bottomMatrix)
    bottomRightMatrix = block(0, halfOfN, halfOfN, halfOfN, bottomMatrix)
    # Recursive step
    return squareCase(halfOfN, topLeftMatrix) or squareCase(halfOfN, topRightMatrix) or squareCase(halfOfN, bottomLeftMatrix) or squareCase(halfOfN, bottomRightMatrix) or splitCase(halfOfN, n, topMatrix, bottomMatrix, 'horizontal')


def splitCase(rows, cols, topMatrix, bottomMatrix, boundaryOrientation):

    topMatrixMap = {}

    if boundaryOrientation == 'horizontal':
        listOfSets = [{x for x in range(cols)}]
        n = cols
    elif boundaryOrientation == 'vertical':
        listOfSets = [{x for x in range(rows)}]
        n = rows

    for i in range(int(n/2)):
        newListOfSets = []
        for columnSet in listOfSets:
            zeroSet, oneSet = split(topMatrix, 'top', boundaryOrientation, n, columnSet, i)
            if len(zeroSet) > 0 and len(oneSet) > 0:
                for x in zeroSet:
                    for y in oneSet:


                        topMatrixMap[(x,y)] = i


            if len(zeroSet) >= 2:
                newListOfSets.append(zeroSet)
            if len(oneSet) >= 2:
                newListOfSets.append(oneSet)
        listOfSets = newListOfSets

    if boundaryOrientation == 'horizontal':
        listOfSets = [{x for x in range(cols)}]
    elif boundaryOrientation == 'vertical':
        listOfSets = [{x for x in range(rows)}]

    for i in range(int(n/2)):
        newListOfSets = []
        for columnSet in listOfSets:
            zeroSet, oneSet = split(bottomMatrix, 'bottom', boundaryOrientation, n, columnSet, i)
            if len(zeroSet) > 0 and len(oneSet) > 0:
                for x in zeroSet:
                    for y in oneSet:
                        if (y,x) in topMatrixMap and boundaryOrientation == 'horizontal':
                            return True
                        elif (x,y) in topMatrixMap and boundaryOrientation == 'vertical':
                            return True

            if len(zeroSet) >= 2:
                newListOfSets.append(zeroSet)
            if len(oneSet) >= 2:
                newListOfSets.append(oneSet)
    listOfSets = newListOfSets





# 0 : 0 1 0 0 0 1 0 1
# 1 : 1 0 1 1 0 0 0 0
# 2 : 0 1 0 1 1 0 1 0
# 3 : 1 0 0 1 0 1 0 0


#strategy - lemma 3 case 1,
#iterate through rows - we are looking for (0, 1) pattern
# initialize X_current = {0 .. n}
# for each row (from middle to top or middle to bottom of M): [O(m/2)]
#   X = {}
#   iterate through elements 0..n to get A0, A1 [O(n)]
#   for S in X_current: [O(?)]
#       S0 = A0.intersection(S)
#       S1 = A1.intersection(S)
#       for all in S0:
#           for all in S1:
#               map(S0, S1) //mapping not yet worked out, notes below
#       if(len(S0)) >= 2:
#           X.add(S0)
#       if(len(S1)) >= 2:
#           X.add(S1)
#   X_current = X


# ideas:
# X could be a queue containing sets. At the beginning of every loop through
# a new row we check its size then go through it that many times. might
# take less time than making new empty set every time we loop?





# row 3
# X = { {0 1 2 3 4 5 6 7} }
# A0 = { 1 2 4 6 7 }, A1 = { 0 3 5 }

# One set in X: S = {0 1 2 3 4 5 6 7}
# S0 = { 1 2 4 6 7 }, S1 = { 0 3 5 }
# 15 mappings done

# row 2
# X = { S_A = { 1 2 4 6 7 }, S_B = { 0 3 5 } }
# A0 = { 0 2 5 7 }, A1 = { 1 3 4 6 }

# S_A:
# S0 = S_A cap A0 = { 2 7 }, S1 = { 1 4 6 }
# 6 mappings done


# S_B:
# S0 = S_B cap A0 = { 0 5 }, S1 = { 3 }
# 2 mappings done

# row 1
# X = { S_A = { 2 7 }, S_B = { 1 4 6 }, S_C = { 0 5 } }
# A0 = { 1 4 5 6 7 }, A1 = { 0 2 3 }

# S_A:
# S0 = { 7 }, S1 = { 2 }
# 1 mapping done

# S_B:
# S0 = { 1 4 6 }, S1 = { }
# 0 mappings done

# S_C:
# S0 = { 5 }, S1 = { 0 }
# 1 mapping done

# row 0
# X = { {1 4 6} }
# A0 = { 0 2 3 4 6 }, A1 = { 1 5 7 }
# One set in X:  S = {1 4 6}
# S0 = { 4 6 }, S1 = { 1 }
# 2 mappings done

# reached the end
# X = { {4 6} } // note columns 4 and 6 are the same
# 27 mappings done

# ---

# total of 27 mappings done
# if there are n columns in topMatrix, the number of possible combinations of different indices is ( n! ) / ( 2 * (n - 2)! )




# what kind of mapping?

#lets say we're on row 2
# S0 = S_A cap A0 = { 2 7 }, S1 = { 1 4 6 }

# make mapping for {2 1}
# check out the link i put in google doc - might be a good lead






# would anything change if the matrix has an odd number of rows? topMatrix and bottomMatrix would have to have different numbers of rows

# note: in the paper it is given that S cap A0 = S0, S cap A1 = S1 for each S.
# When working through this example I used SA, SB etc to keep track of multiple S for each row.
# i.e. i got an S0 and an S1 for each SA, SB, SC etc
