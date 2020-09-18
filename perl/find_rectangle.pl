#!/usr/bin/env perl
#===============================================================================
#
#         FILE: find_rectangle.pl
#
#        USAGE: ./find_rectangle.pl  
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: eevvoor, 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 09/18/2020 05:32:29 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;

use Data::Dumper qw(Dumper);

use lib "./lib";
use FourCornersProblem::Case1111 qw( readMatrix );

sub rectExists {

    my @matrix = FourCornersProblem::Case1111::matrixFile2array;
print Dumper \@matrix;

    # Traverse through the matrix row by row
    for my $i (0..$#matrix) {
    print "$i $matrix[$i]\n";
    # This set will store pairs of column indexes
    my @columnPairs;
        # Traverse through current row's elements to find all 1's (or true entries)
        my @currentRow;
        for my $j (0..4) {
	    print "element $i $j: $matrix[$i][$j]\n";
	}
    }
}

## def rectExists(m, n, matrix):
    # This set will store pairs of column indexes
##    columnPairs = set()
    # Traverse through the matrix row by row
##    for i in range(m):
##        currentRow = []
        # Traverse through current row's elements to find all 1's (or true entries)
##        for j in range(n):
##            if matrix[i][j] == True:
##                currentRow.append(j)
        # Efficiently traverse through pairs of column indexes with 1's (or true entries)
        # First, iterate over all possible entries containing 1 (or true)
##        for firstIndex in range(len(currentRow)):
##            firstElement = currentRow[firstIndex]
            # Next, iterate over all possible next entries containing 1 (or true)
##            for nextIndex in range(firstIndex + 1, len(currentRow)):
##                nextElement = currentRow[nextIndex]
                # print((firstElement * n) + nextElement)
                # Encode a pair (firstElement, nextElement) as (firstElement * n) + nextElement
##                currentPair = (firstElement * n) + nextElement
##                if(currentPair in columnPairs):
                    # print(str(firstElement) + " " + str(nextElement))
##                    return True
##                else:
##                    columnPairs.add(currentPair)
##    return False

rectExists();
