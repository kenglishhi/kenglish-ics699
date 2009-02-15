#!/usr/bin/perl -w
use strict;

# Shannon Entropy Calculator
my %Count;								# stores the counts of each symbol
my $total =0;							# total symbols counted

while (<>){	                            # read lines of input
	foreach my $char (split(//,$_)){	# split the line into characters
		$Count{$char}++;				# add one to this character count
		$total++;						# add one to total counts
	}
}

my $H =0;								# H is the entropy
foreach my $char (keys %Count){			# iterate through characters
	my $p =$Count{$char}/$total;		# probability of character
	$H +=$p *log($p);					# p *log(p)
}
$H = -$H/log(2);						# negate sum,convert base e to base 2

print "H = $H bits \n";					# output
