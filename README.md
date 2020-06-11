# The Four Corners Problem

**Problem Statement**

Input: A Boolean matrix M.

Question: Does there exist a rectangle within M whose four corners are 1's?

**Example Instance**

0	0	1	0	0	0	0	1

1	0	0	0	***1***	1	0 ***1***

0	0	1	0	0	1	0	0

0	0	0	0	***1***	0	1	***1***

0	0	1	0	0	0	1	1

**Example Solution**

Rows 2 & 4

Cols 5 & 8

# Our Algorithm

**Informal Explanation**

Given an m by n Boolean matrix.

First, we want the number of columns to be at most the number of rows. If this is not the case, then simply transpose the matrix and swap the values of m and n. Now, we have n <= m.

Next, create a set of pairs of column indexes. Initially, the set is empty.

Go through entries in the matrix row by row. For each row, add all pairs of column indexes where there is a 1 to the set.

*Note: A common inefficiency is to traverse through every pair of column indexes from each row.  Instead, we convert each row into a set containing all column indexes where there is a 1 so that we can efficiently traverse through pairs of 1's (skipping any pairs with 0).*

If we attempt to add a pair to the set that is already in the set, then we've found a rectangle whose corners are 1's.

Otherwise, if we reach the end, then there is no rectangle whose corners are 1's.

**Runtime**

This takes O(m\*n + n^2) time because we go through each of the m*n entries at most once and we go through each of the (n choose 2) = O(n^2) pairs of column indexes at most once before finding a rectangle whose corners are 1's.

Since n <= m, this takes O(m\*n) time.

# Code

- C++ code by Niteesh Kumar and Michael Wehar.

- Java code by Michael Wehar (based on papers [1] and [2]).

- Python code primary implementation by Ari Liloia and Michael Wehar (based on papers [1] and [2]).  Alternative implementation by Joseph Swernofsky.

# License
- MIT

# Related Resources

**Papers**

- [1] F. Mráz, D. Prusa, and M. Wehar. Two-dimensional Pattern Matching against Basic Picture Languages. CIAA 2019.

- [2] D. Prusa and M. Wehar. Complexity of Searching for 2 by 2 Submatrices in Boolean Matrices. DLT 2020.

**Coding websites that mention this problem**

- https://www.geeksforgeeks.org/find-rectangle-binary-matrix-corners-1/

- https://www.tutorialspoint.com/find-if-there-is-a-rectangle-in-binary-matrix-with-corners-as-1-in-cplusplus

- https://www.interviewbit.com/problems/find-rectangle-in-binary-matrix/
