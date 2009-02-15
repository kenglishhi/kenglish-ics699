#!/usr/bin/perl -w
use strict;

die "usage: $0 <matrix> <word> <threshold>\n" unless @ARGV == 3;
my ($matrix_file, $WORD, $T) = @ARGV;
$WORD = uc $WORD; # differs from version in book
my @W = split(//, $WORD);

die "words must be 3 long\n" unless @W == 3;

my @A = split(//, "ARNDCQEGHILKMFPSTWYVBZX*"); # alphabet
my %S;                                         # Scoring matrix

# Read scoring matrix - use those provided by NCBI-BLAST or WU-BLAST
open(MATRIX, $matrix_file) or die;
while (<MATRIX>) {
    next unless /^[A-Z\*]/;
    my @score = split;
    my $letter = shift @score;
    for (my $i = 0; $i < @A; $i++) {
        $S{$letter}{$A[$i]} = $score[$i];
    }
}

# Calculate neighborhood
my %NH;
for (my $i = 0; $i < @A; $i++) {
    my $s1 = $S{$W[0]}{$A[$i]};
    for (my $j = 0; $j < @A; $j++) {
        my $s2 = $S{$W[1]}{$A[$j]};
        for (my $k = 0; $k < @A; $k++) {
            my $s3 = $S{$W[2]}{$A[$k]};
            my $score = $s1 + $s2 + $s3;
            my $word = "$A[$i]$A[$j]$A[$k]";
            next if $word =~ /[BZX\*]/;
            $NH{$word} = $score if $score >= $T;
        }
    }
}

# Output neighborhood
foreach my $word (sort {$NH{$b} <=> $NH{$a} or $a cmp $b} keys %NH) {
    print "$word $NH{$word}\n";
}
