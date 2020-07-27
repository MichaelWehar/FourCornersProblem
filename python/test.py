# Created on 6/1/20
# Author: Ari Liloia and Michael Wehar

import sys
sys.path.insert(1, 'helper_functions')

from matrix_reader import MatrixReader
# Case 1111
from primary_implementation_case_1111 import rectExists
from alternative_implementation_case_1111 import altRectExists
# Case 1011
from primary_implementation_case_1011 import rectExists1011
# Case 1001
from primary_implementation_case_1001 import rectExists1001


# Run all nine test cases
for i in range(1, 13):
    m, n, testMatrix = MatrixReader.read('test_matrices/testMatrix' + str(i) + '.txt')
    result_1111 = rectExists(m, n, testMatrix)
    altResult_1111 = altRectExists(m, n, testMatrix)
    result_1011 = rectExists1011(m, n, testMatrix)
    result_1001 = rectExists1001(m, n, testMatrix)
    print("Test Case " + str(i) + " \t Primary 1111: " + str(result_1111) + " \t Alternative 1111: " + str(altResult_1111) + " \t Primary 1011: " + str(result_1011) + " \t Primary 1001: " + str(result_1001))
