# Created on 6/1/20
# Author: Ari Liloia and Michael Wehar

import sys
sys.path.insert(1, 'helper_functions')

from matrix_reader import MatrixReader
from primary_implementation_case_1011 import lemma2Exists
from primary_implementation_case_1011 import createNextRightMap
from primary_implementation_case_1011 import createNextDownMap

# Run all test cases
for i in range(1, 10):
    m, n, testMatrix = MatrixReader.read('test_matrices/testMatrix' + str(i) + '.txt')
    result = lemma2Exists(m, n, testMatrix)
    print("Test Case " + str(i) + " | " + str(result) )
