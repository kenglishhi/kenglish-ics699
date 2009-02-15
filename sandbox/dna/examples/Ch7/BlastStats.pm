##############################################################################
# BlastStats.pm
#
# In order to use this module, you must "use" it  from your perl program. For
# example:
#
#         #!/usr/bin/perl -w
#         use strict
#         use BlastStats;
#
# If you get a message "Can't locate  BlastStats.pm in @INC (...), this module
# is not being found by the program. Either place this in the same directory
# as the program, in the library include path indicated by ... above, or
# include a "use lib" to point to the directory contains the BlastStats.pm
# file. For example:
#
#         #!/usr/bin/perl -w
#         use strict;
#         use lib "/home/my_favorite_directory";
#         use BlastStats;
#
##############################################################################

package BlastStats;
use strict;
use vars qw(@ISA @EXPORT $VERSION);
use Exporter;
@ISA = qw(
          Exporter
       );

@EXPORT = qw(nToB
             bToN
             rawScoreToBitScore
             rawScoreToExpect
             bitScoreToExpect
             effectiveLengthSeq
             effectiveLengthDb
             EtoP
             PtoE
             sumScore
             effectiveLengthOfBlastxQuery
             pairwiseSumP
             rTestsCorrectedP
             dbSizeCorrectedExpect
             expectedHSPlength
             rawScoreOfExpectOne
             sumScore
            );

#------------------------------------------------------------------------------
#------------------------------- FUNCTIONS -----------------------------------
#------------------------------------------------------------------------------
sub nToB {
        my $n = shift;

        return $n/log(2); # converts nats to bits
}
#-----------------------------------------------------------------------------
sub bToN {
        my $n = shift;

        return $n*log(2); # converts bits to nats
}
#-----------------------------------------------------------------------------
sub rawScoreToBitScore {
	my $raw_score 	= shift;
	my $k			= shift;	
	my $l         	= shift; #in nats	
	
	return nToB($l*$raw_score - log($k));

}
#-----------------------------------------------------------------------------
sub rawScoreToExpect {
        my $raw_score = shift;
        my $k         = shift;
        my $l         = shift; #in nats
        my $m         = shift; # effective length of query
        my $n         = shift; # effective length of database

        return $k*$m*$n*exp(-1*$l*$raw_score);

}
#-----------------------------------------------------------------------------
sub bitScoreToExpect {
        my $bit_score = shift;
        my $m         = shift; # effective length query
        my $n         = shift; # effective length of database

        return $m*$n*2**(-1*$bit_score);

}
#-----------------------------------------------------------------------------
sub effectiveLengthSeq {
        my $m                   = shift; # actual length
        my $expected_HSP_length = shift;
        my $k                   = shift; # gapped k

        my $m_prime = $m - $expected_HSP_length;

        if ($m_prime < 1/$k){
                return 1/$k;
        }
        else {
                return $m_prime;
        }

}
#-----------------------------------------------------------------------------
sub effectiveLengthDb {
        my $n                    = shift; # actual length
        my $expected_HSP_length  = shift;
        my $num_seqs_in_db       = shift;
        my $k                    = shift; # gapped k

        my $n_prime = $n - ($num_seqs_in_db*$expected_HSP_length);


        if ($n_prime < 1/$k){
                return 1/$k;
        }
        else {
                return $n_prime;

        }
}
#-----------------------------------------------------------------------------
sub EtoP {
        my $e = shift;

        return 1-exp(-1*$e);
}
#-----------------------------------------------------------------------------
sub PtoE {
        my $p = shift;

        return -1*log(1-$p);
}
#-----------------------------------------------------------------------------
sub sumScore {
        my $raw_scores = shift; # raw scores are in an array reference
        my $k          = shift;
        my $l          = shift;
        my $m          = shift; # effective length of query sequence
        my $n          = shift; # effective length of sbjct sequence
        my $g          = shift; # gap size; for NCBI-BLAST this value is 50.

        my $r = @{$raw_scores};

        die "do not take sum for a single score!\n"
        if $r == 1;

        my $total_raw_score = 0;
        foreach my $individual_raw_score (@{$raw_scores}){
                $total_raw_score += $individual_raw_score;
        }
	 
	 my $n_score = $l*$total_raw_score; 
       return $n_score - log($k*$m*$n)  - ($r -1)*(log($k) + 2*log($g)) - log(fac($r));
}
#-----------------------------------------------------------------------------
sub effectiveLengthOfBlastxQuery {
        my $m     = shift;  # actual nucleotide length of the query
        my $exp   = shift;  # expected HSP length.

        return $m/3 - $exp;
}
#-----------------------------------------------------------------------------
sub pairwiseSumP {
        my $sumS = shift; # the sum score
        my $r    = shift; # number of HSPs being combined


        return (exp(-1*$sumS)*$sumS**fac($r-1))/(fac($r)*fac($r -1));

}
sub fac {
        my $r = shift;

        my $fac;
        for (my $i = $r; $i > 0; $i--){
                $fac = defined($fac) ? $fac*$i: $i;
        }
        $fac = 1 unless defined($fac);
        return $fac;
}
#-----------------------------------------------------------------------------
sub rTestsCorrectedP {
        my $r     = shift;
        my $sum_p = shift;
        my $beta  = shift; # gap decay constant


     return $sum_p/($beta**($r-1)*(1-$beta));

}
#-----------------------------------------------------------------------------
sub dbSizeCorrectedExpect {
        my $sumP                = shift;
        my $effective_length_db = shift; #different than the book
        my $sbjct_seq_length    = shift;

        return ($effective_length_db/$sbjct_seq_length)*$sumP;#different than the book
}
#-----------------------------------------------------------------------------
sub expectedHSPlength{
        my $k = shift;
        my $m = shift; # actual length of query 
        my $n = shift; # actual length of database 
        my $h = shift; # average nats/aligned pair

        return  log($k*$m*$n)/$h;

}
#-----------------------------------------------------------------------------
sub rawScoreOfExpectOne {
        my $k = shift;
        my $m = shift; # actual length of query 
        my $n = shift; # actual length of database 
        my $l = shift;

        return  log($k*$m*$n)/$l;
}
#-----------------------------------------------------------------------------
1;






