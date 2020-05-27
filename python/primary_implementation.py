# Created on Thu May 21 11:11:10 2020
# Author: Ari Liloia

# Helper functions
def createEmptyArray(n):
    return [False for _ in range(n)]

def createEmptyMatrix(m, n):
    return [createEmptyArray(n) for _ in range(m)]

# File IO
def importMatrix(filename):
    #open files with the following convention:
    #first line: #rows (m), #columns (n)
    #subsequent lines: m by n matrix of ones and zeros

    #read the first line of the file, containing m, n
    c_file = open(filename, "r")
    #convert m, n into integers
    mRowsString, mColsString = c_file.readline().split()
    mRows = int(mRowsString)
    mCols = int(mColsString)
    #create an empty 1d array with m rows
    returnMatrix = createEmptyArray(mRows)
    rowIndex = 0
    #for each subsequent line in the file (each line of the matrix)
    for line in c_file:
        #split each row into an array of integer ones and zeros
        matrixRow = [ int(x) for x in line.split() ]
        #if the number of buckets in one row is not the number of columns
        #implicated at the top of the file:
        if(len(matrixRow) != mCols):
            #throw an error and return nothing
            print("Error: incorrect number of columns in row " + str(rowIndex))
            return
        returnMatrix[rowIndex] = matrixRow
        #increment the row 'cursor'
        rowIndex = rowIndex + 1
    #if the number of rows accessed so far is not the number of rows
    #implicated at the top of the file:
    if(rowIndex != mRows):
        #throw an error and return nothing
        print("Error: too few rows")
        return
    c_file.close()
    #close matrix file
    return mRows, mCols, returnMatrix
    #If there are too many rows, an error message will be displayed in the terminal
    #because nonexistent buckets of the matrix will be accessed.

m, n, testMatrix = importMatrix('test_matrices/testMatrix1')

def rectExists(m, n, matrix):
    # This set will store pairs of column indexes
    columnPairs = set()
    # Traverse through the matrix row by row
    for i in range(m):
        currentRow = []
        # Traverse through current row's elements to find all 1's (or true entries)
        for j in range(n):
            if(matrix[i][j] == True):
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

print(rectExists(m, n, testMatrix))
