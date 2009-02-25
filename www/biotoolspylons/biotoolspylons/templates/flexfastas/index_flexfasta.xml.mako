<?xml version="1.0" encoding="UTF-8"?>
<fastafiles>
% for file in c.fasta_files:
  <fastafile>
    <filename>${file.filename}</filename>
    <size>${file.size}</size>
  </fastafile>
% endfor
</fastafiles>
