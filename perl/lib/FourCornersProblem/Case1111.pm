package FourCornersProblem::MatrixInput;

use 5.006;
use strict;
use warnings;

use Perl6::Slurp;

=head1 NAME

FourCornersProblem::MatrixInput - The great new FourCornersProblem::MatrixInput!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';
our $dimension;
our @matrix;
our $matrixFile = "../python/test_matrices/testMatrix1.txt";

=head1 SYNOPSIS

This module provides algorithms for the Four Corners Problem.

=head1 EXPORT

A list of the algorithms the module provides. TODO

=head1 SUBROUTINES/METHODS

=head2 readMatrix

=cut

sub readMatrix {
    my $matrix = slurp "../python/test_matrices/testMatrix1.txt";
    return $matrix;
}

=head2 matrixFile2array

=cut

sub matrixFile2array {
    open my $MATRIXFILE, '<', $matrixFile
        or die "Couldn't open $matrixFile";
    # TODO parse dimension to two ints
    $dimension = <$MATRIXFILE>; chomp $dimension;
    while ( <$MATRIXFILE> ) {
        chomp;
	push @matrix, [ split ];
    }
    return @matrix;
}

=head2 getDimension

=cut

sub getDimension {
    return $dimension;
}

=head2 getMatrix

=cut

sub getMatrix {
    return @matrix;
}

=head1 AUTHOR

eevvoor, C<< <eevvoor at mailbox.org> >>

=head1 BUGS

Please report any bugs or feature requests to TODO github link


=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc FourCornersProblem::MatrixInput


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<https://rt.cpan.org/NoAuth/Bugs.html?Dist=FourCornersProblem-MatrixInput>

=item * AnnoCPAN: Annotated CPAN documentation

L<http://annocpan.org/dist/FourCornersProblem-MatrixInput>

=item * CPAN Ratings

L<https://cpanratings.perl.org/d/FourCornersProblem-MatrixInput>

=item * Search CPAN

L<https://metacpan.org/release/FourCornersProblem-MatrixInput>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

This software is Copyright (c) 2020 by eevvoor.

This is free software, licensed under:

  The Artistic License 2.0 (GPL Compatible)


=cut

1; # End of FourCornersProblem::MatrixInput
