# Code written by Joseph Swernofsky
#
# This approach is slightly different from the Java approach
# that is described in the Readme.
#
# Key details:
# (a) We go through the matrix row by row.
# (b) When we encounter a one in the matrix we add its row
# index to the set row_sets[col] where col is the current
# column index.
# (c) For each row, we build up a set union of row indexes
# where there is a one in the same column as a one in the
# current row.
# (d) If we ever have a non-empty intersection between
# row_sets[col] and union, then we've found a 2x2 subrect.
# This is because we have two ones in the current row that
# both have ones above them at a matching row index.
# (e) The runtime is m^2 + m*n. We have m*n because we visit
# every entry in the matrix. We have m^2 because for each
# row we add at most m row indexes to union or else we would
# have found a duplicate meaning that there is a 2x2 subrect.
#
# Note: You need to transpose the matrix if m > n so that the
# runtime is O(m*n).

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
