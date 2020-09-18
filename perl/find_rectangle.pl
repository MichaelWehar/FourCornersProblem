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

my @matrix = FourCornersProblem::Case1111::matrixFile2array;
print Dumper \@matrix;
