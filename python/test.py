# Created on 6/1/20
# Author: Ari Liloia and Michael Wehar

import sys
sys.path.insert(1, 'helper_functions')

from matrix_reader import MatrixReader
from primary_implementation import rectExists
from alternative_implementation import altRectExists

# Run all six test cases
for i in range(1, 7):
    m, n, testMatrix = MatrixReader.read('test_matrices/testMatrix' + str(i) + '.txt')
    result = rectExists(m, n, testMatrix)
    altResult = altRectExists(m, n, testMatrix)
    print("Test Case " + str(i) + " | Primary: " + str(result) + " | Alternative: " + str(altResult))
