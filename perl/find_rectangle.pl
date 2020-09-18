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
    # This set will store pairs of column indexes
    my @columnPairs;
        # Traverse through current row's elements to find all 1's (or true entries)
        my @currentRow;
        for my $j (0..4) {
	    if ($matrix[$i][$j]) { push @currentRow, $j };
	}
        # Efficiently traverse through pairs of column indexes with 1's (or true entries)
        # First, iterate over all possible entries containing 1 (or true)
	foreach (@currentRow) {
	    my $firstElement; my $nextElement;
                # Encode a pair (firstElement, nextElement) as (firstElement * n) + nextElement
		
        }
    }
    return;
}


rectExists();
