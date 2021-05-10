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

use FourCornersProblem::MatrixInput qw( readMatrix );

sub rectExists {

    my $n = 5;
    my @matrix = FourCornersProblem::MatrixInput::matrixFile2array;
# print Dumper \@matrix;

    # Traverse through the matrix row by row
    for my $i (0..$#matrix) {   # loop through matrix' rows
        # This set will store pairs of column indexes
        my %columnPairs;
        # Traverse through current row's elements to find all 1's (or true entries)
        my @currentRow;
        for my $j (0..$n-1) {
	    if ($matrix[$i][$j]) { push @currentRow, $j };
	}
        # Efficiently traverse through pairs of column indexes with 1's (or true entries)
        # First, iterate over all possible entries containing 1 (or true)
	for my $firstIndex (0..$#currentRow-1) { # TODO call last at second last element
	    my $firstElement = $currentRow[$firstIndex]; # print $firstElement;
            # Next, iterate over all possible next entries containing 1 (or true)
	    for my $nextIndex ($firstIndex+1..$#currentRow){ 
	        my $nextElement = $currentRow[$nextIndex];
                # Encode a pair (firstElement, nextElement) as (firstElement * n) + nextElement
		my $currentPair = ($firstElement * $n) + $nextElement;
		return if exists $columnPairs{$currentPair};
                $columnPairs{$currentPair} = 1; # save it in a hash since you cannot grep through perl arrays 
	    }
        }
    }
    return;
}


rectExists();
