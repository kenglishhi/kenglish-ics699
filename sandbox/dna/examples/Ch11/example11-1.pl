#!/usr/bin/perl
$i = 2147483648;
while (<>){
	if (/^>/){
		$i--;
		print ">gi|$i (fake-gi) ", substr($_, 1); # differs from version in the book
	}
	else {
		print;
	}
}
