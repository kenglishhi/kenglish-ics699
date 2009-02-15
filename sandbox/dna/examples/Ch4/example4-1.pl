#!/usr/bin/perl -w
use strict;
use constant Pn => 0.25; # probability of any nucleotide

die "usage: $0 <match> <mismatch>\n" unless @ARGV == 2;
my ($match, $mismatch) = @ARGV;
my $expected_score = $match * 0.25 + $mismatch * 0.75;
die "illegal scores\n" if $match <= 0 or $expected_score >= 0;

# calculate lambda
my ($lambda, $high, $low) = (1, 2, 0); # initial estimates
while ($high - $low > 0.001) {         # precision

    # calculate the sum of all normalized scores
    my $sum = Pn * Pn * exp($lambda * $match)    * 4
            + Pn * Pn * exp($lambda * $mismatch) * 12;

    # refine guess at lambda
    if ($sum > 1) {
        $high = $lambda;
        $lambda = ($lambda + $low)/2;
    }
    else {
        $low = $lambda;
        $lambda = ($lambda + $high)/2;
    }
}

# compute target frequency and H
my $targetID = Pn * Pn * exp($lambda * $match) * 4;
my $H = $lambda * $match    *     $targetID
      + $lambda * $mismatch * (1 -$targetID);

# output
print "expscore: $expected_score\n";
print "lambda:   $lambda nats (", $lambda/log(2), " bits)\n";
print "H:        $H nats (", $H/log(2), " bits)\n";
print "%ID:      ", $targetID * 100, "\n";
