# Created on 7/1/20
# Author: Ari Liloia and Michael Wehar

# Imports
import math

########################
# (1) Helper Functions #
########################

# Creates an m by n matrix with all entries equal to the default value
def printMatrix(matrix):
    m_rows = len(matrix)
    for i in range(m_rows):
        print(matrix[i])

def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(int(n))] for _ in range(int(m))]

def createEmptyArray(n):
    return [-1 for _ in range(n)]

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

def block(r_f, c_f, rows_f, cols_f, matrix):
    r = int(r_f)
    c = int(c_f)
    rows = int(rows_f)
    cols = int(cols_f)
    blockMatrix = createMatrix(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            if (r + i) < len(matrix) and (c + j) < len(matrix[r + i]):
                blockMatrix[i][j] = matrix[r + i][c + j]
            else:
                blockMatrix[i][j] = -1
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
        k = math.ceil(math.log(n, 2))
        l_f = math.pow(2, k)
        l = int(l_f)
        # Solve problem for square matrix with dummy
        # zero columns and rows appended to the end
        return squareCase(l, matrix)
    # case 1: square matrix
        # initialize top mapping array
        # initialize bottom mapping array
        #

# Requires that n is a power of 2
def squareCase(n, matrix):
    # Computing dimensions of four smaller matrices
    halfOfN = n / 2 # Divides evenly because n is a power of 2
    # Horizontal Split
    topMatrix = block(0, 0, halfOfN, n, matrix)
    print("topMatrix")
    printMatrix(topMatrix)
    bottomMatrix = block(halfOfN, 0, halfOfN, n, matrix)
    print("bMatrix")
    printMatrix(bottomMatrix)

    # Top Vertical Split
    topLeftMatrix = block(0, 0, halfOfN, halfOfN, topMatrix)
    topRightMatrix = block(0, halfOfN, halfOfN, halfOfN, topMatrix)
    # Bottom Vertical Split
    bottomLeftMatrix = block(0, 0, halfOfN, halfOfN, bottomMatrix)
    bottomRightMatrix = block(0, halfOfN, halfOfN, halfOfN, bottomMatrix)
    # Recursive step





    return squareCase(halfOfN, topLeftMatrix) or squareCase(halfOfN, topRightMatrix) or squareCase(halfOfN, bottomLeftMatrix) or squareCase(halfOfN, bottomRightMatrix) or splitCase(halfOfN, n, topMatrix, bottomMatrix)




def splitCase(rows, cols, topMatrix, bottomMatrix):


    topMatrixMap = createEmptyArray(n*n)
    for i in range(rows):
        currentRow = rows - i - 1
        onesInRow = set()
        for j in range(cols):
            if topMatrix[currentRow][j] == 1:
                onesInRow.add(i)
            if topMatrix[currentRow][j] == 0:
                for x in onesInRow:
                    if topMatrixMap[(x*cols)+j] == 0:
                        topMatrixMap[(x*cols)+j] = currentRow

    for i in range(rows):
        currentRow = i
        zerosInRow = set()
        for j in range(cols):
            if bottomMatrix[currentRow][j] == 0:
                zerosInRow.add(i)
            if bottomMatrix[currentRow][j] == 1:
                for x in zerosInRow:
                    if topMatrixMap[(x*cols)+j] == 1:
                        return True

    return False



    """
    topMatrixMap = createEmptyArray(n*n)

    unchecked = [set() for _ in range(n)]
    for u in range(n):
        for v in range(n):
            unchecked[u].add(v)
        unchecked[u].remove(u)

    # O(n) work per row (nested for loops)
    for i in range(rows):
        currentRow = rows - i - 1
        onesInRow = set()
        for j in range(cols):
            if topMatrix[currentRow][j] == 1 and len(unchecked[j]) != 0:
                onesInRow.add(i)
            if topMatrix[currentRow][j] == 0:
                for x in onesInRow:
                    # note that createEmptyArray's default value is -1
                    if topMatrixMap[(x*cols)+j] == -1:
                        topMatrixMap[(x*cols)+j] = currentRow
                        unchecked[x].remove(j)
                        unchecked[j].remove(x)
                        print(unchecked)
    """




###

    # build map for topMatrix
    # since we're dividing a square matrix at a horizontal boundary across which the square created by the
    # edges of the full square matrix would be symmetric, we know that cols = rows * 2

    #mapTopMatrix = createEmptyArray(cols * cols)
    #for i in range(rows):
#        # start at the row just above the boundary between bottomMatrix and topMatrix#
#        currentRow = rows - i - 1
        # iterate across each row
#        for j in range(cols):





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
