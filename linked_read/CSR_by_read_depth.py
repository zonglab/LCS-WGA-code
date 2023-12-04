#import pandas as pd

import sys

inputfile = sys.argv[1]

readcount= {}
denovocount= {}
accudenovo= {}
accutotal= {}
df=[]

lira = open(inputfile, "r")

count=0
total=0
for line in lira:
	lineset = line.strip('\n').split('\t')

	if int(lineset[3])+int(lineset[4]) not in readcount:
		readcount[int(lineset[3])+int(lineset[4])] =1
	else:
		readcount[int(lineset[3])+int(lineset[4])] +=1

	if (int(lineset[4])==0 ) :
		if int(lineset[3]) not in denovocount :
			denovocount[int(lineset[3])] = 1
		else:
			denovocount[int(lineset[3])] += 1

readcount_list = list(readcount.keys())
readcount_list.sort(reverse=False)

accuread=0
for i in readcount_list:
	if i in denovocount: 
		accuread += readcount[i]
		#print(i,"\t", float(denovocount[i])/accuread)
		print(i,denovocount[i],accuread,float(denovocount[i])/accuread, sep='\t')
		accuread = 0
	else :
		accuread +=readcount[i]


lira.close()

print(accuread)
