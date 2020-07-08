#!/usr/bin/env python

import csv
import sys
import pysam

f1=sys.argv[1]
f2=sys.argv[2]
f3=sys.argv[3]
f4=sys.argv[4]
f5=sys.argv[5]


samfile1 = pysam.AlignmentFile(f2, "rb")
samfile2 = pysam.AlignmentFile(f3, "rb")
samfile3 = pysam.AlignmentFile(f4, "rb")

with open(f1, 'rb') as m1:
   for line  in m1:

     li=line.strip()

     if not li.startswith("#"):

       rows = li.split("\t")
       chrnum = rows[0]
       pos =  int(rows[1])
       snpref= rows[3]
       snpvar= rows[4]
       snpQual= float(rows[5])

       snplen = 1
)

       denovo1 = 0
       denovo2 = 0
       denovo3 = 0

       read1 = 0
       read2 = 0
       read3 = 0
       af1=0.0
       af2=0.0
       af3=0.0

       if snpQual > 5000 :
          continue


       for pileupcolumn in samfile1.pileup(chrnum , pos-1, pos):
          foundread = []
          for pileupread in pileupcolumn.pileups:

            try:
              foundread.index(pileupread.alignment.qname)
            except ValueError :

              if (pileupread.alignment.mapping_quality < 50):
                  continue
              if pileupcolumn.pos == pos-1:
                   read1 += 1
                   if pileupread.query_position != None :
                     base = pileupread.alignment.query_sequence[pileupread.query_position: pileupread.query_position+snplen]
                     qual =  pileupread.alignment.query_qualities[pileupread.query_position: pileupread.query_position+snplen][0]
                     if base == snpvar and qual > 30:
                        denovo1 += 1
              foundread.append(pileupread.alignment.qname)
          if (read1>0 ): af1= float(denovo1)/read1


       for pileupcolumn in samfile2.pileup(chrnum , pos-1, pos):
          foundread = []
          for pileupread in pileupcolumn.pileups:

            try:
              foundread.index(pileupread.alignment.qname)
            except ValueError :
              if (pileupread.alignment.mapping_quality < 50):
                  continue
              if pileupcolumn.pos == pos-1:
                   read2 += 1
                   if pileupread.query_position != None :
                     base = pileupread.alignment.query_sequence[pileupread.query_position: pileupread.query_position+snplen]
                     qual =  pileupread.alignment.query_qualities[pileupread.query_position: pileupread.query_position+snplen][0]
                     if base == snpvar and qual > 30:
                        denovo2 += 1
              foundread.append(pileupread.alignment.qname)
          if (read2>0): af2= float(denovo2)/read2


       for pileupcolumn in samfile3.pileup(chrnum , pos-1, pos):
          foundread = []
          for pileupread in pileupcolumn.pileups:
            try:
              foundread.index(pileupread.alignment.qname)
            except ValueError :
              if (pileupread.alignment.mapping_quality < 50):
                  continue
              if pileupcolumn.pos == pos-1:
                   read3 += 1
                   if pileupread.query_position != None :
                     base = pileupread.alignment.query_sequence[pileupread.query_position: pileupread.query_position+snplen]
                     qual =  pileupread.alignment.query_qualities[pileupread.query_position: pileupread.query_position+snplen][0]
                     if base == snpvar and qual > 30 :
                        denovo3 += 1
              foundread.append(pileupread.alignment.qname)
          if(read3>0): af3= float(denovo3)/read3


       if (denovo1+denovo2+denovo3>=3):
          if ( af1>  float(f5) and af2>  float(f5) and af3>  float(f5)  ) :

            print line.strip()







