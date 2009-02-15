#!/usr/bin/perl -w
use strict;

my ($def, @seq) = <>;
print $def;
chomp @seq;
@seq = split(//, join("", @seq));
my $count = 0;
while (@seq) {
	my $index = rand(@seq);
	my $base = splice(@seq, $index, 1);
	print $base;
	print "\n" if ++$count % 60 == 0;
}
print "\n" unless $count %60 == 0;# differs from version in the book
