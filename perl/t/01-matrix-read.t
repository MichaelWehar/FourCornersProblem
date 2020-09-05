#===============================================================================
#
#         FILE: 01-matrix-read.t
#
#  DESCRIPTION: Read a test matrix from the python tests.
#
#        FILES: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: eevvoor
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 08/29/2020 12:59:19 AM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use Perl6::Slurp;
use lib "./lib";
use FourCornersProblem::Case1111 qw( readMatrix );
use Data::Dumper qw(Dumper);

use Test::More qw( no_plan);                      # last test to print

my $file =  "../python/test_matrices/testMatrix1.txt";
my $matrixA = slurp $file;
# my $matrixC = readMatrix();
my $matrixB = "5 5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 0 0 0 1
";
my @matrix = FourCornersProblem::Case1111::matrixFile2array;
ok($matrixB eq $matrixA, "Matrix read in as string and from file.");
ok(FourCornersProblem::Case1111::readMatrix() eq $matrixA, "Matrix read in as string and from file via modules subroutine.");

isnt(FourCornersProblem::Case1111::getDimension, "5 5\n", "dimension:" . FourCornersProblem::Case1111::matrixFile2array);
is(FourCornersProblem::Case1111::getDimension, "5 5", "dimension:" . FourCornersProblem::Case1111::matrixFile2array);
print Dumper \@matrix;
is($matrix[4][4], 1, "test one matrix entry")
