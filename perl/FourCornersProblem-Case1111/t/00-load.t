#!perl -T
use 5.006;
use strict;
use warnings;
use Test::More;

plan tests => 1;

BEGIN {
    use_ok( 'FourCornersProblem::Case1111' ) || print "Bail out!\n";
}

diag( "Testing FourCornersProblem::Case1111 $FourCornersProblem::Case1111::VERSION, Perl $], $^X" );
