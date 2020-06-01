# Created on 5/27/20
# Author: Ari Liloia and Michael Wehar

class MatrixReader:
    # Private helper method
    @staticmethod
    def _createEmptyArray(m):
        return [False for _ in range(m)]
    # Public method
    @staticmethod
    def read(filename):
        #open files with the following convention:
        #first line: rows (m), columns (n)
        #subsequent lines: m by n matrix of ones and zeros

        #read the first line of the file, containing m, n
        matrixFile = open(filename, "r")
        #convert m, n into integers
        mRowsString, mColsString = matrixFile.readline().split()
        mRows = int(mRowsString)
        mCols = int(mColsString)
        #create an empty 1d array with m rows
        returnMatrix = MatrixReader._createEmptyArray(mRows)
        rowIndex = 0
        #for each subsequent line in the file (each line of the matrix)
        for line in matrixFile:
            #split each row into an array of integer ones and zeros
            matrixRow = [int(x) for x in line.split()]
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
        matrixFile.close()
        #close matrix file
        return mRows, mCols, returnMatrix
        #If there are too many rows, an error message will be displayed in the terminal
        #because nonexistent buckets of the matrix will be accessed.
