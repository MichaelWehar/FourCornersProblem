# Boolean Matrix Rectangle Problem
**Problem Statement**

Find a rectangle whose corners are 1's in a Boolean matrix.

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

**Informal Explanation:**

Given an m by n Boolean matrix.

First, we want the number of columns to be at most the number of rows. If this is not the case, then simply transpose the matrix and swap the values of m and n. Now, we have n <= m.

Next, create a set of pairs of column indexes. Initially, the set is empty.

Go through entries in the matrix row by row. For each row, add all pairs of column indexes where there is a 1 to the set.

**Note:** A common inefficiency is to traverse through every pair of column indexes from each row.  Instead, we convert each row into a set containing all column indexes where there is a 1 so that we can efficiently traverse through pairs of 1's (skiping any pairs with 0).

If we attempt to add a pair to the set that is already in the set, then we've found a rectangle whose corners are 1's.

Otherwise, if we reach the end, then there is no rectangle whose corners are 1's.

# Runtime

This takes O(m\*n + n^2) time because we go through each of the m*n entries at most once and we go through each of the (n choose 2) = O(n^2) pairs of column indexes at most once before finding a rectangle whose corners are 1's.

Since n <= m, this takes O(m\*n) time.

# Code

- Java code by Michael Wehar
(based on **Two-dimensional Pattern Matching against Basic Picture Languages** by *F. Mráz, D. Prusa, and M. Wehar*)

- Python code by Joseph Swernofsky

# License
- MIT
