#!/usr/bin/env python

import csv
import sys
import pysam

f1=sys.argv[1]
f2=sys.argv[2]
mxreads=sys.argv[3]

samfile = pysam.AlignmentFile(f2, "rb")

with open(f1, 'rb') as m1:
  for line  in m1:
    if not line.startswith("#"):
       rows = line.strip().split("\t")
       chrnum = rows[0]
       pos =  int(rows[1])
       snpref= rows[3]
       snpvar= rows[4]

       snplen = len(snpvar)

       if snplen > 1:
         continue

       denovo = 0

       readnum = 0
       for pileupcolumn in samfile.pileup(chrnum , pos-1, pos):
          for pileupread in pileupcolumn.pileups:
              if pileupcolumn.pos == pos-1:
                   if pileupread.query_position != None :
                      if pileupread.alignment.query_qualities[pileupread.query_position] > 0 :
                       base = pileupread.alignment.query_sequence[pileupread.query_position:pileupread.query_position+snplen]
                       readnum += 1
                       
                       if base == snpvar :
                          denovo += 1



       if denovo <= int(mxreads) and readnum>=10 :
           
           print line.strip()



