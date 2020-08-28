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
use FourCornersProblem::Case1111;

use Test::More tests => 1;                      # last test to print

my $matrix = slurp "../../python/test_matrices/testMatrix1.txt";
ok(reverse("foobar") eq "raboof", "'foobar' rueckwaerts ist 'raboof'");
