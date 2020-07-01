# Created on 6/1/20
# Author: Ari Liloia and Michael Wehar

import sys
sys.path.insert(1, 'helper_functions')

from matrix_reader import MatrixReader
# Case 1111
from primary_implementation_case_1111 import rectExists
from alternative_implementation_case_1111 import altRectExists
# Case 1011
from primary_implementation_case_1011 import lemma2Exists
from primary_implementation_case_1011 import createNextRightMap
from primary_implementation_case_1011 import createNextDownMap

# Run all nine test cases
for i in range(1, 10):
    m, n, testMatrix = MatrixReader.read('test_matrices/testMatrix' + str(i) + '.txt')
    result_1111 = rectExists(m, n, testMatrix)
    altResult_1111 = altRectExists(m, n, testMatrix)
    result_1011 = lemma2Exists(m, n, testMatrix)
    print("Test Case " + str(i) + " \t Primary 1111: " + str(result_1111) + " \t Alternative 1111: " + str(altResult_1111) + " \t Primary 1011: " + str(result_1011))
