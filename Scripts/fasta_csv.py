#! usr/bin/python/

#script for extracting data from a fasta file 
#Script written by Charles N. Agoti, inspired by Dr. Matthew Cotten
#Started on 18th Apr 2013, Version 1.0

import sys
import os.path
sys.path.insert(0,"/Users/mikemwanga/Documents/progs/biopython-master")

import csv
from Bio import Seq
from Bio import SeqRecord
from Bio import SeqIO

if len(sys.argv) !=2:
	print "Usage: infoseq.py, <input fasta file>"
	sys.exit()
	


file = sys.argv[1]
outprefix = os.path.splitext(file)[0]
print outprefix

info_table = open(outprefix+'_info_details.csv', 'a')
info_table.write("Accession, seq_len, Ns, actualseq\n")
info_table.close()

count=0
for seq_record in SeqIO.parse(file, "fasta"):
	count=count+1
	print seq_record.id
	print repr(seq_record.seq)
	print len (seq_record)
	
	seq_id=seq_record.id
	seq_len=len(seq_record)
	actualseq=seq_record.seq
	Ns=seq_record.seq.count("N")
	

	info_table = open(outprefix+'_info_details.csv', 'a')
	info_table.write(('%s,%s,%s,%s\n')%(seq_id,seq_len,Ns,actualseq))
	info_table.close()

print "Number of sequences in the file is %d" % count
print "God is good!"
	
