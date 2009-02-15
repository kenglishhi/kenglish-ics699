#!/usr/bin/perl -w
use strict;

die "usage: $0 <wu-blast command line>\n" unless @ARGV >= 3;
my ($BLAST, $DB, $Q, @P) = @ARGV;

die "ERROR ($0): single FASTA files only\n" if `grep -c ">" $Q` > 1;
my $params = "@P";
die "ERROR ($0): filter ahead of time\n" if $params =~ /filter|wordmask/;
open(FASTA, $Q) or die;
my $def = <FASTA>;
my $count = 0;
while (<FASTA>) {$count += length($_) -1}
my $segment = 100000;
for (my $i = 1; $i <= $count; $i += $segment) {
    system("$BLAST $DB $Q  nwstart=$i nwlen=$segment");
}
