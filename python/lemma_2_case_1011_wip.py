# Created on 6/22/20
# Author: Ari Liloia and Michael Wehar

# Main Function
def lemma2Exists(m, n, matrix):

    # Map any location of a 1 such as (i, j) to the next location of a 1
    # to the right or down
    nextOneRight = []
    nextOneDown = []
    # Create the nextOneRight map with row-wise traversal
    prevEntry = []
    for i in range(m):
        for j in range(n):
            nextOneRight[i * n + j] = -1
            if matrix[i][j] == True:
                if len(prevEntry) != 2:
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    nextOneRight[prevRowIndex * n + prevColIndex] = j
                    prevEntry = [i, j]
    # Create the nextOneDown map with col-wise traversal
    prevEntry = []
    for j in range(n):
        for i in range(m):
            nextOneDown[i * n + j] = -1
            if matrix[i][j] == True:
                if len(prevEntry) != 2:
                    prevRowIndex = prevEntry[0]
                    prevColIndex = prevEntry[1]
                    nextOneDown[prevRowIndex * n + prevColIndex] = i
                    prevEntry = [i, j]
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
