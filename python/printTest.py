def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def createMatrix(m, n, defaultValue = -1):
    return [[defaultValue for _ in range(n)] for _ in range(m)]

matrix = [[0, 1, 0, 0, 1, 0, 0, 1],[0, 1, 1, 1, 0, 1, 1, 0],[1, 0, 1, 1, 0, 1, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 0, 1, 0, 0, 0, 0,],[1, 1, 1, 0, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 0, 1, 0, 1, 1, 0,]]

printMatrix(matrix)


n = 8



def split(matrix, matrixOrientation, boundaryOrientation, n, columnSet, rowIndex):
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
            #print(int(n/2)-rowIndex-1)
            if matrix[i][int(n/2)-rowIndex-1] == 0:
                zeroSet.add(i)
            elif matrix[i][int(n/2)-rowIndex-1] == 1:
                oneSet.add(i)
        elif boundaryOrientation == 'vertical' and matrixOrientation == 'top':
            if matrix[i][rowIndex] == 0:
                zeroSet.add(i)
            elif matrix[i][rowIndex] == 1:
                oneSet.add(i)
    #print("zeroSet")
    #print(zeroSet)
    #print("oneSet")
    #print(oneSet)
    return zeroSet, oneSet

def block(r, c, rows, cols, matrix):
    blockMatrix = createMatrix(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            if (r + i) < len(matrix) and (c + j) < len(matrix[0]):
                blockMatrix[i][j] = matrix[r + i][c + j]
            else:
                blockMatrix[i][j] = 0
                print(str(r+i))
                print(str(rows))
    return blockMatrix

halfOfN = int(n/2)
topMatrix = block(0, 0, halfOfN, n, matrix)
bottomMatrix = block(halfOfN, 0, halfOfN, n, matrix)


leftMatrix = block(0, 0, n, halfOfN, matrix)
rightMatrix = block(0, halfOfN, n, halfOfN, matrix)
print("")
printMatrix(rightMatrix)

listOfSets = [{x for x in range(n)}]
for i in range(int(n/2)):
    print(i)
    newListOfSets = []
    for columnSet in listOfSets:
        zeroSet, oneSet = split(rightMatrix, 'top', 'vertical', n, columnSet, i)
        #if len(zeroSet) > 0 and len(oneSet) > 0:
        #    for x in zeroSet:
        #        for y in oneSet:
        #            check(x, y)

        if len(zeroSet) >= 2:
            newListOfSets.append(zeroSet)
        if len(oneSet) >= 2:
            newListOfSets.append(oneSet)
    listOfSets = newListOfSets
    print(newListOfSets)

#split(rightMatrix, 'top', 'vertical', n, columnSet, 0)
