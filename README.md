# The Four Corners Problem

The *four corners problem* is a 2D pattern matching problem that has frequently appeared in online coding challenges and on interview practice websites.  The *four corners problem* is decidable in O(n \* m) time.

It is related to several well studied problems such as [frequent itemset mining](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.210.7727) and [4-cycle](https://www.sciencedirect.com/science/article/pii/S0304020808730196) as well as problems related to [computational geometry](http://dspace.library.uu.nl/handle/1874/16599).

## Problem Statement

Input: A Boolean matrix M.

Question: Does there exist a rectangle within M whose four corners are 1's?

Answer: True / False

**Example Instance**: 5 x 8 matrix

|        |  c1  |  c2  |  c3  |  c4  |  c5   |  c6  |  c7  |  c8   |
|   ---  | ---  | ---  | ---  | ---  | ---   | ---  | ---  | ---   |
| **r1** | 0    | 0    | 1    | 0    | 0     | 0    | 0    | 1     |
| **r2** | 1    | 0    | 0    | 0    | **1** | 1    | 0    | **1** |
| **r3** | 0    | 0    | 1    | 0    | 0     | 1    | 0    | 0     |
| **r4** | 0    | 0    | 0    | 0    | **1** | 0    | 1    | **1** |
| **r5** | 0    | 0    | 1    | 0    | 0     | 0    | 1    | 1     |

**Example Solution**

Rows 2 & 4, Cols 5 & 8

# Our Algorithm - Runtime O(n \* m)

**Informal Explanation**

Given an m by n Boolean matrix.

First, we want the number of columns to be at most the number of rows. If this is not the case, then simply transpose the matrix and swap the values of m and n. Now, we have n <= m.

Next, create a set of pairs of column indexes. Initially, the set is empty.

Go through entries in the matrix row by row. For each row, add all pairs of column indexes where there is a 1 to the set.

*Note: A common inefficiency is to traverse through every pair of column indexes from each row.  Instead, we convert each row into a set containing all column indexes where there is a 1 so that we can efficiently traverse through pairs of 1's (skipping any pairs with 0).*

If we attempt to add a pair to the set that is already in the set, then we've found a rectangle whose corners are 1's.

Otherwise, if we reach the end, then there is no rectangle whose corners are 1's.

**Runtime Analysis**

This takes O(m \* n + n^2) time because we go through each of the m*n entries at most once and we go through each of the (n choose 2) = O(n^2) pairs of column indexes at most once before finding a rectangle whose corners are 1's.

Since n <= m, this takes O(m \* n) time.

# Code

- C++ code by Niteesh Kumar and Michael Wehar.

- Java code by Michael Wehar (based on papers [1] and [2]).

- Python code primary implementation by Ari Liloia and Michael Wehar (based on papers [1] and [2]).  Alternative implementation by Joseph Swernofsky.

- Additional contributions by Yvo Meeres and Chen Xu.

# License

- MIT

# Related Resources

**The algorithm above is discussed in the following papers**

- [1] F. Mráz, D. Prusa, and M. Wehar. Two-dimensional Pattern Matching against Basic Picture Languages. CIAA 2019.

- [2] D. Prusa and M. Wehar. Complexity of Searching for 2 by 2 Submatrices in Boolean Matrices. DLT 2020.

**The problem is discussed on the following coding websites**

- https://www.geeksforgeeks.org/find-rectangle-binary-matrix-corners-1/

- https://www.tutorialspoint.com/find-if-there-is-a-rectangle-in-binary-matrix-with-corners-as-1-in-cplusplus

- https://www.interviewbit.com/problems/find-rectangle-in-binary-matrix/
