# Created by Joseph Swernofsky
m,n = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(m)]

print(matrix)

def subrect(matrix, m, n):
    # Which rows touch this column
    row_sets = [set() for _ in range(n)]

    for row in range(m):
        union = set()
        for col in range(n):
            if matrix[row][col]:
                # If you see a row twice it's in a 2x2 subrect
                if row_sets[col].intersection(union):
                    #print("row = {}, col = {}".format(row, col))
                    #print("union = {}, to add = {}".format(union, row_sets))
                    return True
                union |= row_sets[col]
                row_sets[col].add(row)
    return False

print(subrect(matrix, m, n))
