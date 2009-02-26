<?xml version="1.0" encoding="UTF-8"?>
<fastafiles>
% for fasta in c.fasta_files:
  <fastafile>
    <filename>${fasta.filename}</filename>
    <size>${fasta.size}</size>
    <mod_time>${fasta.modTime()}</mod_time>
    <sequence_count>${fasta.sequence_count()}</sequence_count>

  </fastafile>
% endfor
</fastafiles>
