#!/usr/bin/perl -w
use strict;
die "usage: $0 <fasta file> <size> <overlap>\n" unless @ARGV == 3;
my ($file, $size, $overlap) = @ARGV;

my $def = "";
my $dna = "";
my $sequence = 0;
my $fragment = 0;

open(IN, $file) or die;
while (<IN>) {
    chomp;
    if (/^>(.+)/) {
        segment();
        $def = $1;
        $sequence++;
        $fragment = 1;
        $dna = "";
    }
    else {
        $dna .= $_;
    }
    while (length($dna) > $size) {segment()}    
}

sub segment {
    return unless $dna;
    my $output = substr($dna, 0, $size);
    if (length($output) == $size) {
        $dna = substr($dna, $size - $overlap);
    }
    else {
        $dna = "";
    }
    my $start = ($fragment -1) * ($size - $overlap) + 1;
    my $end = $start + length($output) -1;
    print ">lcl|$sequence-$fragment {$start..$end} $def\n";
    for (my $i = 0; $i < length($output); $i+= 80) {
        print substr($output, $i, 80), "\n";
    }
    $fragment++;
}
