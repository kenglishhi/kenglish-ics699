#!/usr/bin/perl -w
use strict;
use Bio::SearchIO;

my $blast = new Bio::SearchIO(
    -format => 'blast',
    -file   => $ARGV[0]);

my %Name;
while(my $result = $blast->next_result) {
    while(my $sbjct = $result->next_hit) {
        while(my $hsp = $sbjct->next_hsp) {
            $Name{$sbjct->name} = 1 if $hsp->frac_identical >= 0.9;
        }
    }
}

print join("\n", sort keys %Name), "\n";
