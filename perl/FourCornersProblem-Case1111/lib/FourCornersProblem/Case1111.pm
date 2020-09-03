package FourCornersProblem::Case1111;

use 5.006;
use strict;
use warnings;

use Perl6::Slurp;

=head1 NAME

FourCornersProblem::Case1111 - The great new FourCornersProblem::Case1111!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';


=head1 SYNOPSIS

This module provides algorithms for the Four Corners Problem.

=head1 EXPORT

A list of the algorithms the module provides. TODO

=head1 SUBROUTINES/METHODS

=head2 readMatrix

=cut

sub readMatrix {
    my $matrix = slurp "../../python/test_matrices/testMatrix1.txt";
    return $matrix;
}

=head2 matrixFile2array

=cut

sub matrixFile2array {
    my @matrix = {};
    my $matrixFile = "../../python/test_matrices/testMatrix1.txt";
    open my $MATRIXFILE, '<', $matrixFile
        or die "Couldn't open $matrixFile";
    my $dimension = <$MATRIXFILE>;
    return $dimension;
    # return @matrix;
}

=head1 AUTHOR

eevvoor, C<< <eevvoor at mailbox.org> >>

=head1 BUGS

Please report any bugs or feature requests to TODO github link


=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc FourCornersProblem::Case1111


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<https://rt.cpan.org/NoAuth/Bugs.html?Dist=FourCornersProblem-Case1111>

=item * AnnoCPAN: Annotated CPAN documentation

L<http://annocpan.org/dist/FourCornersProblem-Case1111>

=item * CPAN Ratings

L<https://cpanratings.perl.org/d/FourCornersProblem-Case1111>

=item * Search CPAN

L<https://metacpan.org/release/FourCornersProblem-Case1111>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

This software is Copyright (c) 2020 by eevvoor.

This is free software, licensed under:

  The Artistic License 2.0 (GPL Compatible)


=cut

1; # End of FourCornersProblem::Case1111
