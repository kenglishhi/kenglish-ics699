#!/usr/bin/perl -w
use strict;
die "usage: $0 <database> <query> <wordsize> <hitdist>\n" unless @ARGV == 4;
my ($DB, $Q, $W, $H) = @ARGV;
$H = $H ? "hitdist=$H" : "";
my $tmpdir = "/tmp/tt-blastx.tmpdir";
END {system("rm -rf $tmpdir") if defined $tmpdir}
system("mkdir $tmpdir") == 0 or die "ERROR ($0): can't create $tmpdir\n";
my $STD = "B=100000 V=100000 wordmask=seg";

# search
system("blastx $DB $Q W=$W T=999 $H $STD > $tmpdir/search") == 0 or die;

# collect names
my @name;
open(NAME, ">$tmpdir/names") or die;
open(SEARCH, "$tmpdir/search") or die;
while (<SEARCH>) {print NAME "$1\n" if /^>(\S+)/}
close SEARCH;
close NAME;

# build second stage database
system("xdget -p -f $DB $tmpdir/names > $tmpdir/database") == 0 or die;
system("xdformat -p $tmpdir/database") == 0 or die;

# align
system("blastx $tmpdir/database $Q $STD") == 0 or die;
