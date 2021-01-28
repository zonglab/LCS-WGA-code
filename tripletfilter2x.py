#!/usr/bin/env python

import csv
import sys
import pysam

f1=sys.argv[1]
f2=sys.argv[2]
f3=sys.argv[3]
f4=sys.argv[4]
f5=sys.argv[5]


#samfile = pysam.AlignmentFile("/data1/czong/genome/X10_031617_analysis/Sample_HHHJ3ALXX-1-IDN702/mergedclone1bulk_RG.bam", "rb")
samfile1 = pysam.AlignmentFile(f2, "rb")
samfile2 = pysam.AlignmentFile(f3, "rb")
samfile3 = pysam.AlignmentFile(f4, "rb")

#print "#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT"

with open(f1, 'rb') as m1:
#    data1 = csv.reader(m1,delimiter='	')
#    mydict1 = {rows[1]:rows[4] for rows in data1}
   for line  in m1:

     li=line.strip()

     if not li.startswith("#"):

       rows = li.split("\t")
       #snp.append(int(rows[1]))
       #chrnum = int(rows[0][3:])
       chrnum = rows[0]
       pos =  int(rows[1])
       snpref= rows[3]
       snpvar= rows[4]
       snpQual= float(rows[5])

       snplen = 1
       #snplen = len(snpvar)

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
                   #print "position", pileupread.query_position
                   if pileupread.query_position != None : 
                     base = pileupread.alignment.query_sequence[pileupread.query_position: pileupread.query_position+snplen]
                     qual =  pileupread.alignment.query_qualities[pileupread.query_position: pileupread.query_position+snplen][0]
                     #print base
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
                   #print "position", pileupread.query_position
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
                   #print "position", pileupread.query_position
                   if pileupread.query_position != None :
                     base = pileupread.alignment.query_sequence[pileupread.query_position: pileupread.query_position+snplen]
                     qual =  pileupread.alignment.query_qualities[pileupread.query_position: pileupread.query_position+snplen][0]
                     if base == snpvar and qual > 30 :
                        denovo3 += 1
              foundread.append(pileupread.alignment.qname)
          if(read3>0): af3= float(denovo3)/read3

       #print pos-1,denovo1, denovo2, denovo3, read1, read2, read3

       #if (denovo1>=2 and denovo2>=2) or (denovo2>=2 and denovo3>=2) or (denovo1>=2 and denovo3>=2) or (denovo1>=1 and denovo2>=1 and denovo3>=1)  :
       #if (denovo1>=1 and denovo2+denovo3>=2) or (denovo2>=1 and denovo1+denovo3>=2) or (denovo3>=1 and denovo1+denovo2>=2)  :
       if (denovo1+denovo2+denovo3>=3):
          ##if ( af1+af2+af3>1.5) :
          if ( af1>  float(f5) and af2>  float(f5) ) or (  af1>  float(f5)  and af3>  float(f5)  ) or (af2>  float(f5)  and af3>  float(f5)  ) :
          #if ( af1>0 and af2>0 and af3>0 and (af1+af2+af3)> float(f5) ) :

            print line.strip()



       #splitcount=0
       #if denovo1>=1 :
          #if float(denovo1)/read1>0.2  :
       #       splitcount += 1
       #if denovo2>=1 :
          #if float(denovo2)/read2>0.2 :
       #       splitcount += 1
       #if denovo3>=1 :
          #if float(denovo3)/read3>0.2 :
       #       splitcount += 1


       #if splitcount >= 2 :
       #if denovo1 >=2 and denovo2 >=2 and denovo3 >=2  :
           #print  "denovo"
       #    print line.strip()
           #print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(snpvcf[pos][0], snpvcf[pos][1],snpvcf[pos][2],snpvcf[pos][3], \
	   #           snpvcf[pos][4],snpvcf[pos][5],snpvcf[pos][6],snpvcf[pos][7]))
