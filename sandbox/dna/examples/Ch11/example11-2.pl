#!/usr/bin/perl
use Bio::SeqIO;

my %NR;
my $file = Bio::SeqIO->new(-fh =>\*ARGV);
while (my $fasta =$file->next_seq){
	my $def = $fasta->id . "" . $fasta->desc;
	$NR{$fasta->seq}{$def} = 1;
}
for my $seq(keys %NR) {
	print ">", join(chr(1), keys %{$NR{$seq}}), "\n", $seq, "\n";
}
