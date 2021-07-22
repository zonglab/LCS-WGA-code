#!/usr/bin/env python

import csv
import sys
import pysam

x1=sys.argv[1]
x2=sys.argv[2]

filename1=x1
filename2=x2


with open(filename1) as f1, open(filename2) as f2:
  for line, line2 in zip(f1, f2):

       rows = line.strip().split("\t")
       rows2 = line2.strip().split("\t")
       chrnum = rows[0]
       pos =  int(rows[1])
       snpref= rows[3]
       snpvar= rows[4]

       snplen = len(snpvar)

       if snplen > 1 :
           continue

       localseq = rows2[2][:10]
       localseq2 = rows2[2][10:]

       if ( localseq.count('A')+localseq.count('a') >=8 or  \
            localseq.count('T')+localseq.count('t') >=8 or  \
            localseq.count('G')+localseq.count('g') >=8 or  \
            localseq.count('C')+localseq.count('c') >=8 ) :
          continue

       if ( localseq2.count('A')+localseq2.count('a') >=8 or  \
            localseq2.count('T')+localseq2.count('t') >=8 or  \
            localseq2.count('G')+localseq2.count('g') >=8 or  \
            localseq2.count('C')+localseq2.count('c') >=8 ) :
          continue

       print line.strip()

