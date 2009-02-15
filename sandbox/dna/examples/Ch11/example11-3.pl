#!/usr/bin/perl -w
use strict;

my (@DB, $i);
for ($i = 0; $i < @ARGV; $i++) {
    if ($ARGV[$i] =~ /\s/) {
        @DB = split(/\s+/, $ARGV[$i]);
        last;
    }
}

exec("xdget @ARGV") unless @DB;

my @pre = splice(@ARGV, 0, $i);
my @post = splice(@ARGV, 1);
foreach my $db (@DB) {
    system("xdget @pre $db @post");
}
